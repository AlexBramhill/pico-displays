from src.display.configs.display_configs import DISPLAY_TYPE
from src.display.configs.bases.display_config import DisplayConfig
from src.display.display import DisplayAbstract
from src.display.pimoroni_display import PimoroniDisplay


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

        raise NotImplementedError(
            f"Display type {config.display_name} is not implemented in the factory."
        )
