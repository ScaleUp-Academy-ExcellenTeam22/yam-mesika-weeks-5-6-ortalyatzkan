

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


def get_recipe_price(prices,optionals='',**ingredients):
    """
    A function that receives a list of products
    quantities and products that
    will not be considered in the price and
    returns the price of the products
    :param prices:a list of products and prices
    :param optionals:List of products that will not be included in the price
    :param ingredients:Quantities of each product
    :return:the price
    """
    final_price=0
    for product in prices:
        if product not in optionals:#if the product is not in the list of products that are not included in the price
            final_price += prices.get(product)*ingredients.get(product)/100
    return final_price


if __name__== '__main__':
    print(join())
    print(join([1,2],[8],[9,5,6],sep='@'))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({}))