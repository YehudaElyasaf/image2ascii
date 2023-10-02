class AsciiCell:
    def __init__(self, char, r, g, b):
        self.char = char
        self.r = r
        self.g = g
        self.b = b

        def __str__(self):
            return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, char)
