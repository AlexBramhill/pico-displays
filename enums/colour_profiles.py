from src.helpers.name_from_value_mixin import NameFromValueMixin


class COLOUR_PROFILE(NameFromValueMixin):
    ONE_BIT = 1
    TWO_BIT = 2
    FOUR_BIT_PALETTE = 4
    EIGHT_BIT_PALETTE = 8
    RGB332 = 322
    RGB565 = 565
    RGB888 = 888
