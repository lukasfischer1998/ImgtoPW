class BinaryConverter:
    def __init__(self, BinValTextPath, asciiValTextPath) -> None:
        self.PWArray = []
        self.BinValTextPath = BinValTextPath
        self.AsciiValTextPath = asciiValTextPath

    def binary_to_decimal(self, binary_string):
        # Convert binary string -> decimal
        decimal_value = 0
        for i, bit in enumerate(reversed(binary_string)):
            decimal_value += int(bit) * (2 ** i)
        return decimal_value

    def read_binary_values(self):
        # Read binary values from file
        binary_values = []
        try:
            with open(self.BinValTextPath, 'r') as file:
                for line in file:
                    binary_values.extend(line.strip().split())
        except FileNotFoundError:
            print(f"Error: File '{self.BinValTextPath}' not found.")
        except Exception as e:
            print(f"error occurred: {str(e)}")
        return binary_values

    def convert_binary_to_ascii(self, binary_values):
        # Convert binary values to ASCII characters
        ascii_text = ""
        for binary_value in binary_values:
            decimal_value = self.binary_to_decimal(binary_value)
            # Überprüfe, ob das Dezimalergebnis ein gültiges ASCII-Zeichen ist und kein Steuerzeichen
            if 32 < decimal_value < 127:
                ascii_text += chr(decimal_value)
        return ascii_text

    def process_ascii_file(self):
        # Read binary values, convert to ASCII, and append to PWArray
        binary_values = self.read_binary_values()
        ascii_text = self.convert_binary_to_ascii(binary_values)
        self.PWArray.append(ascii_text)

    def write_ascii_to_file(self):
        # Write ASCII values to the specified text file
        try:
            with open(self.AsciiValTextPath, 'w') as file:
                for item in self.PWArray:
                    file.write("%s\n" % item)
            print(f"wrote ASCII values to {
                  self.AsciiValTextPath}")
        except Exception as e:
            print(f"error occurred writing to file: {str(e)}")
