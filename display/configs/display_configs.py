from picographics import DISPLAY_INKY_PACK, DISPLAY_PICO_DISPLAY_2
from src.display.enums.display_configs import DISPLAY_CONFIG
from src.display.enums.colour_profiles import COLOUR_PROFILE
from src.display.enums.display_types import DISPLAY_TYPE
from src.display.configs.bases.display_config import DisplayConfig
from src.display.configs.bases.pimoroni_config import PimoroniDisplayConfig


def display2_config(image_format: int):
    return DisplayConfig(
        display_name="Pimoroni Pico Display Pack 2.0",
        display_type=DISPLAY_TYPE.PIMORONI,
        colour_profile=COLOUR_PROFILE.EIGHT_BIT_PALETTE,
        image_format=image_format,
        pimoroni_config=PimoroniDisplayConfig(
            display=DISPLAY_PICO_DISPLAY_2,
        )
    )


def inky_config(image_format: int):
    return DisplayConfig(
        display_name="Pimoroni Inky Pack",
        display_type=DISPLAY_TYPE.PIMORONI,
        colour_profile=COLOUR_PROFILE.ONE_BIT,
        image_format=image_format,
        maximum_update_speed_in_ms=15000,
        pimoroni_config=PimoroniDisplayConfig(
            display=DISPLAY_INKY_PACK,
            update_speed=1
        )
    )


def waveshare_3in7_eink_config(image_format: int):
    return DisplayConfig(
        display_name="Waveshare 3.7\" E-Ink",
        display_type=DISPLAY_TYPE.WAVESHARE_3IN7_EINK,
        colour_profile=COLOUR_PROFILE.TWO_BIT,
        image_format=image_format,
        maximum_update_speed_in_ms=15000,
    )


display_configs = {
    DISPLAY_CONFIG.DISPLAY2: display2_config,
    DISPLAY_CONFIG.INKY: inky_config,
    DISPLAY_CONFIG.WAVESHARE_3IN7_EINK: waveshare_3in7_eink_config
}
