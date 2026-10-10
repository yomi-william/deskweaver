# deskweaver

Desktop automation framework based on pyautogui.

This project applies separation of concerns to desktop automation. The structure prioritizes maintainability over quick scripting. Changes to UI coordinates, validation rules, or peripheral logic are isolated to specific directories. This prevents regression when requirements evolve.

## Architecture

The codebase is divided into four distinct layers. Each layer has a single responsibility and does not import from peer layers.

### 1. Core Actions (`core_actions/`)
Pure execution modules for mouse, keyboard, and screen interactions.
-   **Mouse:** Cursor movement, clicking, scrolling.
-   **Keyboard:** Typing, key presses, shortcuts.
-   **Screen:** Image location, coordinate retrieval, waiting.

These modules perform actions only. They contain no validation logic and no hardcoded data. They rely entirely on `utils` for input checking and `data` for target coordinates.

### 2. Data (`data/`)
Single source of truth for all external references.
-   Stores screen coordinates, image paths, and application-specific mappings.
-   Example: `data/capcut/edit_screen_coords.py` holds all CapCut interface positions.

When a UI element moves, update this file only. No changes are required in core actions or workflows.

### 3. Utils (`utils/`)
Shared infrastructure that enforces system constraints.
-   **Validators:** All input validation (types, ranges, formats) lives here. Core actions call these validators but do not implement them.
-   **Exceptions:** Custom error classes for validation failures and core action errors.

This ensures core actions remain focused solely on execution. Validation rules are centralized and reusable.

### 4. Workflows (`workflows/`)
Business logic composed of core actions and data references.
-   Contains no raw pyautogui calls.
-   Reads as sequential instructions using imported functions and data constants.

```python
from core_actions.mouse import click
from core_actions.screen import wait
from data.capcut.edit_screen_coords import increase_zoom_coords

click(increase_zoom_coords)
wait(2.0)
```

## Practical Impact

| Decision | Result |
| :--- | :--- |
| Coordinates in `data/` only | UI changes require editing one file, not searching through workflow scripts |
| Validation in `utils/` only | Core actions stay minimal; rule changes happen in one place |
| No cross-imports between peripherals | Modifying mouse logic cannot break keyboard or screen functions |
| Workflows use named constants | Code reads as intent, not implementation details |

## Requirements Alignment

Implementation follows the v1.0 specification exactly:
-   Input validation matches defined parameter constraints
-   Error messages distinguish validation failures from core action errors
-   `pyautogui.FAILSAFE` enabled by default
-   Performance timing adheres to specified durations and intervals
-   Python 3.10+ with pyautogui required; opencv-python needed for image confidence

## Setup

1.  Python 3.10+
2.  `pip install pyautogui opencv-python`
3.  Define coordinates in `data/`
4.  Compose workflows in `workflows/`

## Why This Structure

Automation systems fail when they are written as scripts. Scripts couple data, logic, and validation together. When the target application changes, the entire script must be rewritten.

This framework treats automation as software engineering. Separating concerns means each part of the system can change independently. The result is a codebase that accepts new requirements without structural overhaul.