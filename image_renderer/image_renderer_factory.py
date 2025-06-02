from src.image_renderer.waveshare_3in7_eink_bmp_raw_renderer import Waveshare3In7EinkBmpRawRenderer
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
        print(display.get_display_type())
        print(image_type)
        return ImageRendererFactory._instance
