
class BaseConverter:
    def __init__(self, celsius,conversion_type):
        self.celsius = celsius
        self.conversion_type = conversion_type

    def convert(self, conversion_type):
        if conversion_type == 0:
            result = self.celsius + 273.15
        elif conversion_type == 1:
            result = (self.celsius * 9 / 5) + 32
        else:
            raise ValueError("Недопустимый тип конвертации")

        return  result
