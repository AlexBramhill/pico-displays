from src.enums.colour_profiles import COLOUR_PROFILE
from src.display.configs.bases.display_config import DisplayConfig
from src.display.abstract.display_abstract import DisplayAbstract
from src.display.drivers.waveshare_pico_epaper_3in7 import EPD_3in7


class Waveshare3In7EinkDisplay(DisplayAbstract): \

    def __init__(self, config: DisplayConfig):
        super().__init__(config)
        self._config = config
        self._instance = EPD_3in7()
        self._instance.EPD_3IN7_4Gray_init()
        self._update_count = 0
        self._hard_refresh_every = 10

    def get_bounds(self):
        return (self._instance.width, self._instance.height)

    def update(self):
        super().record_update()
        (should_long_refresh) = self.handle_update_count_and_get_should_long_refresh()
        if ((should_long_refresh)):
            self._long_refresh()

    def handle_update_count_and_get_should_long_refresh(self):
        if (self._update_count >= self._hard_refresh_every):
            self._long_refresh()
            self._update_count = 0
            return True
        self._update_count += 1
        return False

    def get_waveshare_display(self):
        return self._instance

    def get_display_type(self):
        return self._config.display_type

    # Completely untested
    # And should definitely be separated out into two classes
    def _long_refresh(self):
        if (self._config.colour_profile == COLOUR_PROFILE.ONE_BIT):
            self._instance.EPD_3IN7_1Gray_Clear()
        elif (self._config.colour_profile == COLOUR_PROFILE.TWO_BIT):
            self._instance.EPD_3IN7_4Gray_Clear()
        self._instance.ReadBusy()
