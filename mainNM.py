import math
import matplotlib.pyplot as plt
import numpy as np
import data_class as dc
import json

ROOT = 0.176923


def algebraic_equasion_function(x):
    """
    This function makes a calculation for an Algebraic equasion
    It calculates f(x) with the given equasion and x as a parameter
    """
    formula = x**2 + 6*x + 9
    return formula


def algebraic_equasion_defunction(x):
    """
    This function makes a calculation for an Algebraic equasion
    It calculates f'(x) with the given equasion and x as a parameter
    """
    formula = 2*x + 6
    return formula


def algebraic_u(x):
    """
    This function makes a calculation for an Algebraic equasion
    It calculates u(x) = f(x)/f'(x) with the given equasion and x as a parameter
    """
    f = algebraic_equasion_function(x)
    de_f = algebraic_equasion_defunction(x)
    u = f / de_f
    return u


def function_F_of_X(x):  # function - f(x)
    """
    This function makes a calculation for Non-Algebraic equasion
    It calculates f(x) with the given equasion and x as a parameter
    """
    solution = x ** 3 + x + 2 * math.sqrt(math.e ** x)
    return solution


def DE_function_F_of_X(x):  # function - f'(x)
    """
    This function makes a calculation for Non-Algebraic equasion
    It calculates f'(x) with the given equasion and x as a parameter
    """
    solution = 3 * x ** 2 + 1 + math.sqrt(math.e ** x)
    return solution


def solve_U_function_of_X(x):  # function - u(x)
    """
    This function makes a calculation for Non-Algebraic equasion
    It calculates u(x) = f(x)/f'(x) with the given equasion and x as a parameter
    """
    f_of_x = function_F_of_X(x)
    de_f_of_x = DE_function_F_of_X(x)
    variable_u = f_of_x / de_f_of_x
    return variable_u


json_data = []

first = True


def save_data(the_data):
    json_data.append([{"VALUES": i.VALUES, "F_X": i.F_X, "DEF_X": i.DEF_X, "P1": i.P1, "P3": i.P3, "ERROR": i.ERROR,
                       "counter": i.counter} for i in the_data])


def save_data_to_json(filename_str: str):
    with open(filename_str, "w") as file:
        json.dump(json_data, file)
    json_data.clear()


def read_data_from_json(filename_str: str):
    with open(filename_str, "r") as file:
        data = json.load(file)
    return data


def print_data(filename_str: str, title: str):
    data = read_data_from_json(filename_str)
    list_Lables = []
    NR_non_al = []
    MP_non_al = []

    for d in data[:(int(len(data) / 2))]:
        print(f"Value: {d[0]['VALUES']} Counter: {d[-1]['counter']}")
        list_Lables.append(d[0]['VALUES'])
        NR_non_al.append(d[-1]['counter'])
    print()

    for d in data[(int(len(data) / 2)):]:
        print(f"Value: {d[0]['VALUES']} Counter: {d[-1]['counter']}")
        MP_non_al.append(d[-1]['counter'])

    make_a_plot(list_Lables, NR_non_al, MP_non_al, title)


def solve_until_zero(x, counter, temp_data):  # function calculate f(x) till f(x) == 0
    the_data = temp_data
    while True:
        f_of_x = round(function_F_of_X(x), 4)  # Our f'(x) for the table!
        if first:
            new_x = x - solve_U_function_of_X(x)  # Our X new for the table!
        else:
            new_x = x - 1 / 12 * (5 * solve_U_function_of_X(x) + 7 * f_of_x / DE_function_F_of_X(
                x - 6 * solve_U_function_of_X(x) / 7))  # Our X new for the table!

        p1 = calculate_p(x, new_x, 1)  # p1
        p3 = calculate_p(x, new_x, 3)  # p3
        #  DEBUG print(f"VALUE: {x}, F_OF_X:{f_of_x}, DE_F_OF_X: {de_f_of_x}, NEW_VALUE: {new_x}")
        if counter == -1:
            counter += 1
            the_data.append(dc.data_container(x, f_of_x, DE_function_F_of_X(x), "", "", calculate_error(x), counter))
        else:
            counter += 1
            if round(f_of_x, 4) != 0:
                the_data.append(
                    dc.data_container(new_x, round(function_F_of_X(new_x), 4), DE_function_F_of_X(new_x), p1, p3,
                                      calculate_error(new_x), counter))
                # for i in range(0, the_data.counter_DC()):
                #     the_data.print(i)
                return solve_until_zero(new_x, counter, the_data)
            else:
                break

    save_data(the_data)


