
def flatten(lst, out = []):

    for item in lst:
        if type(item) == list:
            flatten(item)
        else:
            out.append(item)

    return out


def reverse_it(lst):

    length = len(lst)

    for i in range(length):
        if type(lst[i]) == list:
            lst[i] = reverse_it(lst[i])
            
    return [lst[length - ind - 1] for ind in range(length)]
