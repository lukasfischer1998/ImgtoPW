if __name__ == "__main__":
    from setup import SetupMain
    from utils import FileFinder

    # IF NOT NEEDED DONT CHANGE
    bin_file_path = 'src\\TempSafe\\binaryval.txt'
    ascii_file_path = 'src\\TempSafe\\asciival.txt'

    img_dir = 'img'
    file_finder = FileFinder(img_dir)
    files_in_directory = file_finder.find_files_in_directory()
    img_path = file_finder.select_file_path(files_in_directory)

    setup_instance = SetupMain(img_path, bin_file_path, ascii_file_path)
    setup_instance.printPWLOOP()
