from Utility.files import *

class Controller:
    @staticmethod
    def file_input(path):
        return File_Handler.read_file(path)

    @staticmethod
    def file_output(path):
        return File_Handler.write_to_file(path)