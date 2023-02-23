import random
import csv
import pandas as pd
import re


#  A. Settings for platforms
#
#  Intrinsic_value \in [1, 2]
def initialize_intrinsic_value(input_number_of_platforms):
    return_intrinsic_value = []
    for i in range(input_number_of_platforms + 1):
        return_intrinsic_value.append(random.random() * 5 + 1 + (i - 1) * 5)
    return return_intrinsic_value


#  Task_size_of_platform \in [0.5, 1.6] MB
def initialize_task_size_of_platform(input_number_of_platforms):
    return_task_size_of_platform = []
    for i in range(input_number_of_platforms + 1):
        return_task_size_of_platform.append(random.random() * 5 + 1 + (i - 1) * 5)
    return return_task_size_of_platform


#  Task_computation_demand \in [0.5, 1]
def initialize_task_computation_demand(input_number_of_platforms):
    return_task_computation_demand = []
    for i in range(input_number_of_platforms + 1):
        return_task_computation_demand.append(random.random() * 0.5 + 0.5)
    return return_task_computation_demand


#  B. settings for workers
#
#  Performance_of_worker \in [1, 2], [11, 12], [21, 22], ... ?
def initialize_performance_of_worker(input_number_of_workers):
    return_performance_of_worker = []
    for i in range(input_number_of_workers + 1):
        return_performance_of_worker.append(random.random() * 5 + 1 + (i - 1) * 5)
    return return_performance_of_worker


# Task_computation_capacity \in [2, 3.5], [1.5, 2]
def initialize_task_computation_capacity(input_number_of_workers):
    return_task_computation_capacity = []
    for i in range(input_number_of_workers + 1):
        return_task_computation_capacity.append(random.random() * 0.5 + 1.5)
    return return_task_computation_capacity


#  C. Others
#
#  Fluctuate_range
def initialize_fluctuate_range():
    return 2


#  D. Write/Read Settings
#
#  Write Settings
def write_settings(number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform,
                   task_computation_demand, performance_of_worker, task_computation_capacity, fluctuate_range, T_explore):
    setting_file_path = './setting_file.csv'
    setting_file = open(setting_file_path, 'w', newline='')
    csv_writer = csv.writer(setting_file)
    csv_writer.writerow(['number_of_platforms', 'number_of_workers', 'intrinsic_value', 'task_size_of_platform',
                   'task_computation_demand', 'performance_of_worker', 'task_computation_capacity', 'fluctuate_range', 'T_explore'])
    csv_writer.writerow([number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform,
                   task_computation_demand, performance_of_worker, task_computation_capacity, fluctuate_range, T_explore])
    setting_file.close()
    return


#  Split for Read
def split_for_read(read_string):
    return_result = []
    split_parts = re.split(r',\s+', read_string[1:-1])
    for split_part in split_parts:
        return_result.append(float(split_part))
    return return_result


#  Read Settings
def read_settings(setting_file_name):
    settings = pd.read_csv('./' + setting_file_name + '.csv')
    number_of_platforms = int(settings['number_of_platforms'][0])
    number_of_workers = int(settings['number_of_workers'][0])
    intrinsic_value = split_for_read(settings['intrinsic_value'][0])
    task_size_of_platform = split_for_read(settings['task_size_of_platform'][0])
    task_computation_demand = split_for_read(settings['task_computation_demand'][0])
    performance_of_worker = split_for_read(settings['performance_of_worker'][0])
    task_computation_capacity = split_for_read(settings['task_computation_capacity'][0])
    fluctuate_range = float(settings['fluctuate_range'][0])
    return number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, \
           task_computation_demand, performance_of_worker, task_computation_capacity, fluctuate_range