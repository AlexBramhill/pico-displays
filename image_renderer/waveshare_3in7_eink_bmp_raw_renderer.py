from src.image_renderer.image_types import IMAGE_TYPE
from src.display.waveshare_3in7_eink_display import Waveshare3In7EinkDisplay
from src.image_renderer.image_renderer import ImageRendererAbstract


class Waveshare3In7EinkBmpRawRenderer(ImageRendererAbstract):
    def __init__(self, display: Waveshare3In7EinkDisplay):
        self._display = display
        self._waveshareDisplayInstance = display.get_waveshare_display()
        super().__init__(image_type=IMAGE_TYPE.BMP_RAW)

    def display_image_from_bytes(self, image_bytes):
        self._waveshareDisplayInstance.EPD_3IN7_1Gray_Display_Part(image_bytes)
