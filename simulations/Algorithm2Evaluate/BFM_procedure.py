import mknapsack



# worker = 3


# platform = 3
def BFM_3(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        for d_2 in decision:
            for d_3 in decision:
                weight_accum = [0, 0, 0, 0]
                weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]

                value_accum = 0
                if d_1 != 0:
                    value_accum = value_accum + u[1][d_1]
                if d_2 != 0:
                    value_accum = value_accum + u[2][d_2]
                if d_3 != 0:
                    value_accum = value_accum + u[3][d_3]

                if weight_accum[1] <= task_computation_capacity[1] and \
                        weight_accum[2] <= task_computation_capacity[2] and \
                        weight_accum[3] <= task_computation_capacity[3]:
                    if value_accum > max_value:
                        max_value = value_accum
    return value_accum


# platform = 5
def BFM_5(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        for d_2 in decision:
            for d_3 in decision:
                for d_4 in decision:
                    for d_5 in decision:
                        weight_accum = [0, 0, 0, 0]
                        weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                        weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                        weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]
                        weight_accum[d_4] = weight_accum[d_4] + task_computation_demand[4]
                        weight_accum[d_5] = weight_accum[d_5] + task_computation_demand[5]

                        value_accum = 0
                        if d_1 != 0:
                            value_accum = value_accum + u[1][d_1]
                        if d_2 != 0:
                            value_accum = value_accum + u[2][d_2]
                        if d_3 != 0:
                            value_accum = value_accum + u[3][d_3]
                        if d_4 != 0:
                            value_accum = value_accum + u[4][d_4]
                        if d_5 != 0:
                            value_accum = value_accum + u[5][d_5]

                        if weight_accum[1] <= task_computation_capacity[1] and \
                                weight_accum[2] <= task_computation_capacity[2] and \
                                weight_accum[3] <= task_computation_capacity[3]:
                            if value_accum > max_value:
                                max_value = value_accum
    return value_accum


# platform = 6
def BFM_6(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        for d_2 in decision:
            for d_3 in decision:
                for d_4 in decision:
                    for d_5 in decision:
                        for d_6 in decision:
                            weight_accum = [0, 0, 0, 0]
                            weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                            weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                            weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]
                            weight_accum[d_4] = weight_accum[d_4] + task_computation_demand[4]
                            weight_accum[d_5] = weight_accum[d_5] + task_computation_demand[5]
                            weight_accum[d_6] = weight_accum[d_6] + task_computation_demand[6]

                            value_accum = 0
                            if d_1 != 0:
                                value_accum = value_accum + u[1][d_1]
                            if d_2 != 0:
                                value_accum = value_accum + u[2][d_2]
                            if d_3 != 0:
                                value_accum = value_accum + u[3][d_3]
                            if d_4 != 0:
                                value_accum = value_accum + u[4][d_4]
                            if d_5 != 0:
                                value_accum = value_accum + u[5][d_5]
                            if d_6 != 0:
                                value_accum = value_accum + u[6][d_6]

                            if weight_accum[1] <= task_computation_capacity[1] and \
                                    weight_accum[2] <= task_computation_capacity[2] and \
                                    weight_accum[3] <= task_computation_capacity[3]:
                                if value_accum > max_value:
                                    max_value = value_accum
    return value_accum


# platform = 7
def BFM_7(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        for d_2 in decision:
            for d_3 in decision:
                for d_4 in decision:
                    for d_5 in decision:
                        for d_6 in decision:
                            for d_7 in decision:
                                weight_accum = [0, 0, 0, 0]
                                weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                                weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                                weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]
                                weight_accum[d_4] = weight_accum[d_4] + task_computation_demand[4]
                                weight_accum[d_5] = weight_accum[d_5] + task_computation_demand[5]
                                weight_accum[d_6] = weight_accum[d_6] + task_computation_demand[6]
                                weight_accum[d_7] = weight_accum[d_7] + task_computation_demand[7]

                                value_accum = 0
                                if d_1 != 0:
                                    value_accum = value_accum + u[1][d_1]
                                if d_2 != 0:
                                    value_accum = value_accum + u[2][d_2]
                                if d_3 != 0:
                                    value_accum = value_accum + u[3][d_3]
                                if d_4 != 0:
                                    value_accum = value_accum + u[4][d_4]
                                if d_5 != 0:
                                    value_accum = value_accum + u[5][d_5]
                                if d_6 != 0:
                                    value_accum = value_accum + u[6][d_6]
                                if d_7 != 0:
                                    value_accum = value_accum + u[7][d_7]

                                if weight_accum[1] <= task_computation_capacity[1] and \
                                        weight_accum[2] <= task_computation_capacity[2] and \
                                        weight_accum[3] <= task_computation_capacity[3]:
                                    if value_accum > max_value:
                                        max_value = value_accum
    return value_accum


