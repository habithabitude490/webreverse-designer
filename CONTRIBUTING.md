# Contributing — WebReverse Designer

Thanks for contributing! Simple rules:

1. **Scope**: analysis and documentation only. No PR that generates
   or rebuilds sites, no access bypassing.
2. **Style**: Python 3, stdlib preferred; any dependency must be
   justified in the PR and documented in the README.
3. **Tests**: `python3 -m unittest discover -s tests -v` must pass.
   Add a test for every new script behavior.
4. **Evidence**: fictional or authorized examples only (compatible license).
   Never proprietary code, secrets, or screenshots of sites without rights.
5. **Docs**: update `CHANGELOG.md` (`Unreleased` section) and the README
   if behavior changes.

## Workflow
```bash
git clone <your-fork>
cd webreverse-designer
python3 -m unittest discover -s tests -v
# … changes …
python3 -m unittest discover -s tests -v
```
