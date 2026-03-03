# Field Math Engine

A structured Python calculator for practical field computations.

This repository documents the lifecycle of the project, beginning as a simple area calculator and evolving into a broader field computation engine across multiple technical domains.

Right now it includes:

- A geometry domain
- An area and volume calculation workflow
- A clean separation between application entry point and calculation logic

The goal is to structure the system so that adding new domains does not require restructuring the core. Long term, the project aims to support CLI arguments and eventually expand into web or mobile interfaces.

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

From the project root in your terminal:

```bash
python3 main.py
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

Built as part of my long-term focus on learning software system engineering and architectural design.