# platform = 9
def BFM_9(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        for d_2 in decision:
            for d_3 in decision:
                for d_4 in decision:
                    for d_5 in decision:
                        for d_6 in decision:
                            for d_7 in decision:
                                for d_8 in decision:
                                    for d_9 in decision:
                                        weight_accum = [0, 0, 0, 0]
                                        weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                                        weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                                        weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]
                                        weight_accum[d_4] = weight_accum[d_4] + task_computation_demand[4]
                                        weight_accum[d_5] = weight_accum[d_5] + task_computation_demand[5]
                                        weight_accum[d_6] = weight_accum[d_6] + task_computation_demand[6]
                                        weight_accum[d_7] = weight_accum[d_7] + task_computation_demand[7]
                                        weight_accum[d_8] = weight_accum[d_8] + task_computation_demand[8]
                                        weight_accum[d_9] = weight_accum[d_9] + task_computation_demand[9]

                                        value_accum = 0
                                        if d_1 != 0:
                                            value_accum = value_accum + u[1][d_1]
                                        if d_2 != 0:
                                            value_accum = value_accum + u[2][d_2]
                                        if d_3 != 0:
                                            value_accum = value_accum + u[3][d_3]
                                        if d_4 != 0:
                                            value_accum = value_accum + u[4][d_4]
                                        if d_5 != 0:
                                            value_accum = value_accum + u[5][d_5]
                                        if d_6 != 0:
                                            value_accum = value_accum + u[6][d_6]
                                        if d_7 != 0:
                                            value_accum = value_accum + u[7][d_7]
                                        if d_8 != 0:
                                            value_accum = value_accum + u[8][d_8]
                                        if d_9 != 0:
                                            value_accum = value_accum + u[9][d_9]

                                        if weight_accum[1] <= task_computation_capacity[1] and \
                                                weight_accum[2] <= task_computation_capacity[2] and \
                                                weight_accum[3] <= task_computation_capacity[3]:
                                            if value_accum > max_value:
                                                max_value = value_accum
    return value_accum


# platform = 11
def BFM_11(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    optimal_decision = []
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        print("BFM_11: " + str(d_1))
        for d_2 in decision:
            for d_3 in decision:
                for d_4 in decision:
                    for d_5 in decision:
                        for d_6 in decision:
                            for d_7 in decision:
                                for d_8 in decision:
                                    for d_9 in decision:
                                        for d_10 in decision:
                                            for d_11 in decision:
                                                weight_accum = [0, 0, 0, 0]
                                                weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                                                weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                                                weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]
                                                weight_accum[d_4] = weight_accum[d_4] + task_computation_demand[4]
                                                weight_accum[d_5] = weight_accum[d_5] + task_computation_demand[5]
                                                weight_accum[d_6] = weight_accum[d_6] + task_computation_demand[6]
                                                weight_accum[d_7] = weight_accum[d_7] + task_computation_demand[7]
                                                weight_accum[d_8] = weight_accum[d_8] + task_computation_demand[8]
                                                weight_accum[d_9] = weight_accum[d_9] + task_computation_demand[9]
                                                weight_accum[d_10] = weight_accum[d_10] + task_computation_demand[10]
                                                weight_accum[d_11] = weight_accum[d_11] + task_computation_demand[11]

                                                value_accum = 0
                                                if d_1 != 0:
                                                    value_accum = value_accum + u[1][d_1]
                                                if d_2 != 0:
                                                    value_accum = value_accum + u[2][d_2]
                                                if d_3 != 0:
                                                    value_accum = value_accum + u[3][d_3]
                                                if d_4 != 0:
                                                    value_accum = value_accum + u[4][d_4]
                                                if d_5 != 0:
                                                    value_accum = value_accum + u[5][d_5]
                                                if d_6 != 0:
                                                    value_accum = value_accum + u[6][d_6]
                                                if d_7 != 0:
                                                    value_accum = value_accum + u[7][d_7]
                                                if d_8 != 0:
                                                    value_accum = value_accum + u[8][d_8]
                                                if d_9 != 0:
                                                    value_accum = value_accum + u[9][d_9]
                                                if d_10 != 0:
                                                    value_accum = value_accum + u[10][d_10]
                                                if d_11 != 0:
                                                    value_accum = value_accum + u[11][d_11]

                                                if weight_accum[1] <= task_computation_capacity[1] and \
                                                        weight_accum[2] <= task_computation_capacity[2] and \
                                                        weight_accum[3] <= task_computation_capacity[3]:
                                                    if value_accum > max_value:
                                                        max_value = value_accum
                                                        optimal_decision = [d_1, d_2, d_3, d_3, d_5, d_6, d_7, d_8, d_9, d_10, d_11]
    print(optimal_decision)
    return value_accum


