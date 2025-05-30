import jpegdec
from src.display.pimoroni_display import PimoroniDisplay
from src.image_renderer.image_types import IMAGE_TYPE
from src.image_renderer.image_renderer import ImageRendererAbstract


class PimoroniJpegRenderer(ImageRendererAbstract):
    def __init__(self, display: PimoroniDisplay):
        self._display = display
        self._jpegdecInstance = jpegdec.JPEG(display.get_pimoroni_display())
        self._initialised = True
        super().__init__(image_type=IMAGE_TYPE.JPG)
        
    def display_image_from_bytes(self, image_bytes):
        self._jpegdecInstance.open_RAM(image_bytes)
        self._jpegdecInstance.decode(0, 0)
        self._display.update()
