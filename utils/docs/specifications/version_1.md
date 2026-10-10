# deskweaver — Requirements Document v1.0

## Overview

This framework based on pyautogui allow a user to build a desktop app automation, recommended to a person that need to automate a manual task on a desktop aplication.

## Features in Scope

### 1. Move Mouse To
An user can move the mouse to a certain position by providing a x(non-negative integer), y(non-negative integer) and an optional duration(positive number greater than or equal 0.1 and less than 10.0, default to 0.3)

if any input is invalid, the system displays an error message identifying wish field failed and the expected format. The action is not performed

if the input are valid but the system cannot perform the action, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed

If all inputs are valid and the action succeeds, the system performs the mouse movimentation operation at the specified location.

**Constraints:**
- Performance: mouse movement should complete within the specified duration parameter (default 0.3 seconds), throughput can handle sequential calls with minimum 0.1 second pause between actions (configurable via pyautogui.PAUSE)
- Security: no user authentication required, fail-safe enabled by default (pyautogui.FAILSAFE = True) - moving mouse to screen corner aborts automation
- Data: `x` must be a non-negative integer. `Y` must be a non-negative integer and `duration` must be a positive number greater than or equal 0.1 and less than 10.0
- Environment: python 3.10 or higher and pyautogui library must be installed. On Linux, is needed gui support check(https://pyautogui.readthedocs.io) for more information.

### 2. click
An user can perform a click with the mouse by providing optional x(non-negative integer, default to None), optional y(non-negative integer, default to None), interval(positive number greater than or equal 0.1 and less than 1.0, default to 0.1), duration(positive number greater than or equal 0.1 and less than 2.0, default to 0.3) and clicks(positive integer greater than zero, default to 1).

if any input is invalid, the system displays an error message identifying wish field failed and the expected format. The action is not performed.

if the input are valid but the system cannot perform the action, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed.

If all inputs are valid and the action succeeds, the system performs the click at the specified location (or current position if x/y are not provided).

**Constrains**:
- Performance: mouse click must happen under the specified duration paramater (default 0.3)
- Security: the coordinates x, y are checked agains the actual screen size
- Data: `x` optional non-negative integer, `y` optional non-negative integer, `interval` positive number greater than or equal 0.1, `duration` positive number greater than or equal 0.1 and less than 2.0 and `clicks` positive integer greater than 1
- Environment: python 3.10 or higher and pyautogui library must be installed

### 3. Right Click

A user can perform a right-click with the mouse by providing optional x (non-negative integer, default to None), optional y (non-negative integer, default to None), interval (positive number greater than or equal 0.1 and less than 1.0, default to 0.1), duration (positive number greater than or equal 0.1 and less than 2.0, default to 0.3) and clicks (positive integer greater than zero, default to 1).

If any input is invalid, the system displays an error message identifying which field failed and the expected format. The action is not performed.

If the inputs are valid but the system cannot perform the action, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed.

If all inputs are valid and the action succeeds, the system performs the right click operation at the specified location (or current position if x/y are not provided).

**Constraints:**

- **Performance:** mouse right-click must happen under the specified duration parameter (default 0.3 seconds)
- **Security:** the coordinates x, y are checked against the actual screen size; fail-safe enabled by default (pyautogui.FAILSAFE = True) - moving mouse to screen corner aborts automation
- **Data:** `x` optional non-negative integer, `y` optional non-negative integer, `interval` positive number greater than or equal to 0.1 and less than 1.0, `duration` positive number greater than or equal to 0.1 and less than 2.0, `clicks` positive integer greater than zero
- **Environment:** Python 3.10 or higher and pyautogui library must be installed. On Linux, GUI support check required (see https://pyautogui.readthedocs.io for more information)

### 4. Get Mouse Position

A user can retrieve the current mouse cursor coordinates by providing an optional delay (non-negative number, default to 0.0).

The system waits for the specified `delay` duration, allowing the user to move the mouse to the desired target. After the delay expires, the system captures the coordinates.

If `delay` is negative/non-numeric, the system displays an error message identifying which field failed and the expected format. The action is not performed.

If the system cannot access the mouse position after the delay due to a display or permission error, the system displays a message informing the user of a *core action error* and asks them to verify their display environment. The action is not performed.

If all inputs are valid and the operation succeeds, the system returns x_value (non-negative integer), y_value (non-negative integer).

**Constraints:**

- **Performance:** the system must wait exactly for the specified `delay` duration before capturing; total operation time is `delay` + < 0.2 for capture.
- **Security:** fail-safe enabled by default (pyautogui.FAILSAFE = True) moving mouse to screen corner during the delay aborts the wait and raises an exception.
- **Data:** `delay` is a non-negative number (float or int). Default is 0.0. Output `x_value` and `y_value` are non-negative integers.
- **Environment:** Python 3.10 or higher and pyautogui library must be installed. On Linux, GUI support check required (see https://pyautogui.readthedocs.io for more information).

### 6. Scroll

A user can scroll the mouse wheel by providing scroll_amount (integer, default to zero) and optional x (non-negative integer, default to None), optional y (non-negative integer, default to None).

If any input is invalid, the system displays an error message identifying which field failed and the expected format. The action is not performed.

If the inputs are valid but the system cannot perform the action, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed.

If all inputs are valid and the action succeeds, the system performs the scroll operation at the specified location (or current position if x/y are not provided).

**Constraints:**

- **Performance:** scrolling must complete within 2 seconds
- **Security:** the coordinates x, y are checked against the actual screen size; fail-safe enabled by default (pyautogui.FAILSAFE = True) - moving mouse to screen corner aborts automation
- **Data:** scroll_amount required integer non-zero (positive for up/right, negative for down/left), x optional non-negative integer, y optional non-negative integer
- **Environment:** Python 3.10 or higher and pyautogui library must be installed. On Linux, GUI support check required (see https://pyautogui.readthedocs.io for more information)

### 7. Type Text

A user can enter text by providing text (string, non-empty) and optional interval (positive number greater than or equal to 0.16, default to 0.16).

If any input is invalid, the system displays an error message identifying which field failed and the expected format. The action is not performed.

If the inputs are valid but the system cannot perform the action, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed.

If all inputs are valid and the action succeeds, the system types the specified text with the given interval between keystrokes.

**Constraints:**

-   **Performance:** each keystroke must respect the specified interval parameter (default 0.16 seconds); total time is `len(text) * interval`
-   **Security:** fail-safe enabled by default (pyautogui.FAILSAFE = True) - moving mouse to screen corner aborts automation
-   **Data:** `text` required non-empty string, interval positive number greater than or equal to 0.16
-   **Environment:** Python 3.10 or higher and pyautogui library must be installed. On Linux, GUI support check required (see https://pyautogui.readthedocs.io for more information)

---

### 8. Press Key

A user can press a specific key by providing key (string, valid pyautogui key name, default to 'enter'), optional interval (positive number greater than or equal to 0.1, default to 0.1) and optional presses (positive integer greater than zero, default to 1).

If any input is invalid, the system displays an error message identifying which field failed and the expected format. The action is not performed.

If the inputs are valid but the system cannot perform the action, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed.

If all inputs are valid and the action succeeds, the system presses and releases the specified key the requested number of times with the given interval between presses.

**Constraints:**

- **Performance:** each key press must respect the specified interval parameter (default 0.1 seconds); total time is `presses * interval`
- **Security:** fail-safe enabled by default (pyautogui.FAILSAFE = True) - moving mouse to screen corner aborts automation
- **Data:** `key` required non-empty string, must be a valid pyautogui key name (e.g., 'enter', 'tab', 'escape', 'a', 'f1'), default to 'enter', `interval` positive number greater than or equal to 0.1, `presses` positive integer greater than zero, default to 1
- **Environment:** Python 3.10 or higher and pyautogui library must be installed. On Linux, GUI support check required (see https://pyautogui.readthedocs.io for more information)

### 9. Shortcut

A user can perform a keyboard shortcut by providing keys (list of strings, non-empty, valid pyautogui key names).

If any input is invalid, the system displays an error message identifying which field failed and the expected format. The action is not performed.

If the inputs are valid but the system cannot perform the action, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed.

If all inputs are valid and the action succeeds, the system presses all specified keys simultaneously in order and releases them in reverse order.

**Constraints:**

-   **Performance:** shortcut execution must complete within 0.8 seconds
-   **Security:** fail-safe enabled by default (pyautogui.FAILSAFE = True) - moving mouse to screen corner aborts automation
-   **Data:** `keys` required non-empty list of strings, each element must be a valid pyautogui key name, check(https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)
-   **Environment:** Python 3.10 or higher and pyautogui library must be installed. On Linux, GUI support check required (see https://pyautogui.readthedocs.io for more information)

### 10. Locate Image

A user can locate an image on the screen by providing image_path (string, non-empty, valid file path), optional search_time (positive number greater than or equal to 5.0, default to 10.0), optional search_area (tuple of 4 non-negative integers representing left, top, width, height, default to None) and optional confidence (positive float greater than zero and less than or equal to 1.0, default to None).

If any input is invalid, the system displays an error message identifying which field failed and the expected format. The action is not performed.

If the inputs are valid but the system cannot perform the action due to a display or library error, the system displays a message informing the user of a *core action error* and asks them to try again. The action is not performed.

If all inputs are valid and the operation succeeds, but the image is not found within the specified `search_time`, the system returns None.

If all inputs are valid and the image is found, the system returns a Point object containing the center x and y coordinates of the located image.

**Constraints:**

- **Performance:** the system searches for the image for up to `search_time` seconds; if found earlier, it returns immediately.
- **Security:** fail-safe enabled by default (pyautogui.FAILSAFE = True) - moving mouse to screen corner aborts automation; `image_path` is validated to ensure it points to an existing file.
- **Data:** `image_path` required non-empty string pointing to a valid image file, `search_time` positive number >= 5.0, `search_area` optional tuple of 4 non-negative integers (left, top, width, height), `confidence` optional positive float > 0.0 and <= 1.0 (requires OpenCV installed).
- **Environment:** Python 3.10 or higher, pyautogui library must be installed. For `confidence` parameter, opencv-python (cv2) must be installed. On Linux, GUI support check required (see https://pyautogui.readthedocs.io for more information).

| Feature | Reason |
| :--- | :--- |
| Visual Recording / Playback | Screen capture is a diagnostic tool that does not validate input constraints or core action contracts; it belongs in v2 after the execution layer is proven stable and debuggable through logs alone. |