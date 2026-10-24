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

The hooks require `uv` to be installed. GitHub Actions also runs the test suite
on pushes and pull requests. To require the GitHub check before merging, enable
branch protection and mark the `Tests / test` check as required; GitHub Actions
cannot reject a push after it has already reached the remote.