def calculate_error(x: float):  # function to calculate an error ERROR
    error = abs(x - ROOT)
    return error


def calculate_p(old_x, new_x: float, power: int):  # function to calculate an error P1 (Power of 1)
    p = abs(new_x - ROOT) / abs(old_x - ROOT) ** power
    return p


def call_NA(list: list):
    global first
    counter = -1
    first = True
    for element in list:
        temp_data = []
        solve_until_zero(element, counter, temp_data)
        # print('\n')
    first = not first
    for element in list:
        temp_data = []
        solve_until_zero(element, counter, temp_data)
        # print('\n')

def solve_until_zeroA(x, counter, temp_data):  # function calculate f(x) till f(x) == 0
    the_data_algebraic = temp_data
    while True:
        f_of_x = round(function_F_of_X(x), 4)  # Our f'(x) for the table!
        if first:
            new_x = x - algebraic_u(x)  # Our X new for the table!
        else:
            new_x = x - 1 / 12 * (5 * algebraic_u(x) + 7 * round(algebraic_equasion_function(x),
                                                                 4) / algebraic_equasion_defunction(
                x - 6 * algebraic_u(x) / 7))

        p1 = calculate_p(x, new_x, 1)  # p1
        p3 = calculate_p(x, new_x, 3)  # p3
        #  DEBUG print(f"VALUE: {x}, F_OF_X:{f_of_x}, DE_F_OF_X: {de_f_of_x}, NEW_VALUE: {new_x}")
        if counter == -1:
            counter += 1
            the_data_algebraic.append(
                dc.data_container(x, f_of_x, DE_function_F_of_X(x), "", "", calculate_error(x), counter))
        else:
            counter += 1
            if round(f_of_x, 4) != 0:
                the_data_algebraic.append(
                    dc.data_container(new_x, round(function_F_of_X(new_x), 4), DE_function_F_of_X(new_x), p1, p3,
                                      calculate_error(new_x), counter))
                # for i in range(0, the_data.counter_DC()):
                #     the_data.print(i)
                return solve_until_zero(new_x, counter, the_data_algebraic)
            else:
                break

    save_data(the_data_algebraic)


def call_A(list: list):
    global first
    counter = -1
    for element in list:
        temp_data = []
        solve_until_zeroA(element, counter, temp_data)
        # print('\n')
    first = not first
    for element in list:
        temp_data = []
        solve_until_zeroA(element, counter, temp_data)
        # print('\n')


def make_a_plot(labels_parameter: list, NewtonMethod: list, MultiPoint: list, title: str):
    """
    This function makes a plot of the given data for comparison
    """
    x = np.arange(len(labels_parameter))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, MultiPoint, width, label='Multi-Point Method')
    rects2 = ax.bar(x + width / 2, NewtonMethod, width, label='Newtons Method')

    ax.set_ylabel('Number of Repeats')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels_parameter)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    labels = [-25.5, -20.7, -15.2, -10.7, -5.6, -1.9, 0.4, 1.5, 2.5, 10, 20.2, 50]
    print("NON ALGEBRAIC:")
    call_NA(labels)
    #print(json_data)
    save_data_to_json("data1.json")
    read_data_from_json("data1.json")
    print_data("data1.json", 'Non-Algebraic')
    print("ALGEBRAIC:")
    call_A(labels)
    #print(json_data)
    save_data_to_json("data2.json")
    read_data_from_json("data2.json")
    print_data("data2.json", 'Algebraic')

