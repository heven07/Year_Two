def bankers_algorithm(num_processes, num_resources, available, max_demand, allocation):
    available_copy = available.copy()
    completion = [False] * num_processes
    safe_sequence = []
    while not all(completion):
        for i in range(num_processes):
            if completion[i]:
                continue
            can_complete = True
            for j in range(num_resources):
                if max_demand[i][j] - allocation[i][j] > available_copy[j]:
                    can_complete = False
                    break
            if can_complete:
                completion[i] = True
                safe_sequence.append(i)
                for j in range(num_resources):
                    available_copy[j] += allocation[i][j]
    return safe_sequence

num_processes = 5
num_resources = 3
available = [3, 3, 2]
max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

safe_sequence = bankers_algorithm(num_processes, num_resources, available, max_demand, allocation)
print(safe_sequence)