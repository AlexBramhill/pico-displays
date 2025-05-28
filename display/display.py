import time

from src.display.configs.bases.display_config import DisplayConfig


class DisplayAbstract:
    def __init__(self, config: DisplayConfig):
        """Initialize the display."""
        self._config = config
        self._maximum_update_speed_in_ms = config.maximum_update_speed_in_ms
        self._last_update_time = None
        if type(self) is DisplayAbstract:
            raise NotImplementedError(
                "This method should be overridden by subclasses.")

    def get_bounds(self):
        """Get the dimensions of the display."""
        raise NotImplementedError(
            "This method should be overridden by subclasses.")

    def update(self):
        """Update the display."""
        raise NotImplementedError(
            "This method should be overridden by subclasses.")

    def render_image(self, image):
        """Render an image on the display."""
        raise NotImplementedError(
            "This method should be overridden by subclasses.")

    def update_with_image_from_bytes(self, image_bytes):
        """Update the display with an image from bytes."""
        raise NotImplementedError(
            "This method should be overridden by subclasses.")

    def update_with_image_from_file(self, path):
        """Update the display with an image from a file."""
        raise NotImplementedError(
            "This method should be overridden by subclasses.")

    def record_update(self):
        self._last_update_time = time.ticks_ms()

    def ready_to_update(self):
        """Check if the display is ready for an update."""
        if self._maximum_update_speed_in_ms is None or self._last_update_time is None:
            return True
        elapsed = time.ticks_diff(time.ticks_ms(), self._last_update_time)
        return elapsed >= self._maximum_update_speed_in_ms

    def get_display_type(self):
        return self._config.display_type
