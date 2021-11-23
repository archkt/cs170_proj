import parse
import Task
import numpy as np

np.random.seed(37)

# Set ranges
deadline_range = [1, 1441]
duration_range = [1, 61]
profit_range = [0.001, 99.999]


def generate(n) -> None:
    tasks = []
    deadline = np.random.randint(low=deadline_range[0], high=deadline_range[1], size=n)
    duration = np.random.randint(low=duration_range[0], high=duration_range[1], size=n)
    profit = np.random.uniform(low=profit_range[0], high=profit_range[1], size=n)
    profit[:] = [round(i, 3) for i in profit]

    for i in range(n):
        tasks.append(Task.Task(i+1, deadline[i], duration[i], profit[i]))

    file_name = 'inputs/' + str(n) + '.in'
    parse.write_input_file(file_name, tasks)


generate(100)
generate(150)
generate(200)
