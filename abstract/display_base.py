import time


class DisplayBase:
    def __init__(self, max_update_speed_in_ms=0, hard_refresh_interval=None):
        self._max_update_speed_in_ms = max_update_speed_in_ms
        self._next_valid_update_time = 0
        self._draw_handlers = {}
        self._hard_refresh_interval = hard_refresh_interval
        self._renders_until_next_hard_refresh = hard_refresh_interval

    def draw_image(self, img_data, img_format, color_profile, *args, **kwargs):
        if not self._is_ready_for_update():
            return False

        if self._hard_refresh_interval is not None:
            self._handle_hard_refresh_cycle()

        handler = self._get_draw_handler(img_format, color_profile)
        handler(img_data, *args, **kwargs)

        self._update_next_valid_update_time()
        return True

    def _handle_hard_refresh_cycle(self):
        self._renders_until_next_hard_refresh -= 1  # type: ignore
        if self._renders_until_next_hard_refresh <= 0:
            self._hard_refresh()
            self._reset_refresh_counters()

    def _get_draw_handler(self, img_format, color_profile):
        try:
            return self._draw_handlers[(img_format, color_profile)]
        except KeyError:
            raise ValueError(
                f"Unsupported combination: {img_format} with {color_profile}")

    def _is_ready_for_update(self):
        return self._max_update_speed_in_ms == 0 or time.ticks_ms() >= self._next_valid_update_time

    def _update_next_valid_update_time(self):
        if self._max_update_speed_in_ms > 0:
            self._next_valid_update_time = time.ticks_ms() + self._max_update_speed_in_ms

    def _hard_refresh(self):
        raise NotImplementedError(
            "_hard_refresh must be implemented in subclass")

    def _reset_refresh_counters(self):
        self._renders_until_next_hard_refresh = self._hard_refresh_interval

    @property
    def supported_combinations(self):
        return list(self._draw_handlers.keys())

    @property
    def renders_until_next_hard_refresh(self):
        return self._renders_until_next_hard_refresh
