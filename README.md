# Automated Documentation Demo

## Overview

**src/calculator.py** — Calculator module.

Provides basic arithmetic operations.
**src/temperature.py** — Temperature conversion utilities.

Provides functions for converting temperatures between units.

## Source Files

### `src/calculator.py`

**Functions / Methods:**

- `add()`
- `subtract()`
- `multiply()`
- `divide()`

### `src/temperature.py`

**Functions / Methods:**

- `celsius_to_fahrenheit()`
- `fahrenheit_to_celsius()`

## Project Structure

```text
Doxyfile
README.md
docs/index.md
docs/installation.md
docs/javascripts/auto-reload.js
docs/usage.md
mkdocs.yml
scripts/generate_docs.py
scripts/generate_readme.py
src/calculator.py
src/temperature.py
```

## Dependencies

No dependency configuration files were detected.

## Documentation

This project uses automated documentation generation.

- **Doxygen** generates technical documentation from source-code documentation.
- **MkDocs** builds the documentation website.
- **GitHub Actions** automatically regenerates the documentation when changes are pushed.
- **GitHub Pages** publishes the generated documentation.
