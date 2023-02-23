# Attention! All the indices count from 1.


import random
import math
import KnapsackSolver
import InitializeSettings


#  settings for platforms
number_of_platforms_list = [3, 5, 7, 9, 11]
first_flag = 1
for number_of_platforms in number_of_platforms_list:
    intrinsic_value = InitializeSettings.initialize_intrinsic_value(number_of_platforms)
    task_size_of_platform = InitializeSettings.initialize_task_size_of_platform(number_of_platforms)
    task_computation_demand = InitializeSettings.initialize_task_computation_demand(number_of_platforms)

    #  settings for workers
    number_of_workers = 3
    performance_of_worker = InitializeSettings.initialize_performance_of_worker(number_of_workers)
    task_computation_capacity = InitializeSettings.initialize_task_computation_capacity(number_of_workers)
    if first_flag == 1:
        first_flag = 0
        InitializeSettings.write_settings(1, number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, \
                                      task_computation_demand, performance_of_worker, task_computation_capacity)
    else:
        InitializeSettings.write_settings(0, number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, task_computation_demand, performance_of_worker, task_computation_capacity)