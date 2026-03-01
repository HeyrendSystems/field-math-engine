# Field Math Engine

A Python-based field calculator built with clean structure and room to grow.

This started as a simple area calculator, but it’s being built intentionally as a modular system so it can expand into other technical domains like electrical and hydraulics.

---

## Overview

Field Math Engine is structured as a Python package rather than a standalone script.

Right now it includes:

- A geometry domain
- An area calculation workflow
- A clean separation between the entrypoint and calculation logic

The system is organized so adding new domains does not require restructuring the core. The long-term goal is to support CLI arguments and eventually expand into web or mobile interfaces.

---

## Project Structure
```text
field-math-engine/
│
├── field_math_engine/
│   ├── __init__.py
│   └── geometry/
│       ├── __init__.py
│       └── area_calculator.py
│
├── main.py
├── LICENSE
└── README.md
```

---

## Architecture Philosophy

The system is structured around domain ownership:

- `main.py` serves as the application entrypoint.
- Domain modules (e.g., geometry) encapsulate their own workflows.
- Internal calculation logic is isolated from execution logic.

This separation enables:

- Future CLI argument parsing
- Web application integration
- Mobile deployment
- Scalable domain expansion

---

## Running the Application

From the project root:

```bash
python main.py
```

---

## Roadmap

- Add argparse support for CLI arguments
- Expand supported formulas
- Introduce additional technical domains (electrical, hydraulics)
- Expand unit conversion support
- Add test coverage

---

## Purpose

Built as part of my long-term focus on systems engineering and architectural discipline.
