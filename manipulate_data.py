def manipulate_data(int_list):
    count = 0
    negative_int_sum = 0
    if type(int_list) != type([]):
        return 'Only lists allowed'
    for item in int_list:
        if item < 0:
            negative_int_sum += item
        else:
            count += 1
    result_list = [count, negative_int_sum]
    return result_list

