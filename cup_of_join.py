def join(*lists:tuple ,sep='-')->list:
    """
    A function that get a number of lists and returns one list With the values of all the lists with value of sap between the list.
    :param lists:List to concatenate.
    :param sep:A value insert between lists.
    :return:One list of all the lists with sap between them.
    """
    concatenate_list = []
    # If no list was passed to the function.
    if len(lists) == 0:
        return None
    for index in range (len(lists)):
        concatenate_list += lists[index]
        # If this is not the last list.
        if index < len(lists)-1:
            concatenate_list += sep
    return concatenate_list


if __name__ == '__main__':
    print(join())
    print(join([1,2],[8],[9,5,6],sep='@'))
