from convbinary import BinaryConverter
from convimg import ImageConverter
from utils import FileFinder
import random
import os


class SetupMain:
    def __init__(self, img_path, bin_file_path, ascii_file_path):
        self.img_path = img_path
        self.bin_file_path = bin_file_path
        self.ascii_file_path = ascii_file_path
        self.PWFilePath = "finalPW"
        self.startIndexPW = 0

    # get user Length
    def get_user_number(self):
        while True:
            try:
                user_input = int(
                    input("enter a length valid range (1-256): "))
                if 1 <= user_input <= 256:
                    return user_input
                else:
                    print(
                        "not within the valid range (1-256). again.")
            except ValueError:
                print("Invalid input. Need integer.")

    # convert img -> binary -> ascii
    def convert_image_to_password(self):
        converterIMGtoBin = ImageConverter()
        converterBintoPW = BinaryConverter(
            self.bin_file_path, self.ascii_file_path)

        binary_data = converterIMGtoBin.img_to_binary(self.img_path)
        converterIMGtoBin.write_to_file(binary_data, self.bin_file_path)
        print("\nFinished Converting to Binary\n")

        converterBintoPW.process_ascii_file()
        converterBintoPW.write_ascii_to_file()
        print("\nFinished Converting to ASCII\n")

    # get charcount from ascii file
    def analyze_text_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                char_count = 0
                for line in file:
                    char_count += len(line)
            return int(char_count)
        except FileNotFoundError:
            print("\nERROR FILE CHAR COUNT!\n")

    # Find lost pw for example
    def find_password(self):
        start_index = int(input("Enter the start index: "))
        length = int(input("length of the password: "))

        # Lesen des Passworts aus der Datei
        with open(self.ascii_file_path, 'r') as file:
            file.seek(start_index)
            password = file.read(length)

        print("Password:", password)

    # main loop creating finding
    def printPWLOOP(self):
        while True:
            action = input(
                "Create a PW or Find PW? (create/find): ").lower()

            if action == 'create':
                self.lengthPW = self.get_user_number()

                self.convert_image_to_password()

                # random start point
                max_start_index = self.analyze_text_file(
                    self.ascii_file_path) - self.lengthPW
                self.startIndexPW = random.randint(0, max_start_index)

                # Read Pw from ascii
                with open(self.ascii_file_path, 'r') as file:
                    file.seek(self.startIndexPW)
                    password = file.read(self.lengthPW)

                # Write in final
                filename = "PW"
                count = 0
                while os.path.exists(f"{self.PWFilePath}/{filename}{count}.txt"):
                    count += 1
                final_file_path = f"{self.PWFilePath}/{filename}{count}.txt"

                with open(final_file_path, 'w') as file:
                    file.write(f"Password: {password}\nStart Index: {
                        self.startIndexPW}\nLength: {self.lengthPW}\n")

                print("Generated Password:", password)
                print("Start Index:", self.startIndexPW)
            elif action == 'find':
                self.find_password()
            else:
                print("Invalid choice. 'create' or 'find'.")

            # Again?
            choice = input("perform another action? (yes/no): ")
            if choice.lower() != 'yes':
                break
