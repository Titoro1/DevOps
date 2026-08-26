# Calculator Project

A simple calculator command-line tool supporting addition, subtraction, multiplication, and division.

## Installation

```bash
uv sync
```

## Usage

```bash
uv run calculator --add 10 5
uv run calculator --subtract 10 5
uv run calculator --multiply 10 5
uv run calculator --divide 10 5
```

Note: if you see 'Failed to spawn':

```bash
uv run -m df00_calculator_joeytribbiani.cli --add 10 5
uv run -m df00_calculator_joeytribbiani.cli --subtract 10 5
uv run -m df00_calculator_joeytribbiani.cli --multiply 10 5
uv run -m df00_calculator_joeytribbiani.cli --divide 10 5
```

## Run tests

```bash
uv run pytest
```

## Build

```bash
uv build
```

The `.whl` and `.tar.gz` files will be output to the `dist/` directory.
