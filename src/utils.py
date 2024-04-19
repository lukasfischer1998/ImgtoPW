import os


class FileFinder:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def find_files_in_directory(self):
        if not os.path.exists(self.folder_path):
            print(f"Folder '{self.folder_path}' does not exist.")
            return []

        files_in_directory = [f for f in os.listdir(
            self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        return files_in_directory

    def select_file_path(self, files_in_directory):
        if not files_in_directory:
            print("No files found in the directory.")
            return None

        if len(files_in_directory) == 1:
            print(f"Found file: {files_in_directory[0]}")
            return os.path.join(self.folder_path, files_in_directory[0])

        print("Multiple files found in the directory:")
        for idx, file_name in enumerate(files_in_directory):
            print(f"{idx + 1}: {file_name}")

        while True:
            try:
                choice = int(
                    input("Enter the number of the file you want to select: "))
                if 1 <= choice <= len(files_in_directory):
                    selected_file = files_in_directory[choice - 1]
                    return os.path.join(self.folder_path, selected_file)
                else:
                    print("Invalid choice. Please enter a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Beispielaufruf der Klasse
folder_path = "example_folder"
file_finder = FileFinder(folder_path)
files_in_directory = file_finder.find_files_in_directory()
selected_file_path = file_finder.select_file_path(files_in_directory)
if selected_file_path:
    print(f"Selected file: {selected_file_path}")
