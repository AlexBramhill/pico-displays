import pngdec
from src.display.concrete.pimoroni_display import PimoroniDisplay
from src.enums.image_types import IMAGE_TYPE
from src.image_renderer.abstract.image_renderer_abstract import ImageRendererAbstract


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
