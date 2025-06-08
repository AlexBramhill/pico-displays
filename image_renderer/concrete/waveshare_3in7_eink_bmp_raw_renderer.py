from src.enums.colour_profiles import COLOUR_PROFILE
from src.enums.image_types import IMAGE_TYPE
from src.display.concrete.waveshare_3in7_eink_display import Waveshare3In7EinkDisplay
from src.image_renderer.abstract.image_renderer_abstract import ImageRendererAbstract


class Waveshare3In7EinkBmpRawRenderer(ImageRendererAbstract):
    def __init__(self, display: Waveshare3In7EinkDisplay):
        self._display = display
        self._waveshareDisplayInstance = display.get_waveshare_display()
        self._colour_profile = display.get_colour_profile()
        super().__init__(image_type=IMAGE_TYPE.BMP_RAW,
                         colour_profile=display.get_colour_profile())

    def display_image_from_bytes(self, image_bytes):
        self._display.update()
        if (self._colour_profile == COLOUR_PROFILE.ONE_BIT):
            self._waveshareDisplayInstance.EPD_3IN7_1Gray_Display(image_bytes)
        elif (self._colour_profile == COLOUR_PROFILE.TWO_BIT):
            self._waveshareDisplayInstance.EPD_3IN7_4Gray_Display(image_bytes)
