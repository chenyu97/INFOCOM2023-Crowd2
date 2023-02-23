# Attention! All the indices count from 1.

import csv
import random
import math
import InitializeSettings


#  Read settings
number_of_workers_list = [3,5,7,9,11]
result_file_path = '../0-FigureDraw/scalability_worker_UCI.csv'
result_file = open(result_file_path, 'w', newline='')
csv_writer = csv.writer(result_file)
csv_writer.writerow(['number_of_workers', 'time_average_social_welfare'])

for index in range(len(number_of_workers_list)):
    number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, task_computation_demand, \
    performance_of_worker, task_computation_capacity, fluctuate_range = InitializeSettings.read_settings('setting_file', index)


    # Used to calculate the optimal social welfare, then the regret
    def get_optimal_social_welfare(input_time_slot):
        return input_time_slot * (expected_reward_from_worker(1, 3) + expected_reward_from_worker(2, 2) +
                                  expected_reward_from_worker(3, 3))


    #  Show u
    def show_u():
        print("Show u:")
        for n in range(1, number_of_platforms + 1):
            for m in range(1, number_of_workers + 1):
                print(expected_reward_from_worker(n, m))
        return


    #  Expected reward from workers
    def expected_reward_from_worker(input_platform, input_selected_worker):
        return intrinsic_value[input_platform] + \
               performance_of_worker[input_selected_worker] * task_size_of_platform[input_platform]


    #  Simulate the reward from workers
    def observe_reward_from_worker(input_platform, input_selected_worker):
        return intrinsic_value[input_platform] + \
               performance_of_worker[input_selected_worker] * task_size_of_platform[input_platform] + \
               (random.random() * fluctuate_range - fluctuate_range / 2)


    time_slot = 1
    social_welfare = 0

    while time_slot <= 100:
        worker_receive_task = []
        for m in range(0, number_of_workers + 1):
            task_list = []
            worker_receive_task.append(task_list)

        for n in range(number_of_platforms + 1):
            if n == 0:
                continue
            selected_worker = 1
            max_reward = expected_reward_from_worker(n, selected_worker)
            for m in range(2, number_of_workers + 1):
                if expected_reward_from_worker(n, m) > max_reward:
                    selected_worker = m
                    max_reward = expected_reward_from_worker(n, m)
            worker_receive_task[selected_worker].append(n)

        # print("worker_receive_task: " + str(worker_receive_task))
        for m in range(1, number_of_workers + 1):
            demand_sum = 0
            for wrt in worker_receive_task[m]:
                demand_sum = demand_sum + task_computation_demand[wrt]

            while demand_sum > task_computation_capacity[m]:
                abandon_task = math.floor(random.random() * len(worker_receive_task[m]))
                demand_sum = demand_sum - task_computation_demand[worker_receive_task[m][abandon_task]]
                new_worker_receive_task_m = []
                for task in range(len(worker_receive_task[m])):
                    if task != abandon_task:
                        new_worker_receive_task_m.append(worker_receive_task[m][task])
                worker_receive_task[m] = new_worker_receive_task_m

            for n in worker_receive_task[m]:
                social_welfare = social_welfare + observe_reward_from_worker(n, m)
                print("observe_reward_from_worker: " + str(n) + ", " + str(m))

        time_slot = time_slot + 1

    csv_writer.writerow([number_of_workers_list[index], social_welfare / float(time_slot)])

result_file.close()