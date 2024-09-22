

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {'A':50,'B':30,'C':120,'D':115, 'E':40}
    checkout_price = 0
    sku_counts = {}

    for sku in skus:
        if sku not in item_prices:
            return -1
        sku_counts[sku] = sku_counts.get(sku, 0) + 1

    for sku, count in sku_counts.items():
        checkout_price += count * item_prices[sku]

    if 'A' in sku_counts:
        count_A = sku_counts['A']
        checkout_price -= (count_A//5) * (5 * item_prices['A'] - 200)
        checkout_price -= (count_A//3) * (3 * item_prices['A'] - 130)

    if 'B' in sku_counts:
        count_B = sku_counts['B']
        checkout_price-= (count_B //2) * (2 * item_prices['B'] - 45)

    if 'E' in sku_counts:
        count_E = sku_counts['E']
        if count_E >= 2 and 'B' in sku_counts:
            count_B_free = count_E // 2
            sku_counts['B'] -= count_B_free
            if sku_counts['B'] < 0:
                sku_counts['B'] = 0

    if 'B' in sku_counts:
        checkout_price += sku_counts['B'] * item_prices['B']
    return checkout_price
