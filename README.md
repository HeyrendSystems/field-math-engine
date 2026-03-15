# Field Math Engine

A structured Python calculator for practical field computations.

This repository documents the lifecycle of the project, beginning as a simple area calculator and evolving into a broader field computation engine across multiple technical domains.

## Current Architecture

```
Application Entry Point
        │
        ▼
      main.py
        │
        ▼
    CLI Interface
      (cli.py)
        │
        ▼
   Calculation Layer
        │
 ┌──────┴───────────────┐
 │                      │
 ▼                      ▼
Geometry Domain     Hydraulics Domain
 │                      │
 ├─ Area                ├─ Flow
 └─ Volume              ├─ Velocity
                        ├─ Total Dynamic Head (TDH)
                        └─ Pump Horsepower
```

The system is designed so that new computational domains can be added without modifying the core architecture. Long term, the project aims to support CLI arguments and eventually expand into web or mobile interfaces.

---

## Project Structure
```text
field-math-engine/
│
├── main.py
│
├── field_math_engine/
│   ├── __init__.py
│   ├── cli.py
│   ├── constants.py
│   ├── unit_helpers.py
│
│   ├── geometry/
│   │   ├── __init__.py
│   │   ├── area.py
│   │   ├── volume.py
│   │   └── input_helpers.py
│
│   └── hydraulics/
│       ├── flow.py
│       ├── pump_horsepower.py
│       ├── tdh.py
│       └── velocity.py
│
├── LICENSE
└── README.md
```

---

## Architecture Philosophy

The system is structured around domain ownership:

- `main.py` serves as the application entrypoint.
- The CLI layer handles user interaction and command flow.
- Domain modules encapsulate their own calculation logic.

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
- Introduce additional domains (electrical, thermodynamics, etc.)
- Expand unit conversion support
- Add test coverage

---

## Purpose

This project is part of my long-term focus on learning software system engineering and architectural design.
