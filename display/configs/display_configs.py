from picographics import DISPLAY_INKY_PACK, DISPLAY_PICO_DISPLAY_2
from src.enums.image_types import IMAGE_TYPE
from src.enums.display_configs import DISPLAY_CONFIG
from src.enums.colour_profiles import COLOUR_PROFILE
from src.enums.display_types import DISPLAY_TYPE
from src.display.configs.bases.display_config import DisplayConfig
from src.display.configs.bases.pimoroni_config import PimoroniDisplayConfig


def display2_config(image_format: int | None = None):
    return DisplayConfig(
        display_name="Pimoroni Pico Display Pack 2.0",
        display_type=DISPLAY_TYPE.PIMORONI,
        colour_profile=COLOUR_PROFILE.EIGHT_BIT_PALETTE,
        supported_colour_profiles=[
            COLOUR_PROFILE.EIGHT_BIT_PALETTE
        ],
        image_format=image_format,
        supported_image_formats=[
            IMAGE_TYPE.PNG,
            IMAGE_TYPE.JPG,
        ],
        pimoroni_config=PimoroniDisplayConfig(
            display=DISPLAY_PICO_DISPLAY_2,
        )
    )


def inky_config(image_format: int | None = None):
    return DisplayConfig(
        display_name="Pimoroni Inky Pack",
        display_type=DISPLAY_TYPE.PIMORONI,
        colour_profile=COLOUR_PROFILE.ONE_BIT,
        supported_colour_profiles=[
            COLOUR_PROFILE.ONE_BIT
        ],
        image_format=image_format,
        supported_image_formats=[
            IMAGE_TYPE.PNG,
            IMAGE_TYPE.JPG,
        ],
        maximum_update_speed_in_ms=60000,
        pimoroni_config=PimoroniDisplayConfig(
            display=DISPLAY_INKY_PACK,
            update_speed=1
        )
    )


def waveshare_3in7_eink_config(image_format: int | None = None):
    return DisplayConfig(
        display_name="Waveshare 3.7\" E-Ink",
        display_type=DISPLAY_TYPE.WAVESHARE_3IN7_EINK,
        colour_profile=COLOUR_PROFILE.TWO_BIT,
        supported_colour_profiles=[
            COLOUR_PROFILE.TWO_BIT,
            COLOUR_PROFILE.ONE_BIT
        ],
        image_format=image_format,
        supported_image_formats=[
            IMAGE_TYPE.BMP_RAW
        ],
        maximum_update_speed_in_ms=60000,
        default_rotation=90
    )


display_configs = {
    DISPLAY_CONFIG.DISPLAY2: display2_config,
    DISPLAY_CONFIG.INKY: inky_config,
    DISPLAY_CONFIG.WAVESHARE_3IN7_EINK: waveshare_3in7_eink_config
}
