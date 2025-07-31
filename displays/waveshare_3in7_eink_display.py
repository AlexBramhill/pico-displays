from ..abstract.display_base import DisplayBase
from ..enums import COLOUR_PROFILE, IMAGE_TYPE


class Waveshare3In7EinkDisplay(DisplayBase):

    def __init__(self, max_update_speed_in_ms=0, hard_refresh_interval=10):
        # Import the driver only when the class is initialized
        from ..drivers.waveshare_pico_epaper_3in7 import EPD_3in7

        super().__init__(max_update_speed_in_ms, hard_refresh_interval)
        self._instance = EPD_3in7()

        self._draw_handlers = {
            (IMAGE_TYPE.BMP_RAW, COLOUR_PROFILE.ONE_BIT): self._draw_bmp_1bit,
            (IMAGE_TYPE.BMP_RAW, COLOUR_PROFILE.TWO_BIT): self._draw_bmp_2bit,
        }

    def _hard_refresh(self):
        if not hasattr(self, '_last_color_profile'):
            return

        if self._last_color_profile == COLOUR_PROFILE.ONE_BIT:
            self._hard_refresh_1bit()
        elif self._last_color_profile == COLOUR_PROFILE.TWO_BIT:
            self._hard_refresh_2bit()

    def _hard_refresh_1bit(self):
        self._instance.EPD_3IN7_1Gray_Clear()

    def _hard_refresh_2bit(self):
        self._instance.EPD_3IN7_4Gray_Clear()

    def _draw_bmp_1bit(self, img_data):
        self._last_color_profile = COLOUR_PROFILE.ONE_BIT
        self._instance.EPD_3IN7_1Gray_Display(img_data)
        return True

    def _draw_bmp_2bit(self, img_data):
        self._last_color_profile = COLOUR_PROFILE.TWO_BIT
        self._instance.EPD_3IN7_4Gray_Display(img_data)
        return True
