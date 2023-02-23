# Attention! All the indices count from 1.

import csv
import random
import math
import KnapsackSolver
import InitializeSettings


#  Read settings
number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, task_computation_demand, \
performance_of_worker, task_computation_capacity, fluctuate_range = InitializeSettings.read_settings('setting_file')



print(number_of_platforms)
print(number_of_workers)
print(intrinsic_value[1:])
print(task_size_of_platform[1:])
print(task_computation_demand[1:])
print(performance_of_worker[1:])
print(task_computation_capacity[1:])
print(fluctuate_range)


# Used to calculate the optimal social welfare, then the regret
def get_optimal_social_welfare(input_time_slot):
    return input_time_slot * (expected_reward_from_worker(1, 3) + expected_reward_from_worker(2, 2) +
                              expected_reward_from_worker(3, 3))

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


#  Calculate parameter N_max
def get_N_max(input_task_computation_demand, input_task_computation_capacity):
    min_task_computation_demand = float('inf')
    for demand in input_task_computation_demand:
        if demand < min_task_computation_demand:
            min_task_computation_demand = demand
    max_task_computation_capacity = 0
    for capacity in input_task_computation_capacity:
        if capacity > max_task_computation_capacity:
            max_task_computation_capacity = capacity
    return math.ceil(float(max_task_computation_capacity) / float(min_task_computation_demand))


#  Get delta_min
def get_delta_min():
    #  get delta_min^1
    delta_min1 = float('inf')
    for n in range(1, number_of_platforms + 1):
        for n_p in range(1, number_of_platforms + 1):
            for m in range(1, number_of_workers + 1):
                if n == n_p:
                    continue
                if math.fabs(expected_reward_from_worker(n, m) - expected_reward_from_worker(n_p, m)) < delta_min1:
                    delta_min1 = math.fabs(expected_reward_from_worker(n, m) - expected_reward_from_worker(n_p, m))
    print("delta_min1: " + str(delta_min1))

    #  get delta_min^2
    delta_min2 = float('inf')
    for n in range(1, number_of_platforms + 1):
        for n_p in range(1, number_of_platforms + 1):
            for m in range(1, number_of_workers + 1):
                for m_p in range(1, number_of_workers + 1):
                    if n == n_p or m == m_p:
                        continue
                    if math.fabs((expected_reward_from_worker(n, m) - expected_reward_from_worker(n, m_p)) - \
                                 expected_reward_from_worker(n_p, m)) < delta_min2:
                        delta_min2 = math.fabs((expected_reward_from_worker(n, m) - expected_reward_from_worker(n, m_p)) - \
                                 expected_reward_from_worker(n_p, m))
    print("delta_min2: " + str(delta_min2))

    #  get delta_min^3
    delta_min3 = float('inf')
    for n in range(1, number_of_platforms + 1):
        for n_p in range(1, number_of_platforms + 1):
            for m in range(1, number_of_workers + 1):
                for m_p in range(1, number_of_workers + 1):
                    for m_pp in range(1, number_of_workers + 1):
                        if n == n_p or m == m_p or m == m_pp:
                            continue
                        if math.fabs((expected_reward_from_worker(n, m) - expected_reward_from_worker(n, m_p)) - \
                                     (expected_reward_from_worker(n_p, m) - expected_reward_from_worker(n_p, m_pp))) < delta_min3:
                            if math.fabs((expected_reward_from_worker(n, m) - expected_reward_from_worker(n, m_p)) - \
                                         (expected_reward_from_worker(n_p, m) - expected_reward_from_worker(n_p, m_pp))) == 0:
                                print("n, n_p, m, m_p, m_pp: " + str(n) + ", " + str(n_p) + ", " + str(m) + ", " + \
                                      str(m_p) + ", " + str(m_pp))
                                print(expected_reward_from_worker(n, m))
                                print(expected_reward_from_worker(n, m_p))
                                print(expected_reward_from_worker(n, m) - expected_reward_from_worker(n, m_p))
                                print(expected_reward_from_worker(n_p, m))
                                print(expected_reward_from_worker(n_p, m_pp))
                                print(expected_reward_from_worker(n_p, m) - expected_reward_from_worker(n_p, m_pp))
                            delta_min3 = math.fabs((expected_reward_from_worker(n, m) - expected_reward_from_worker(n, m_p)) - \
                                     (expected_reward_from_worker(n_p, m) - expected_reward_from_worker(n_p, m_pp)))
    print("delta_min3: " + str(delta_min3))

    #  get the min of {delta_min1, delta_min2, delta_min3}
    return_delta_min = min(delta_min1, delta_min2, delta_min3)
    return return_delta_min


#  Show u
def show_u():
    print("Show u:")
    for n in range(1, number_of_platforms + 1):
        for m in range(1, number_of_workers + 1):
            print(expected_reward_from_worker(n, m))
    return


#  Get u_max
def get_u_max():
    return_u_max = 0
    for n in range(1, number_of_platforms + 1):
        for m in range(1, number_of_workers + 1):
            if expected_reward_from_worker(n, m) > return_u_max:
                return_u_max = expected_reward_from_worker(n, m)
    return return_u_max + fluctuate_range / 2


