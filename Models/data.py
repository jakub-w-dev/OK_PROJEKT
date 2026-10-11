class Data:
    def __init__(self, machines, jobs):
        self.machines = machines
        self.jobs = jobs

    def solve_greedy(self):
        loads = [0] * self.machines
        assignment = [[] for _ in range(self.machines)]
        for job in self.jobs:
            machine = loads.index(min(loads))
            loads[machine] += job
            assignment[machine].append(job)
        return max(loads), assignment