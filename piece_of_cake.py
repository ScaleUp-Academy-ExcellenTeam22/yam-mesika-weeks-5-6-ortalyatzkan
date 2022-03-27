from functools import reduce


def get_recipe_price(prices:list,optionals='', **ingredients)->int:
    """
    A function that receives a list of products quantities and products that will not be considered in the price.
    Returns the price of the products.
    :param prices:A list of products and prices.
    :param optionals:List of products that will not be included in the price.
    :param ingredients:Quantities of each product.
    :return:The price.
    """
    final_price=0
    final_price = reduce(lambda price,product:price+prices.get(product)*ingredients.get(product)/100  if (product not in optionals) else price, prices,0)
    return final_price


if __name__== '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8,'cookie':10}, optionals=['milk','cookie'], chocolate=300))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({}))