#  Get u_min
def get_u_min():
    return_u_min = float('inf')
    for n in range(1, number_of_platforms + 1):
        for m in range(1, number_of_workers + 1):
            if expected_reward_from_worker(n, m) < return_u_min:
                return_u_min = expected_reward_from_worker(n, m)
    return return_u_min - fluctuate_range / 2


#  Expected reward from workers
def expected_reward_from_worker(input_platform, input_selected_worker):
    return intrinsic_value[input_platform] + \
           performance_of_worker[input_selected_worker] * task_size_of_platform[input_platform]


#  Simulate the reward from workers
def observe_reward_from_worker(input_platform, input_selected_worker):
    return intrinsic_value[input_platform] + \
           performance_of_worker[input_selected_worker] * task_size_of_platform[input_platform] + \
           (random.random() * fluctuate_range - fluctuate_range / 2)


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
    for i in range(number_of_platforms + 1):
        if i == 0:
            continue
        return_weight_cost.append((input_task_computation_demand[i], input_Delta[i][input_m]))
    return return_weight_cost


#  Define Algorithm 2
def mapping_upon_multi_knapsack(u, input_number_of_platforms, input_number_of_workers, social_welfare, time_slot,
                                csv_writer, tau):
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
                                                                       task_computation_capacity[m],\
                                                                       weight_cost)
        # Observe based on solution to knapsack problem
        for i in range(len(best_combination)):
            # for platform i + 1
            if best_combination[i] == 1:
                observe_reward = observe_reward_from_worker(i + 1, m)
                social_welfare = social_welfare + observe_reward
                Pi[i + 1] = m

        regret_current = get_optimal_social_welfare(time_slot + m) - social_welfare
        print("time_slot: " + str(time_slot + m) + ', social_welfare: ' + str(social_welfare) + ', regret: ' + str(regret_current))
        csv_writer.writerow([tau, time_slot + m, 'Mapping', social_welfare, regret_current])
    return Pi, social_welfare


#  Define Algorithm 1
def video_analytics_dispatch_with_bandit(T_explore, T_exploit, N_min, number_of_batches):

    return T_explore, T_exploit


#  Main function entry:
#
#
#  Some parameters
N_min = get_N_min(task_computation_demand, task_computation_capacity)
N_max = get_N_max(task_computation_demand, task_computation_capacity)
number_of_batches = math.ceil(float(number_of_platforms) / float((N_min * number_of_workers)))
delta_min = get_delta_min()
show_u()
u_max = get_u_max()
u_min = get_u_min()
T_explore = math.ceil(float(25 * N_max * N_max * (u_max - u_min) * (u_max - u_min) * number_of_workers) / \
                      float(2 * delta_min * delta_min))
print("N_min: " + str(N_min))
print("N_max: " + str(N_max))
print("u_max - u_min: " + str(u_max - u_min))
print("delta_min: " + str(delta_min))
print("T_explore: " + str(T_explore))
T_exploit = 0
#
#
#  Invoke Algorithm 1
T_explore = 5

u = initialize_u(number_of_platforms, number_of_workers)
tau = 1
time_slot = 0
social_welfare = 0

result_file_path = '../0-FigureDraw/flexibility_join_social_welfare.csv'
result_file = open(result_file_path, 'w', newline='')
csv_writer = csv.writer(result_file)
csv_writer.writerow(['tau', 'time_slot', 'phase', 'social_welfare', 'regret'])

number_of_platforms = number_of_platforms - 1

while True:
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
        regret_current = get_optimal_social_welfare(time_slot + t) - social_welfare
        print("time_slot: " + str(time_slot + t) + ', social_welfare: ' + str(social_welfare) + ', regret: ' + str(
            regret_current))
        csv_writer.writerow([tau, time_slot + t, 'Exploring', social_welfare, regret_current])
    time_slot = time_slot + T_explore

    #  Mapping:
    print("tau = " + str(tau) + ": Mapping...")
    Pi, social_welfare = mapping_upon_multi_knapsack(u, number_of_platforms, number_of_workers,
                                                                      social_welfare, time_slot, csv_writer, tau)
    time_slot = time_slot + number_of_workers
    show_Pi(tau, Pi)

    #  Exploiting:
    print("tau = " + str(tau) + ": Exploiting...")
    # T_exploit = int(math.pow(2, tau))
    T_exploit = int(math.pow(17, tau))
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

        regret_current = get_optimal_social_welfare(time_slot + t) - social_welfare
        print("time_slot: " + str(time_slot + t) + ', social_welfare: ' + str(social_welfare) + ', regret: ' + str(
            regret_current))
        csv_writer.writerow([tau, time_slot + t, 'Exploiting', social_welfare, regret_current])
    time_slot = time_slot + T_exploit

    print("time_slot:" + str(time_slot))
    #  Update tau:
    tau = tau + 1
    if tau == 2:
        number_of_platforms = number_of_platforms + 1
        print("Join! time_slot:" + str(time_slot))

result_file.close()


