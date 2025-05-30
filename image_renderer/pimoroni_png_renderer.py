import pngdec
from src.display.pimoroni_display import PimoroniDisplay
from src.image_renderer.image_types import IMAGE_TYPE
from src.image_renderer.image_renderer import ImageRendererAbstract


class PimoroniPngRenderer(ImageRendererAbstract):
    def __init__(self, display: PimoroniDisplay):
        self._display = display
        self._pngdecInstance = pngdec.PNG(display.get_pimoroni_display())
        self._initialised = True
        super().__init__(image_type=IMAGE_TYPE.PNG)

    def display_image_from_bytes(self, image_bytes):
        self._pngdecInstance.open_RAM(image_bytes)
        self._pngdecInstance.decode(0, 0)
        self._display.update()