# platform = 12
def BFM_12(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    optimal_decision = []
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        print("BFM_12: " + str(d_1))
        for d_2 in decision:
            for d_3 in decision:
                for d_4 in decision:
                    for d_5 in decision:
                        for d_6 in decision:
                            for d_7 in decision:
                                for d_8 in decision:
                                    for d_9 in decision:
                                        for d_10 in decision:
                                            for d_11 in decision:
                                                for d_12 in decision:
                                                    weight_accum = [0, 0, 0, 0]
                                                    weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                                                    weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                                                    weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]
                                                    weight_accum[d_4] = weight_accum[d_4] + task_computation_demand[4]
                                                    weight_accum[d_5] = weight_accum[d_5] + task_computation_demand[5]
                                                    weight_accum[d_6] = weight_accum[d_6] + task_computation_demand[6]
                                                    weight_accum[d_7] = weight_accum[d_7] + task_computation_demand[7]
                                                    weight_accum[d_8] = weight_accum[d_8] + task_computation_demand[8]
                                                    weight_accum[d_9] = weight_accum[d_9] + task_computation_demand[9]
                                                    weight_accum[d_10] = weight_accum[d_10] + task_computation_demand[10]
                                                    weight_accum[d_11] = weight_accum[d_11] + task_computation_demand[11]
                                                    weight_accum[d_12] = weight_accum[d_12] + task_computation_demand[12]

                                                    value_accum = 0
                                                    if d_1 != 0:
                                                        value_accum = value_accum + u[1][d_1]
                                                    if d_2 != 0:
                                                        value_accum = value_accum + u[2][d_2]
                                                    if d_3 != 0:
                                                        value_accum = value_accum + u[3][d_3]
                                                    if d_4 != 0:
                                                        value_accum = value_accum + u[4][d_4]
                                                    if d_5 != 0:
                                                        value_accum = value_accum + u[5][d_5]
                                                    if d_6 != 0:
                                                        value_accum = value_accum + u[6][d_6]
                                                    if d_7 != 0:
                                                        value_accum = value_accum + u[7][d_7]
                                                    if d_8 != 0:
                                                        value_accum = value_accum + u[8][d_8]
                                                    if d_9 != 0:
                                                        value_accum = value_accum + u[9][d_9]
                                                    if d_10 != 0:
                                                        value_accum = value_accum + u[10][d_10]
                                                    if d_11 != 0:
                                                        value_accum = value_accum + u[11][d_11]
                                                    if d_12 != 0:
                                                        value_accum = value_accum + u[12][d_12]

                                                    if weight_accum[1] <= task_computation_capacity[1] and \
                                                            weight_accum[2] <= task_computation_capacity[2] and \
                                                            weight_accum[3] <= task_computation_capacity[3]:
                                                        if value_accum > max_value:
                                                            max_value = value_accum
                                                            optimal_decision = [d_1, d_2, d_3, d_3, d_5, d_6, d_7, d_8, d_9, d_10, d_11, d_12]
    print(optimal_decision)
    return value_accum


