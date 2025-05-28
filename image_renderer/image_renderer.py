class ImageRendererAbstract:

    def __init__(self, image_type: int):
        self.image_type = image_type

    def display_image_from_file(self, path):
        raise NotImplementedError("Subclasses should implement this!")

    def display_image_from_bytes(self, image_bytes):
        raise NotImplementedError("Subclasses should implement this!")

    def get_image_type(self):
        return self.image_type
