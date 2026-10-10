from random import *

class File_Handler:
    @staticmethod
    def read_file(path):
        i = 0
        jobs = []
        input_file = open(path, 'r')
        for line in input_file:
            if (i > 0):
                jobs.append(int(line))
            else:
                machines = int(line)
            i+=1
        input_file.close()
        return machines, jobs

    @staticmethod
    def write_to_file(path):
        output_file = open(path, 'w')
        output_file.write(Input_Generator.generate_input())
        output_file.close()
        return True

class Input_Generator:
    @staticmethod
    def generate_input():
        machines = randrange(2, 10)
        jobs_count = randrange(machines, 20)
        lines = [str(machines)]
        for _ in range(jobs_count):
            lines.append(str(randrange(1, 40)))
        return '\n'.join(lines)