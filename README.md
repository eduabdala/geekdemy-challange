# Geektrust - geekdemy - Documentation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

This repository contains documentation and explanations of the solution architecture and design decisions made for the **Geektrust - Geekdemy.** coding challange.

---

## 📂 Documentation Index

This project contains multiple structured sections:

- [`Command Instructions`](#commands)
- [`📘 1. Problem Summary`](docs/context.md)
- [`📘 2. Input Summary`](docs/sampleio.md#-input-commands)
- [`📘 3. Output Summary`](docs/sampleio.md#-output-format)
- [`📘 4. Assumptions`](docs/assumptions.md)
- [`📘 5. Goal`](docs/goal.md)
- [`📘 6. Cupons`](docs/cupons.md)

- [`Development path`](docs/development_path.md)

---

## Commands

Use the following commands to configure, run, and manage the project:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# (Optional) Run the startup script
./run.sh

# Install dependencies
pip install -r requirements.txt

# Run the application with a sample input
python3 -m geektrust sample_input/input1.txt

# Deactivate the virtual environment when finished
deactivate
