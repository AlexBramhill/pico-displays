import jpegdec

from image_renderer.image_renderer import ImageRendererAbstract


class Jpeg_Renderer(ImageRendererAbstract):
    def __init__(self, display):
        self.display = display
        self._jpegdecInstance = jpegdec.JPEG(display)
        self._initialised = True

    def display_image_from_file(self, path):
        with open(path, "rb") as f:
            self._jpegdecInstance.open_RAM(f.read())
            self._jpegdecInstance.decode(0, 0)
        self.display.update()

    def display_image_from_bytes(self, image_bytes):
        self._jpegdecInstance.open_RAM(image_bytes)
        self._jpegdecInstance.decode(0, 0)
        self.display.update()

    def get_required_file_format(self):
        return "jpeg"
