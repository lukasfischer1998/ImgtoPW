

class HashSha256:
    def __init__(self) -> None:
        self.BinArray = []

    def getBinValues(self, PathBin):
        try:
            with open(PathBin, 'r') as file:
                for line in file:
                    self.BinArray.append(line.strip())  #strip \n
        except Exception as e:
            print(f"error occurred writing to file: {str(e)}")

    def explicit_or(num1, num2):
        result = ""
        for bit1, bit2 in zip(num1, num2):
            if bit1 != bit2:
                result += "1"
            else:
                result += "0"
        return result

    def logical_and(num1, num2):
        result = ""
        for bit1, bit2 in zip(num1, num2):
            if bit1 == "1" and bit2 == "1":
                result += "1"
            else:
                result += "0"
        return result

    def bitwise_not(num):
        result = ""
        for bit in num:
            if bit == "0":
                result += "1"
            else:
                result += "0"
        return result

    def shift_left(num, n):
        return num << n

    def shift_right(num, n):
        return num >> n

    def rotate(value, rotations, width=32):
        rotations %= width
        rotated_left = (value << rotations) | (value >> (width - rotations))
        mask = (1 << width) - 1
        result = rotated_left & mask
        return result


sha256 = HashSha256()
sha256.getBinValues(
    r"C:\Users\lukif\Desktop\PWImage\src\TempSafe\binaryval.txt")

print(sha256.BinArray)
