# Attention! All the indices count from 1.

import csv
import random
import math
import KnapsackSolver
import InitializeSettings
import BFM_procedure
import time


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


#  Show \Pi
def show_Pi(input_tau, Pi):
    print("tau = " + str(input_tau) + ":")
    for i in range(len(Pi)):
        if i == 0:
            continue
        print("Platform " + str(i) + " dispatches to worker " + str(Pi[i]))
    return


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


result_file_path = '../0-FigureDraw/BFM.csv'
result_file = open(result_file_path, 'a', newline='')
csv_writer = csv.writer(result_file)
csv_writer.writerow(['number_of_platforms', 'social_welfare', 'time_cost'])

#  Read settings
number_of_platforms_list = [3, 5, 7, 9, 11]
for index in range(len(number_of_platforms_list)):
    number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, task_computation_demand, \
            performance_of_worker, task_computation_capacity = InitializeSettings.read_settings('setting_file', index)

    u = initialize_u(number_of_platforms, number_of_workers)
    for n in range(1, number_of_platforms + 1):
        for m in range(1, number_of_workers + 1):
            u[n][m] = intrinsic_value[n] + performance_of_worker[m] * task_size_of_platform[n]
    social_welfare = 0

    time_start = time.time()

    ## BFM:
    if number_of_platforms == 3:
        social_welfare = BFM_procedure.BFM_3(u, task_computation_demand, task_computation_capacity)
    elif number_of_platforms == 5:
        social_welfare = BFM_procedure.BFM_5(u, task_computation_demand, task_computation_capacity)
    elif number_of_platforms == 7:
        social_welfare = BFM_procedure.BFM_7(u, task_computation_demand, task_computation_capacity)
    elif number_of_platforms == 9:
        social_welfare = BFM_procedure.BFM_9(u, task_computation_demand, task_computation_capacity)
    elif number_of_platforms == 11:
        social_welfare = BFM_procedure.BFM_11(u, task_computation_demand, task_computation_capacity)

    time_end = time.time()
    time_sum = time_end - time_start

    csv_writer.writerow([number_of_platforms_list[index], social_welfare, time_sum])

result_file.close()
