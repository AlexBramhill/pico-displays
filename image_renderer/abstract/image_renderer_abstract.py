class ImageRendererAbstract:

    def __init__(self, image_type: int, colour_profile: int):
        self._image_type = image_type
        self._colour_profile = colour_profile

    def display_image_from_bytes(self, image_bytes):
        raise NotImplementedError("Subclasses should implement this!")

    def get_image_type(self):
        return self._image_type

    def get_colour_profile(self):
        return self._colour_profile
