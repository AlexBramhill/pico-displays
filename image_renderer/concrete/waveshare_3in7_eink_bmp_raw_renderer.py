from src.enums.image_types import IMAGE_TYPE
from src.display.concrete.waveshare_3in7_eink_display import Waveshare3In7EinkDisplay
from src.image_renderer.abstract.image_renderer_abstract import ImageRendererAbstract


class Waveshare3In7EinkBmpRawRenderer(ImageRendererAbstract):
    def __init__(self, display: Waveshare3In7EinkDisplay):
        self._display = display
        self._waveshareDisplayInstance = display.get_waveshare_display()
        super().__init__(image_type=IMAGE_TYPE.BMP_RAW)

    def display_image_from_bytes(self, image_bytes):
        self._display.update()
        self._waveshareDisplayInstance.EPD_3IN7_1Gray_Display(image_bytes)
