

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {'A':50,'B':30,'C':20,'D':15}
    checkout_price = 0

    for sku in skus:
        if sku not in item_prices:
            return -1
        checkout_price += item_prices[sku]

    if skus.count('A') >= 3:
        checkout_price -= (skus.count('A') // 3) * (3 * item_prices['A'] - 130)
    if skus.count('B') >= 2:
        checkout_price -= (skus.count('B') // 2) * (2 * item_prices['B'] - 45)
    return checkout_price
