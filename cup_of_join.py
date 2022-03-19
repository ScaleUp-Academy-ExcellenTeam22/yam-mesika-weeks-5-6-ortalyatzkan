def join(*lists ,sep='-'):
    """
    A function that get a number of lists and
     returns one list With the values ​​of all the lists with value of sap between the list
    :param parameters:list
    :param sep:a value insert between lists
    :return:One list of all the lists with sap between them
    """
    temp=[]
    if len(lists)== 0:#if no list was passed to the function
        return None
    for index in range (len(lists)):
        temp+=lists[index]
        if index < len(lists)-1:#If this is not the last list
            temp+=sep
    return temp

if __name__ == '__main__':
    print(join())
    print(join([1,2],[8],[9,5,6],sep='@'))