# platform = 15
def BFM_15(u, task_computation_demand, task_computation_capacity):
    max_value = 0
    optimal_decision = []
    decision = [0, 1, 2, 3]
    for d_1 in decision:
        print("BFM_15: " + str(d_1))
        for d_2 in decision:
            for d_3 in decision:
                for d_4 in decision:
                    for d_5 in decision:
                        for d_6 in decision:
                            for d_7 in decision:
                                for d_8 in decision:
                                    for d_9 in decision:
                                        for d_10 in decision:
                                            for d_11 in decision:
                                                for d_12 in decision:
                                                    for d_13 in decision:
                                                        for d_14 in decision:
                                                            for d_15 in decision:
                                                                weight_accum = [0, 0, 0, 0]
                                                                weight_accum[d_1] = weight_accum[d_1] + task_computation_demand[1]
                                                                weight_accum[d_2] = weight_accum[d_2] + task_computation_demand[2]
                                                                weight_accum[d_3] = weight_accum[d_3] + task_computation_demand[3]
                                                                weight_accum[d_4] = weight_accum[d_4] + task_computation_demand[4]
                                                                weight_accum[d_5] = weight_accum[d_5] + task_computation_demand[5]
                                                                weight_accum[d_6] = weight_accum[d_6] + task_computation_demand[6]
                                                                weight_accum[d_7] = weight_accum[d_7] + task_computation_demand[7]
                                                                weight_accum[d_8] = weight_accum[d_8] + task_computation_demand[8]
                                                                weight_accum[d_9] = weight_accum[d_9] + task_computation_demand[9]
                                                                weight_accum[d_10] = weight_accum[d_10] + task_computation_demand[10]
                                                                weight_accum[d_11] = weight_accum[d_11] + task_computation_demand[11]
                                                                weight_accum[d_12] = weight_accum[d_12] + task_computation_demand[12]
                                                                weight_accum[d_13] = weight_accum[d_13] + \
                                                                                     task_computation_demand[13]
                                                                weight_accum[d_14] = weight_accum[d_14] + \
                                                                                     task_computation_demand[14]
                                                                weight_accum[d_15] = weight_accum[d_15] + \
                                                                                     task_computation_demand[15]

                                                                value_accum = 0
                                                                if d_1 != 0:
                                                                    value_accum = value_accum + u[1][d_1]
                                                                if d_2 != 0:
                                                                    value_accum = value_accum + u[2][d_2]
                                                                if d_3 != 0:
                                                                    value_accum = value_accum + u[3][d_3]
                                                                if d_4 != 0:
                                                                    value_accum = value_accum + u[4][d_4]
                                                                if d_5 != 0:
                                                                    value_accum = value_accum + u[5][d_5]
                                                                if d_6 != 0:
                                                                    value_accum = value_accum + u[6][d_6]
                                                                if d_7 != 0:
                                                                    value_accum = value_accum + u[7][d_7]
                                                                if d_8 != 0:
                                                                    value_accum = value_accum + u[8][d_8]
                                                                if d_9 != 0:
                                                                    value_accum = value_accum + u[9][d_9]
                                                                if d_10 != 0:
                                                                    value_accum = value_accum + u[10][d_10]
                                                                if d_11 != 0:
                                                                    value_accum = value_accum + u[11][d_11]
                                                                if d_12 != 0:
                                                                    value_accum = value_accum + u[12][d_12]
                                                                if d_13 != 0:
                                                                    value_accum = value_accum + u[13][d_13]
                                                                if d_14 != 0:
                                                                    value_accum = value_accum + u[14][d_14]
                                                                if d_15 != 0:
                                                                    value_accum = value_accum + u[15][d_15]

                                                                if weight_accum[1] <= task_computation_capacity[1] and \
                                                                        weight_accum[2] <= task_computation_capacity[2] and \
                                                                        weight_accum[3] <= task_computation_capacity[3]:
                                                                    if value_accum > max_value:
                                                                        max_value = value_accum
                                                                        optimal_decision = [d_1, d_2, d_3, d_3, d_5, d_6, d_7, d_8, d_9, d_10, d_11, d_12, d_13, d_14, d_15]
    print(optimal_decision)
    return value_accum