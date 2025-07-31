from ..abstract.display_base import DisplayBase
from ..enums import COLOUR_PROFILE, IMAGE_TYPE


class PimoroniDisplay(DisplayBase):

    def __init__(self,
                 max_update_speed_in_ms=0,
                 hard_refresh_every_x_refreshes=None):
        from picographics import (
            PEN_1BIT, PEN_P4, PEN_P8, PEN_RGB332, PEN_RGB565, PEN_RGB888, PicoGraphics, DISPLAY_INKY_PACK
        )
        import jpegdec
        import pngdec

        self.PEN_MAP = {
            COLOUR_PROFILE.ONE_BIT: PEN_1BIT,
            COLOUR_PROFILE.FOUR_BIT_PALETTE: PEN_P4,
            COLOUR_PROFILE.EIGHT_BIT_PALETTE: PEN_P8,
            COLOUR_PROFILE.RGB332: PEN_RGB332,
            COLOUR_PROFILE.RGB565: PEN_RGB565,
            COLOUR_PROFILE.RGB888: PEN_RGB888,
        }

        super().__init__(max_update_speed_in_ms, hard_refresh_every_x_refreshes)
        self._draw_handlers = {
            (IMAGE_TYPE.JPG, COLOUR_PROFILE.ONE_BIT): self._draw_jpg_1bit,
            (IMAGE_TYPE.PNG, COLOUR_PROFILE.ONE_BIT): self._draw_png_1bit,
        }

        self._instance = PicoGraphics(
            DISPLAY_INKY_PACK, self.PEN_MAP[COLOUR_PROFILE.ONE_BIT])
        self._jpegdecInstance = jpegdec.JPEG(self._instance)
        self._pngdecInstance = pngdec.PNG(self._instance)

    def _soft_update(self):
        self._instance.set_update_speed(2)
        self._instance.update()

    def _hard_refresh(self):
        self._instance.set_update_speed(0)
        self._instance.update()

    def _draw_jpg_1bit(self, img_data):
        self._jpegdecInstance.open_RAM(img_data)
        self._jpegdecInstance.decode(0, 0)
        self._instance.update()

    def _draw_png_1bit(self, img_data):
        self._pngdecInstance.open_RAM(img_data)
        self._pngdecInstance.decode(0, 0)
        self._instance.update()
