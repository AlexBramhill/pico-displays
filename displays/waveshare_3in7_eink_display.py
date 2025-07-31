from ..abstract.display_base import DisplayBase
from ..enums import COLOUR_PROFILE, IMAGE_TYPE
from ..drivers.waveshare_pico_epaper_3in7 import EPD_3in7


class Waveshare3In7EinkDisplay(DisplayBase):

    def __init__(self, max_update_speed_in_ms=0, hard_refresh_interval=10):
        super().__init__(max_update_speed_in_ms, hard_refresh_interval)
        self._instance = EPD_3in7()

        self._draw_handlers = {
            (IMAGE_TYPE.BMP_RAW, COLOUR_PROFILE.ONE_BIT): self._draw_bmp_1bit,
            (IMAGE_TYPE.BMP_RAW, COLOUR_PROFILE.TWO_BIT): self._draw_bmp_2bit,
        }

    def _hard_refresh(self):
        """Hard refresh - clear display first to remove ghosting."""
        # Clear based on the last used color profile
        # We'll need to track the last color profile used
        if hasattr(self, '_last_color_profile'):
            if self._last_color_profile == COLOUR_PROFILE.ONE_BIT:
                self._clear_1bit()
            elif self._last_color_profile == COLOUR_PROFILE.TWO_BIT:
                self._clear_2bit()

    def _clear_1bit(self):
        self._instance.EPD_3IN7_1Gray_Clear()

    def _clear_2bit(self):
        self._instance.EPD_3IN7_4Gray_Clear()

    def _draw_bmp_1bit(self, img_data):
        self._last_color_profile = COLOUR_PROFILE.ONE_BIT
        if hasattr(self._instance, 'EPD_3IN7_1Gray_Display'):
            self._instance.EPD_3IN7_1Gray_Display(img_data)
            return True
        return False

    def _draw_bmp_2bit(self, img_data):
        self._last_color_profile = COLOUR_PROFILE.TWO_BIT
        if hasattr(self._instance, 'EPD_3IN7_4Gray_Display'):
            self._instance.EPD_3IN7_4Gray_Display(img_data)
            return True
        return False
