

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {'A':50,'B':30,'C':20,'D':15, 'E':40}
    special_offers = {
        'A': [(5, 200), (3,130)],
        'B': [(2,45)]
    }
    checkout_price = 0
    sku_counts = {}

    for sku in skus:
        if sku not in item_prices:
            return -1
        sku_counts[sku] = sku_counts.get(sku, 0) + 1

    if 'E' in sku_counts:
        free_B_count = sku_counts['E'] // 2
        if 'B' in sku_counts:
            sku_counts['B'] = max(0, sku_counts['B'] - free_B_count)
        else:
            sku_counts['B'] = 0

    for sku, count in sku_counts.items():
        if sku in special_offers:
            for offer_count, offer_price in sorted(special_offers[sku], reverse=True):
                while count >= offer_count:
                    checkout_price += offer_price
                    count -= offer_count
        checkout_price += count * item_prices[sku]


    return checkout_price
