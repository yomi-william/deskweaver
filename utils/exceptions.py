"""Custom exceptions for the framework.

This module defines custom exception classes used across the framework to
handle specific error conditions related to actions and coordinates.

Classes:
    DeskWeaverError: Base exception for all Deskweaver framework errors.
    CoreActionError: Base exception for core action failures.
    CoordinateOutOfBoundsError: Raised when a coordinate exceeds valid bounds.
    OutOfRangeError: Raised when a value is out of the expected range.
    InvalidKeyError: Raised when an invalid pyautogui key is provided for a keyboard action.
    InvalidPathError: Raised when the file path provided does not exist or is invalid.
    InvalidSearchAreaError: Raised when search_area is not a tuple of 4 non-negative integers.
    FailSafeTriggeredError: Raised when the pyautogui failsafe is triggered.
"""

class DeskWeaverError(Exception):
    """Base exception for all Deskweaver framework errors."""
    def __init__(self, message="A Deskweaver framework error occurred."):
        self.message = message
        super().__init__(self.message)

class CoreActionError(DeskWeaverError, RuntimeError):
    """Raised when a core action fails to execute properly."""
    def __init__(self, message: str = "core action failed to execute properly, please check the logs for more details."):
        super().__init__(message)

class CoordinateOutOfBoundsError(DeskWeaverError, ValueError):
    """Raised when a coordinate exceeds the valid screen boundaries."""
    def __init__(self, x, y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.message = f"Coordinates ({x}, {y}) are out of bounds for screen size {screen_width}x{screen_height}"
        super().__init__(self.message)

class OutOfRangeError(DeskWeaverError, ValueError):
    """Raised when a value is out of the expected range."""
    def __init__(self, value, min_value, max_value):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.message = f"Value {value} is out of range. Expected between {min_value} and {max_value}."
        super().__init__(self.message)

class InvalidKeyError(DeskWeaverError, ValueError):
    """Raised when an invalid pyautogui key is provided for a keyboard action."""
    def __init__(self, key):
        self.key = key
        self.message = f"Invalid pyautogui key: '{key}'. Please refer to the pyautogui documentation for valid keys."
        super().__init__(self.message)

class InvalidSearchAreaError(DeskWeaverError, ValueError):
    """Raised when search_area is not a tuple of 4 non-negative integers."""
    def __init__(self, search_area):
        self.search_area = search_area
        self.message = f"Invalid search area: {search_area}. Expected a tuple of 4 non-negative integers."
        super().__init__(self.message)

class InvalidPathError(DeskWeaverError, ValueError):
    """Raised when the file path provided does not exist or is invalid."""
    def __init__(self, path):
        self.path = path
        self.message = f"Invalid file path: '{path}'. Please ensure the path exists and is accessible."
        super().__init__(self.message)

class FailSafeTriggeredError(CoreActionError):
    """Raised when the pyautogui fail-safe is triggered by the user moving the mouse."""
    def __init__(self):
        self.message = "Fail-safe triggered! The automation was aborted because the mouse was moved to a screen corner."
        super().__init__(self.message)