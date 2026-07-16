# Brainfuck Interpreter

A Brainfuck interpreter written completely from scratch in Python.

This project implements the complete Brainfuck instruction set and provides a command-line interface for executing `.bf` programs.

## Features

- Complete Brainfuck instruction set
  - `>`
  - `<`
  - `+`
  - `-`
  - `.`
  - `,`
  - `[`
  - `]`
- Nested loop support
- Jump table preprocessing for efficient loop execution
- Syntax validation for unmatched brackets
- 30,000-cell memory tape
- 8-bit memory cells (0–255 wrapping)
- Command-line interface

## Installation

Clone the repository:

```bash
git clone https://github.com/RonsumGameDev/brainfuck-interpreter.git
cd brainfuck-interpreter
```

Install in editable mode:

```bash
pip install -e .
```

## Usage

Run a Brainfuck program:

```bash
bf hello.bf
```

or

```bash
python -m brainfuck hello.bf
```

## Project Structure

```
brainfuck-interpreter/
│
├── brainfuck/
│   ├── __main__.py
│   ├── interpreter.py
│   ├── preprocessor.py
│   └── __init__.py
│
├── tests/
├── pyproject.toml
└── README.md
```

## Roadmap

- Interactive debugger
- Memory visualization
- Execution tracing
- Performance optimizations
- Interactive REPL
- Brainfuck compiler utilities

## License

This project is licensed under the MIT License.

---

### Note

The Brainfuck interpreter and its implementation were written by me from scratch.

Only this `README.md` was created with the assistance of AI for documentation and formatting purposes.
