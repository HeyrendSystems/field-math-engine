# Field Math Engine

A structured Python calculator for practical field computations.

This repository documents the lifecycle of the project, beginning as a simple area calculator and evolving into a broader field computation engine across multiple technical domains. The system now supports dual-interface deployment, which includes a standard Command Line Interface (CLI) for desktop use and an embedded hardware interface for field use via Raspberry Pi Pico W. 

## Current Architecture
```text
       Desktop CLI                Pico Hardware
        (main.py)                (pico_main.py)
            │                          │
            └────────────┬─────────────┘
                         ▼
                 Calculation Layer
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
   Geometry Domain               Hydraulics Domain
    (Area, Volume)          (Flow, TDH, HP, Velocity)
```
The system is designed so that new computational domains can be added without modifying the core architecture. This separation enables the same logic engine to be driven by either terminal-based user input or physical hardware components like a 4x4 keypad and OLED display.

## Project Structure

```text
.
├── field_math_engine/
│   ├── cli.py
│   ├── constants.py
│   ├── unit_helpers.py
│   ├── geometry/
│   │   ├── area.py
│   │   ├── input_helpers.py
│   │   └── volume.py
│   └── hydraulics/
│       ├── flow.py
│       ├── pump_horsepower.py
│       ├── tdh.py
│       └── velocity.py
├── pico_calculator/
│   ├── keypad_input.py
│   ├── main_menu.py
│   ├── oled_display.py
│   ├── pico_area.py
│   └── sh1106.py
├── main.py
├── pico_main.py
├── LICENSE
└── README.md
```
## Architecture Philosophy

The system is structured around domain ownership and interface abstraction:

- Desktop CLI handles sequential user interaction and command flow in a terminal environment. 
- Embedded Pico implements a manual State Machine within the pico_calculator module to manage keypad polling, numeric buffering, and real-time OLED rendering for handheld use.
- Domain Modules encapsulate pure calculation logic, independent of the user interface.

This separation enables:

- Cross-platform deployment (Desktop vs. Handheld).
- Scalable domain expansion without hardware dependencies.
- Decoupling of physical I/O from mathematical formulas.

## Running the Application

### For running the CLI Application in terminal run

```bash
python3 main.py
```
### For Pico Hardware

> [!NOTE]
> Pico Hardware is currently in the early development stages, with a successful implementation of the area of rectangle calculation.

1. Flash `MicroPython` to the Raspberry Pi Pico W.
2. Upload the `pico_calculator/` directory and `pico_main.py` to the device.
3. The device will boot into the hardware-specific state logic.

## Roadmap

- Add all CLI calculators to Pico 
- Expand supported formulas for all environments (Terminal, Pico, Web)
- Introduce additional domains (electrical, thermodynamics, etc.)
- Expand unit conversion support
- Add test coverage

## Purpose

This project is part of my long-term focus on learning software system engineering and architectural design.
