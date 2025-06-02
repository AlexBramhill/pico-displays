from src.display.configs.display_configs import DISPLAY_TYPE
from src.display.configs.bases.display_config import DisplayConfig
from src.display.abstract.display_abstract import DisplayAbstract
from src.display.concrete.pimoroni_display import PimoroniDisplay
from src.display.concrete.waveshare_3in7_eink_display import Waveshare3In7EinkDisplay

# Worth considering moving these imports in the if block below
# to see if we can get away with not being tied to firmware specific imports


class DisplayFactory:
    _instantiated = False

    @staticmethod
    def create(config: DisplayConfig) -> DisplayAbstract:
        print(f"Creating display with config: {config.display_name}")
        if DisplayFactory._instantiated is True:
            raise RuntimeError(
                "Multiple instances of Display are not allowed. Please use the same instance.")

        DisplayFactory._instantiated = True

        if (config.display_type == DISPLAY_TYPE.PIMORONI):
            return PimoroniDisplay(config)

        if (config.display_type == DISPLAY_TYPE.WAVESHARE_3IN7_EINK):
            return Waveshare3In7EinkDisplay(config)

        raise NotImplementedError(
            f"Display type {config.display_name} is not implemented in the factory."
        )
