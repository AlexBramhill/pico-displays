import time

from src.display.configs.bases.display_config import DisplayConfig


class DisplayAbstract:
    def __init__(self, config: DisplayConfig):
        """Initialize the display."""
        print(f"Initializing display with config: {config.display_name}")
        print(f"Display type: {config.display_type}")
        print(f"Colour profile: {config.colour_profile}")
        print(f"Image format: {config.image_format}")
        print(f"Maximum update speed: {config.maximum_update_speed_in_ms} ms")
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

    def record_update(self):
        self._last_update_time = time.ticks_ms()

    def is_ready_to_update(self):
        """Check if the display is ready for an update."""
        if self._maximum_update_speed_in_ms is None or self._last_update_time is None:
            return True
        elapsed = time.ticks_diff(time.ticks_ms(), self._last_update_time)
        return elapsed >= self._maximum_update_speed_in_ms

    def get_ms_until_next_update_available(self):
        """Get the time when the display will be ready for the next update."""
        if self._maximum_update_speed_in_ms is None:
            return None

        if self._last_update_time is None:
            return self._maximum_update_speed_in_ms

        time_since_last_update = time.ticks_ms() - self._last_update_time

        return self._maximum_update_speed_in_ms - time_since_last_update

    def get_display_type(self):
        return self._config.display_type

    def get_default_rotation(self):
        """Get the default rotation of the display."""
        return self._config.default_rotation
