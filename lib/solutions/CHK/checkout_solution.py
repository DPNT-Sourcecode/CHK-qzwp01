

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {'A':50,'B':30,'C':20,'D':15, 'E':40, 'F':10,
                   'G': 20, 'H': 10, 'I':35, 'J':60, 'K':70,
                   'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30,
                   'R':50, 'S':20, 'T':20, 'U':40, 'V':50, 'W':20,
                   'X':17, 'Y':20, 'Z':21
                   }
    special_offers = {
        'A': [(5, 200), (3,130)],
        'B': [(2,45)],
        'F': [(3, 20)],
        'H': [(10, 80), (5, 45)],
        'K': [(2,150)],
        'P':[(5, 200)],
        'Q':[(3, 80)],
        'V':[(3,130), (2, 90)]
    }

    free_offers = {
        'E': ('B', 2),
        'N': ('M', 3),
        'R': ('Q', 3),
    }

    group_discount = (['S', 'T', 'X', 'Y', 'Z'], 45, 3)
    checkout_price = 0
    sku_counts = {}

    for sku in skus:
        if sku not in item_prices:
            return -1
        sku_counts[sku] = sku_counts.get(sku, 0) + 1

    for offer_sku, (free_sku, qty_required) in free_offers.items():
        if offer_sku in sku_counts:
            free_count = sku_counts[offer_sku] // qty_required
            if free_sku in sku_counts:
                sku_counts[free_sku] = max(0, sku_counts[free_sku] - free_count)
    if 'U' in sku_counts:
        u_count = sku_counts['U']
        end_cost = u_count - (u_count // 4)
        checkout_price += end_cost * item_prices['U']
        del sku_counts['U']

    group_items = group_discount[0]
    group_price = group_discount[1]
    group_size = group_discount[2]

    group_item_count = sum(sku_counts.get(item, 0) for item in group_items)
    sets_of_three = group_item_count // group_size
    checkout_price += sets_of_three * group_price

    remaining_to_deduct = sets_of_three * group_size
    for item in group_items:
        if item in sku_counts:
            if sku_counts[item] <= remaining_to_deduct:
                remaining_to_deduct -= sku_counts[item]
                del sku_counts[item]
            else:
                sku_counts[item] -= remaining_to_deduct
                remaining_to_deduct = 0


    for sku, count in sku_counts.items():
        if sku in special_offers:
            for offer_count, offer_price in sorted(special_offers[sku], reverse=True):
                while count >= offer_count:
                    checkout_price += offer_price
                    count -= offer_count
        checkout_price += count * item_prices[sku]


    return checkout_price


