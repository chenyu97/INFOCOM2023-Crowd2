# Attention! All the indices count from 1.


import random
import math
import KnapsackSolver
import InitializeSettings

#  settings for platforms
number_of_workers_list = [3, 5, 7, 9, 11]
first_flag = 1
for number_of_workers in number_of_workers_list:
    number_of_platforms = 3
    intrinsic_value = InitializeSettings.initialize_intrinsic_value(number_of_platforms)
    task_size_of_platform = InitializeSettings.initialize_task_size_of_platform(number_of_platforms)
    task_computation_demand = InitializeSettings.initialize_task_computation_demand(number_of_platforms)

    #  settings for workers
    performance_of_worker = InitializeSettings.initialize_performance_of_worker(number_of_workers)
    task_computation_capacity = InitializeSettings.initialize_task_computation_capacity(number_of_workers)
    #  settings for stochastic variability
    fluctuate_range = InitializeSettings.initialize_fluctuate_range()

    if first_flag == 1:
        first_flag = 0
        InitializeSettings.write_settings(1, number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, \
                                      task_computation_demand, performance_of_worker, task_computation_capacity, fluctuate_range)
    else:
        InitializeSettings.write_settings(0, number_of_platforms, number_of_workers, intrinsic_value, task_size_of_platform, task_computation_demand, performance_of_worker, task_computation_capacity, fluctuate_range)




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
    for i in range(len(input_task_computation_demand)):
        if i == 0:
            continue
        return_weight_cost.append((input_task_computation_demand[i], input_Delta[i][input_m]))
    return return_weight_cost


#  Define Algorithm 2
def mapping_upon_multi_knapsack(u, input_number_of_platforms, input_number_of_workers):
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
                Pi[i + 1] = m
    return Pi


#  Define Algorithm 1
def video_analytics_dispatch_with_bandit(T_explore, T_exploit, N_min, number_of_batches):
    u = initialize_u(number_of_platforms, number_of_workers)
    tau = 1
    time_slot = 1
    while True:
        #  Exploring:
        print("tau = " + str(tau) + ": Exploring...")
        for t in range(T_explore + 1):
            print(str(t) + "/" + str(T_explore))
            if t == 0:
                continue
            #  for b in range(number_of_batches):  #  Used when the real experiment is conducted
            for n in range(number_of_platforms + 1):
                if n == 0:
                    continue
                selected_worker = math.floor((n + t) % (N_min * number_of_workers) / N_min) + 1
                #  Simulate the reward from workers:
                observe_reward = observe_reward_from_worker(n, selected_worker)
                u[n][selected_worker] = (u[n][selected_worker] * (tau - 1) + observe_reward) / tau
        time_slot = time_slot + T_explore

        #  Mapping:
        print("tau = " + str(tau) + ": Mapping...")
        Pi = mapping_upon_multi_knapsack(u, number_of_platforms, number_of_workers)
        time_slot = time_slot + number_of_workers
        show_Pi(tau, Pi)

        #  Exploiting:
        print("tau = " + str(tau) + ": Exploiting...")
        T_exploit = int(math.pow(2, tau))
        for t in range(T_exploit):
            for n in range(number_of_platforms + 1):
                if n == 0:
                    continue
                selected_worker = Pi[n]
                observe_reward = observe_reward_from_worker(n, selected_worker)
        time_slot = time_slot + T_exploit

        #  Update tau:
        tau = tau + 1
    return T_explore, T_exploit


