from src.display.configs.bases.display_config import DisplayConfig
from src.display.display import DisplayAbstract
from src.display.drivers.waveshare_pico_epaper_3in7 import EPD_3in7


class Waveshare3In7EinkDisplay(DisplayAbstract):
    def __init__(self, config: DisplayConfig):
        super().__init__(config)
        self._instance = EPD_3in7()
        self._instance.EPD_3IN7_4Gray_init()

    def get_bounds(self):
        return (self._instance.width, self._instance.height)

    def update(self):
        super().record_update()
        self._instance.EPD_3IN7_4Gray_Display(self._instance.buffer_4Gray)
        self.record_update()

    def get_waveshare_display(self):
        return self._instance
    
    def get_display_type(self):
        return self._config.display_type
    
    
