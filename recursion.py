def replicate_iter(times, data):
    """
	:Author: Mbuvi

    :param times:
    :param data:
    :return: data_list
    """
    data_list = []
    if isinstance(times, int) and (isinstance(data, str) or isinstance(data, int)):
        if times <= 0:
            data_list = []
        else:
            for item in range(times):
                data_list.append(data)
        return data_list
    else:
        raise ValueError

def replicate_recur(times, data):
    """

    :param times:
    :param data:
    :param data_list:
    :return: data_list
    """
    if isinstance(times, int) and (isinstance(data, str) or isinstance(data, int)):
        if times <= 0:
            return []
        else:
            #data_list.append(data)
            return [data] + replicate_recur(times - 1, data)
    else:
        raise ValueError



times = -1
data = 6

print(replicate_iter(times, data))
print(replicate_recur(times, data))
