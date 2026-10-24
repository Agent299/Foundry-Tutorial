# Foundry Tutorial

## Tests and Git hooks

The test suite uses Python's standard-library `unittest` runner. Run it locally
with:

```sh
uv run --locked python -m unittest discover -s tests -v
```

To run the same checks automatically before each commit and push in this
checkout, configure the repository hooks path once:

```sh
git config --local core.hooksPath .githooks
```

The hooks require `uv` to be installed. Create changes on a temporary branch
from `main`, push that branch, then open a pull request into `main`:

```sh
git switch main
git pull --ff-only
git switch -c feature/short-description
```

GitHub Actions tests pushes to non-`main` branches and pull requests targeting
`main`. To prevent direct pushes and require passing tests before merging, enable
branch protection or a ruleset for `main`, require pull requests, and mark the
`Tests / test` check as required. These repository settings must be enabled in
GitHub; the workflow alone cannot enforce them.