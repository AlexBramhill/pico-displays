class ImageRendererAbstract:

    def __init__(self, display):
        raise NotImplementedError("Subclasses should implement this!")

    def display_image_from_file(self, path):
        raise NotImplementedError("Subclasses should implement this!")

    def display_image_from_bytes(self, image_bytes):
        raise NotImplementedError("Subclasses should implement this!")

    def get_required_file_format(self):
        raise NotImplementedError("Subclasses should implement this!")
