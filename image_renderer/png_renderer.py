import pngdec
from image_renderer.image_renderer import ImageRendererAbstract


class Png_Renderer(ImageRendererAbstract):
    def __init__(self, display):
        self.display = display
        self._pngdecInstance = pngdec.PNG(display)
        self._initialised = True

    def display_image_from_file(self, path):
        with open(path, "rb") as f:
            self._pngdecInstance.open_RAM(f.read())
            self._pngdecInstance.decode(0, 0)
        self.display.update()

    def display_image_from_bytes(self, image_bytes):
        self._pngdecInstance.open_RAM(image_bytes)
        self._pngdecInstance.decode(0, 0)
        self.display.update()

    def get_required_file_format(self):
        return "png"
