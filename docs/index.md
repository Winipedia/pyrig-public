# Home

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-public/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-public/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-public/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-public/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-public/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-public)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/CI/CD--security-zizmor-yellow)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace--fixer-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![YAMLLinter](https://img.shields.io/badge/YAML-ryl-red)](https://github.com/owenlamont/ryl)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-public?style=social)](https://github.com/Winipedia/pyrig-public)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/Documentation-zensical-326CE5)](https://Winipedia.github.io/pyrig-public)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-public?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-public)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-public)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-public)](https://github.com/Winipedia/pyrig-public/blob/main/LICENSE)

---

> A pyrig plugin for public repository functionality.

---

## Overview

`pyrig-public` extends pyrig's generated GitHub configuration with settings
and policies intended for public repositories. Install the plugin as a
development dependency, then run `pyrig sync`; pyrig discovers and applies the
plugin overrides automatically.

```bash
uv add pyrig-public --dev
uv run pyrig sync
```

This regenerates the local configuration files. GitHub is updated when the
generated `.github/configure.sh` runs, such as in pyrig's deployment workflow.

## Repository visibility

The plugin adds `"visibility": "public"` to the generated repository settings.
When `.github/configure.sh` applies those settings, GitHub updates the
repository through its repository settings API. This is enforced each time the
configuration script runs.

!!! warning "Important"
    Changing a repository's visibility can expose its code and history. GitHub
    also warns that visibility changes can affect stars and watchers, detach
    public forks, disable push rulesets, and make Actions history and logs
    accessible. Confirm the repository contents and any organization visibility
    policy before applying the setting.

## Fork pull request workflows

The generated configuration requires maintainer approval before workflows
from pull requests opened by external contributors' forks run. The policy is
set to `all_external_contributors` through GitHub's fork pull request approval
settings.

## Vulnerability reporting

The plugin enables GitHub private vulnerability reporting for the repository.
It also changes the generated `SECURITY.md` reporting instructions to link to
the repository's private vulnerability reporting form. This gives reporters a
private channel instead of directing them to public issues or discussions.

## API reference

Running `pyrig sync` generates the [API reference](api.md) from the package's
public Python docstrings. For class- and method-level details, see that page.
