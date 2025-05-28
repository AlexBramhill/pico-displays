
from src.display.configs.bases.pimoroni_config import PimoroniDisplayConfig


class DisplayConfig:
    def __init__(
        self,
        display_name: str,
        display_type: int,
        colour_profile: int,
        image_format: int,
        maximum_update_speed_in_ms: int | None = None,
        pimoroni_config: PimoroniDisplayConfig | None = None
    ):
        self.display_name = display_name
        self.display_type = display_type
        self.colour_profile = colour_profile
        self.image_format = image_format
        self.maximum_update_speed_in_ms = maximum_update_speed_in_ms
        self.pimoroni_config = pimoroni_config
