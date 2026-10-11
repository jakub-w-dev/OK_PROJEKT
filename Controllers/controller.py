from Utility.files import *
from Models.data import *

class Controller:
    @staticmethod
    def load_input_file(path):
        return FileHandler.read_file(path)

    @staticmethod
    def save_generated_input(path):
        return FileHandler.write_to_file(path)

    @staticmethod
    def run_greedy_algorithm(data):
        return data.solve_greedy()