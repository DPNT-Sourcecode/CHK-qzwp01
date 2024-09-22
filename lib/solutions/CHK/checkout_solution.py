

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {'A':50,'B':30,'C':20,'D':15, 'E':40}
    special_offers = {
        'A': [(5, 200), (3,130)],
        'B': [(2,45)],
        'E': [(2,0)]
    }
    checkout_price = 0
    sku_counts = {}

    for sku in skus:
        if sku not in item_prices:
            return -1
        sku_counts[sku] = sku_counts.get(sku, 0) + 1

    for sku, count in sku_counts.items():
        if sku in special_offers:
            for offer_count, offer_price in special_offers[sku]:
                while count >= offer_count:
                    checkout_price += offer_price
                    count -= offer_count
        checkout_price += count * item_prices[sku]


    if 'E' in sku_counts and 'B' in sku_counts:
        count_E = sku_counts['E']
        free_B_count = count_E // 2
        sku_counts['B'] -= free_B_count
        if sku_counts['B'] < 0:
            sku_counts['B'] = 0

    if 'B' in sku_counts:
        count_B = sku_counts['B']
        if count_B >= 2:
            offer_count, offer_price = special_offers['B'][0]
            while count_B >=2:
                checkout_price +=offer_price
                count_B -= offer_count
        checkout_price += count_B * item_prices['B']

    return checkout_price
