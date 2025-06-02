from src.enums.image_types import IMAGE_TYPE
from src.display.configs.bases.pimoroni_config import PimoroniDisplayConfig
from src.enums.colour_profiles import COLOUR_PROFILE


class DisplayConfig:
    def __init__(
        self,
        display_name: str,
        display_type: int,
        colour_profile: int | None,
        supported_colour_profiles: list[int],
        image_format: int | None,
        supported_image_formats: list[int],
        maximum_update_speed_in_ms: int | None = None,
        pimoroni_config: PimoroniDisplayConfig | None = None
    ):

        colour_profile_to_use = colour_profile or supported_colour_profiles[0]

        if colour_profile_to_use not in supported_colour_profiles:
            raise ValueError(
                f"Colour profile {COLOUR_PROFILE.name_from_value(colour_profile_to_use)} is not in the list of supported colour profiles for {display_name} "
                f"[{', '.join(COLOUR_PROFILE.name_from_value(cp) for cp in supported_colour_profiles)}]"
            )

        image_format_to_use = image_format or supported_image_formats[0]

        if image_format_to_use not in supported_image_formats:
            raise ValueError(
                f"Image format {IMAGE_TYPE.name_from_value(image_format_to_use)} is not in the list of supported image formats for {display_name} "
                f"[{', '.join(IMAGE_TYPE.name_from_value(cp) for cp in supported_image_formats)}]"
            )

        self.display_name = display_name
        self.display_type = display_type
        self.colour_profile = colour_profile
        self.image_format = image_format_to_use
        self.maximum_update_speed_in_ms = maximum_update_speed_in_ms
        self.pimoroni_config = pimoroni_config
