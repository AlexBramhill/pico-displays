from src.image_renderer.abstract.image_renderer_abstract import ImageRendererAbstract
from src.image_renderer.concrete.waveshare_3in7_eink_bmp_raw_renderer import Waveshare3In7EinkBmpRawRenderer
from src.enums.display_types import DISPLAY_TYPE
from src.image_renderer.concrete.pimoroni_jpeg_renderer import PimoroniJpegRenderer
from src.image_renderer.concrete.pimoroni_png_renderer import PimoroniPngRenderer
from src.display.abstract.display_abstract import DisplayAbstract
from src.enums.image_types import IMAGE_TYPE


class ImageRendererFactory:
    @staticmethod
    def create_renderer(display: DisplayAbstract, image_type: int | None = None) -> ImageRendererAbstract:
        if display.get_display_type() == DISPLAY_TYPE.PIMORONI:
            if image_type == IMAGE_TYPE.PNG:
                ImageRendererFactory._instance = PimoroniPngRenderer(
                    display)  # type: ignore
            elif image_type == IMAGE_TYPE.JPG:
                ImageRendererFactory._instance = PimoroniJpegRenderer(
                    display)  # type: ignore
            else:
                raise NotImplementedError(
                    f"Renderer type {display.get_display_type()} is not implemented for Pimoroni display.")

        elif display.get_display_type() == DISPLAY_TYPE.WAVESHARE_3IN7_EINK:
            if image_type == IMAGE_TYPE.BMP_RAW:
                ImageRendererFactory._instance = Waveshare3In7EinkBmpRawRenderer(
                    display)  # type: ignore
            else:
                raise NotImplementedError(
                    f"Renderer type {display.get_display_type()} is not implemented for Waveshare 3.7 E-Ink display.")
        else:
            raise NotImplementedError(
                f"Display type {display.get_display_type()} is not supported for image rendering.")

        return ImageRendererFactory._instance
