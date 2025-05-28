from src.display.configs.display_configs import DISPLAY_TYPE
from src.image_renderer.pimoroni_jpeg_renderer import PimoroniJpegRenderer
from src.image_renderer.pimoroni_png_renderer import PimoroniPngRenderer
from src.display.display import DisplayAbstract
from src.image_renderer.image_types import IMAGE_TYPE


class ImageRendererFactory:
    @staticmethod
    def create_renderer(display: DisplayAbstract, image_type: int):
        if display.get_display_type() == DISPLAY_TYPE.PIMORONI:
            if image_type == IMAGE_TYPE.PNG:
                ImageRendererFactory._instance = PimoroniPngRenderer(
                    display)  # type: ignore
            elif image_type == IMAGE_TYPE.JPG:
                ImageRendererFactory._instance = PimoroniJpegRenderer(
                    display)  # type: ignore
        else:
            raise NotImplementedError(
                f"Renderer type {image_type} is not implemented.")

        return ImageRendererFactory._instance
