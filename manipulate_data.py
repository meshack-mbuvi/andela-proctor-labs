def manipulate_data(int_list):
    """
    :Author:Mbuvi
    :Function manipulate_data that calculates the sum of negative numbers 
       and count of all positive numbers in a list
    :Params: int_list-list containing signed integers
    :Return type:result_list-A list with count of +ve numbers at first index 
    and sum of -ve numbers at second index
    """
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
print manipulate_data({})
