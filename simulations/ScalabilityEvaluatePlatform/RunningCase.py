# Attention! All the indices count from 1.

import csv
import random
import math
import KnapsackSolver
import InitializeSettings


#  Calculate parameter N_min
def get_N_min(input_task_computation_demand, input_task_computation_capacity):
    max_task_computation_demand = 0
    for demand in input_task_computation_demand:
        if demand > max_task_computation_demand:
            max_task_computation_demand = demand
    min_task_computation_capacity = float('inf')
    for capacity in input_task_computation_capacity:
        if capacity < min_task_computation_capacity:
            min_task_computation_capacity = capacity
    return math.floor(float(min_task_computation_capacity) / float(max_task_computation_demand))


#  Initialize \tilde{u}_{n,m}^\tau
def initialize_u(input_number_of_platforms, input_number_of_workers):
    return_u = []
    for n in range(input_number_of_platforms + 1):
        u_row = []
        for m in range(input_number_of_workers + 1):
            u_row.append(0)
        return_u.append(u_row)
    return return_u


#  Initialize \Pi
def initialize_Pi(input_number_of_platforms):
    return_Pi = []
    for n in range(input_number_of_platforms + 1):
        return_Pi.append(0)
    return return_Pi


#  Initialize \Delta~\tilde{u}_{n,m}^\tau
def initialize_Delta(input_number_of_platforms, input_number_of_workers):
    return_Delta = []
    for n in range(input_number_of_platforms + 1):
        Delta_row = []
        for m in range(input_number_of_workers + 1):
            Delta_row.append(0)
        return_Delta.append(Delta_row)
    return return_Delta


#  Used to create [(weight, cost)]
def create_weight_cost(input_task_computation_demand, input_Delta, input_m):
    return_weight_cost = []
    for i in range(len(input_task_computation_demand)):
        if i == 0:
            continue
        return_weight_cost.append((input_task_computation_demand[i], input_Delta[i][input_m]))
    return return_weight_cost


#  Read settings
number_of_platforms_list = [3,5,7,9,11]
result_file_path = '../0-FigureDraw/scalability_platform_crowd2.csv'
result_file = open(result_file_path, 'w', newline='')
csv_writer = csv.writer(result_file)
csv_writer.writerow(['number_of_platforms', 'time_average_social_welfare'])

for index in range(len(number_of_platforms_list)):
    number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, task_computation_demand, \
    performance_of_worker, task_computation_capacity, fluctuate_range = InitializeSettings.read_settings('setting_file', index)

    N_min = get_N_min(task_computation_demand, task_computation_capacity)
    T_exploit = 0
    T_explore = 10
    #  Invoke Algorithm 1

    u = initialize_u(number_of_platforms, number_of_workers)
    tau = 1
    time_slot = 0
    social_welfare = 0

    #  Simulate the reward from workers
    def observe_reward_from_worker(input_platform, input_selected_worker):
        return intrinsic_value[input_platform] + \
               performance_of_worker[input_selected_worker] * task_size_of_platform[input_platform] + \
               (random.random() * fluctuate_range - fluctuate_range / 2)


    #  Define Algorithm 2
    def mapping_upon_multi_knapsack(u, input_number_of_platforms, input_number_of_workers, social_welfare, time_slot,
                                     tau):
        Pi = initialize_Pi(input_number_of_platforms)
        Delta = initialize_Delta(input_number_of_platforms, input_number_of_workers)
        for m in range(input_number_of_workers + 1):
            if m == 0:
                continue
            for n in range(input_number_of_platforms + 1):
                if n == 0:
                    continue
                if Pi[n] == 0:
                    Delta[n][m] = u[n][m]
                else:
                    Delta[n][m] = u[n][m] - u[n][Pi[n]]

            weight_cost = create_weight_cost(task_computation_demand, Delta, m)
            # solve knapsack problem
            best_cost, best_combination = KnapsackSolver.branch_and_bounds(input_number_of_platforms, \
                                                                           task_computation_capacity[m], \
                                                                           weight_cost)
            # Observe based on solution to knapsack problem
            for i in range(len(best_combination)):
                # for platform i + 1
                if best_combination[i] == 1:
                    observe_reward = observe_reward_from_worker(i + 1, m)
                    social_welfare = social_welfare + observe_reward
                    Pi[i + 1] = m

        return Pi, social_welfare


    while time_slot < 100:
        #  Exploring:
        print("tau = " + str(tau) + ": Exploring...")
        for t in range(T_explore + 1):
            # print(str(t) + "/" + str(T_explore))
            if t == 0:
                continue
            #  for b in range(number_of_batches):  #  Used when the real experiment is conducted
            for n in range(number_of_platforms + 1):
                if n == 0:
                    continue
                selected_worker = math.floor((n + t) % (N_min * number_of_workers) / N_min) + 1
                #  Simulate the reward from workers:
                observe_reward = observe_reward_from_worker(n, selected_worker)
                social_welfare = social_welfare + observe_reward
                u[n][selected_worker] = (u[n][selected_worker] * (tau - 1) + observe_reward) / tau
        time_slot = time_slot + T_explore

        #  Mapping:
        print("tau = " + str(tau) + ": Mapping...")
        Pi, social_welfare = mapping_upon_multi_knapsack(u, number_of_platforms, number_of_workers,
                                                                          social_welfare, time_slot, tau)

        time_slot = time_slot + number_of_workers

        #  Exploiting:
        print("tau = " + str(tau) + ": Exploiting...")
        # T_exploit = int(math.pow(2, tau))
        T_exploit = int(math.pow(100, tau))
        for t in range(T_exploit + 1):
            if t == 0:
                continue
            for n in range(number_of_platforms + 1):
                if n == 0:
                    continue
                selected_worker = Pi[n]
                if Pi[n] > 0:
                    observe_reward = observe_reward_from_worker(n, selected_worker)
                    social_welfare = social_welfare + observe_reward
        time_slot = time_slot + T_exploit
        #  Update tau:
        tau = tau + 1

    csv_writer.writerow([number_of_platforms_list[index], social_welfare / float(time_slot)])

result_file.close()