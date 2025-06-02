class NameFromValueMixin:
    @classmethod
    def name_from_value(cls, value):
        for name, val in vars(cls).items():
            if val == value:
                return name
            raise ValueError(
                f"No attribute found with value {value} in class {cls.__name__}")

    @classmethod
    def safe_name_from_value(cls, value):
        try:
            return cls.name_from_value(value)
        except ValueError:
            return str(value)
