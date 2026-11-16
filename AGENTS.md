# Repository Guidelines

## Project Structure & Module Organization

This repository is currently an empty starting point: no application source, tests, assets, or dependency manifests have been committed. Keep the root focused on project configuration and documentation. As implementation begins, group application code in `src/`, automated tests in `tests/`, and sample input data in a clearly named directory such as `fixtures/`. Document the actual structure when these directories are introduced.

## Build, Test, and Development Commands

No build, test, lint, or local development commands are configured yet. When adding a toolchain, provide reproducible commands in a `README.md` and commit the relevant dependency manifest and lockfile. Explain prerequisites and distinguish commands for installation, local execution, testing, and production builds. Do not document commands as available until their configuration exists.

## Coding Style & Naming Conventions

Follow the conventions of the language and framework selected for the implementation. Use consistent indentation, descriptive names, and small modules with clear responsibilities. Configure a formatter and linter early; prefer their enforced rules over manual formatting preferences. Name files consistently within each module and avoid unrelated formatting changes.

## Testing Guidelines

No testing framework or coverage threshold is configured. Add automated tests alongside new behavior and regression tests for bug fixes. Use descriptive test names that identify the behavior and expected outcome. If implementing iperf output parsing, include representative valid, malformed, and incomplete input fixtures. Document the test command once a framework is selected.

## Commit & Pull Request Guidelines

There is no commit history from which to infer an established convention. Use concise, imperative commit subjects, such as `Add iperf output parser`, and keep commits focused. Pull requests should explain the change, link relevant issues, and report validation performed or why validation was unavailable. Include screenshots when changing a user interface.

## Security & Configuration

Never commit credentials or private network captures. Sanitize sample data and use environment variables for secrets. Document required configuration with safe placeholder values.
