# Cliplug

A CLI plugin system built with Click.

## Installation

### For Development

1. Activate the virtual environment:
   ```cmd
   .venv\Scripts\activate
   ```

2. Install the package with dev dependencies:
   ```cmd
   pip install -e ".[dev]"
   ```

### For Production

```cmd
pip install cliplug
```

## Usage

```cmd
cliplug --help
```

## Building

To build the package:

```cmd
python -m build
```

This creates distribution files in the `dist/` directory.
