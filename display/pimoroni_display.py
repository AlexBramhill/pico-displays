from picographics import PEN_1BIT, PEN_P4, PEN_P8, PEN_RGB332, PEN_RGB565, PEN_RGB888, PicoGraphics
from src.image_renderer.image_renderer_factory import ImageRendererFactory
from src.display.colour_profiles import COLOUR_PROFILE
from src.display.configs.bases.display_config import DisplayConfig
from src.display.configs.bases.pimoroni_config import PimoroniDisplayConfig
from src.display.display import DisplayAbstract


class PimoroniDisplay(DisplayAbstract):
    def __init__(self, config: DisplayConfig):
        self._validate_config(config)

        self._config = config

        self._pimoroni_config: PimoroniDisplayConfig = config.pimoroni_config  # type: ignore

        self._instance = PicoGraphics(
            self._pimoroni_config.display, self._get_pen_type())

        self._configure_update_speed()

        super().__init__(config)

    def _validate_config(self, config: DisplayConfig):
        """Validate the configuration for the display."""
        if config.pimoroni_config is None:
            raise ValueError(
                "PimoroniDisplay requires a PimoroniDisplayConfig")

    def _configure_update_speed(self):
        """Configure the update speed of the display."""
        if self._pimoroni_config.update_speed is None:
            return

        self._instance.set_update_speed(
            self._pimoroni_config.update_speed)  # type: ignore

    def get_bounds(self):
        return self._instance.get_bounds()

    def update(self):
        super().record_update()
        return self._instance.update()

    def ready_to_update(self):
        return super().ready_to_update()

    def get_pimoroni_display(self):
        return self._instance

    def _get_pen_type(self) -> int:
        if self._config.colour_profile == COLOUR_PROFILE.ONE_BIT:
            return PEN_1BIT
        elif self._config.colour_profile == COLOUR_PROFILE.FOUR_BIT_PALETTE:
            return PEN_P4
        elif self._config.colour_profile == COLOUR_PROFILE.EIGHT_BIT_PALETTE:
            return PEN_P8
        elif self._config.colour_profile == COLOUR_PROFILE.RGB332:
            return PEN_RGB332
        elif self._config.colour_profile == COLOUR_PROFILE.RGB565:
            return PEN_RGB565
        elif self._config.colour_profile == COLOUR_PROFILE.RGB888:
            return PEN_RGB888
        raise ValueError(
            f"Unsupported colour profile: {self._config.colour_profile}")
