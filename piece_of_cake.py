

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
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({}))