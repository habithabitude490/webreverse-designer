"""WebReverse Designer tests — stdlib unittest only.

Run from the skill root:
    python3 -m unittest discover -s tests -v
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "scripts", "check_project.py")
FIXTURES = os.path.join(ROOT, "tests", "fixtures", "demo-project")


def run_script(*args):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        capture_output=True, text=True, timeout=30)


class TestInventory(unittest.TestCase):
    def test_counts_demo_project(self):
        p = run_script(FIXTURES, "--json")
        self.assertEqual(p.returncode, 0, p.stderr)
        data = json.loads(p.stdout)
        self.assertEqual(data["counts"]["html"], 1)
        self.assertEqual(data["counts"]["css"], 1)
        self.assertEqual(data["counts"]["js"], 2)
        self.assertEqual(data["counts"]["other"], 1)
        self.assertIn("index.html", data["entry_points"])

    def test_refs_detected(self):
        p = run_script(FIXTURES, "--json")
        data = json.loads(p.stdout)
        by_path = {f["path"]: f for f in data["files"]}
        self.assertIn("styles.css", by_path["index.html"]["refs"])
        self.assertIn("app.js", by_path["index.html"]["refs"])
        self.assertIn("btn-primary", by_path["index.html"]["classes"])
        self.assertIn("nav", by_path["index.html"]["ids"])

    def test_css_no_extension_false_positives(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "s.css"), "w") as fh:
                fh.write('@import url("base.css");\n'
                         ".hero { background: url(logo.png); }\n"
                         ".grid { width: 50%; }\n")
            p = run_script(tmp, "--json")
            self.assertEqual(p.returncode, 0, p.stderr)
            data = json.loads(p.stdout)
            classes = data["files"][0]["classes"]
            self.assertIn("hero", classes)
            self.assertIn("grid", classes)
            self.assertNotIn("png", classes)
            self.assertNotIn("css", classes)

    def test_symlinks_skipped_with_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "real.css"), "w") as fh:
                fh.write(".a { color: #333; }\n")
            os.symlink(os.path.join(tmp, "real.css"),
                       os.path.join(tmp, "link.css"))
            p = run_script(tmp, "--json")
            self.assertEqual(p.returncode, 0, p.stderr)
            data = json.loads(p.stdout)
            self.assertEqual(data["counts"]["total"], 1)
            self.assertTrue(any("symlink" in w for w in data["warnings"]))

    def test_excludes_node_modules_and_git(self):
        with tempfile.TemporaryDirectory() as tmp:
            for d in ("node_modules", ".git", "dist"):
                os.makedirs(os.path.join(tmp, d))
                with open(os.path.join(tmp, d, "x.js"), "w") as fh:
                    fh.write("var a = 1;\n")
            with open(os.path.join(tmp, "index.html"), "w") as fh:
                fh.write("<html></html>\n")
            p = run_script(tmp, "--json")
            self.assertEqual(p.returncode, 0, p.stderr)
            data = json.loads(p.stdout)
            self.assertEqual(data["counts"]["total"], 1)
            self.assertEqual(len(data["skipped_dirs"]), 3)

    def test_empty_project_warns_but_ok(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = run_script(tmp, "--json")
            self.assertEqual(p.returncode, 0, p.stderr)
            data = json.loads(p.stdout)
            self.assertEqual(data["counts"]["total"], 0)
            self.assertTrue(any("Empty" in w for w in data["warnings"]))

    def test_missing_dir_exit_1(self):
        p = run_script("/path/that/does/not/exist/at/all")
        self.assertEqual(p.returncode, 1)
        self.assertIn("not found", p.stderr)

    def test_file_path_exit_1(self):
        p = run_script(os.path.join(FIXTURES, "index.html"))
        self.assertEqual(p.returncode, 1)

    def test_bad_encoding_tolerated(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "b.html"), "wb") as fh:
                fh.write(b"<html>\xff\xfe<body>hello</body></html>")
            p = run_script(tmp, "--json")
            self.assertEqual(p.returncode, 0, p.stderr)
            data = json.loads(p.stdout)
            self.assertTrue(data["files"][0]["encoding_issue"])

    def test_text_output_human_readable(self):
        p = run_script(FIXTURES)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("Inventory", p.stdout)
        self.assertIn("index.html", p.stdout)

    def test_version_flag_needs_no_path(self):
        p = run_script("--version")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertRegex(p.stdout.strip(), r"^\d+\.\d+\.\d+$")

    def test_missing_path_prints_usage_exit_1(self):
        p = run_script()
        self.assertEqual(p.returncode, 1)
        self.assertIn("Usage", p.stderr)


if __name__ == "__main__":
    unittest.main()

