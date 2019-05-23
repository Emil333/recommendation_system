import user_pref
import product_pref

weights = []
sorted_products = {}


def set_item_weight(product_id=str):
    if product_id in sorted_products:
        item_weight = sorted_products[product_id] + 10
        return item_weight
    else:
        return 10


def user_pref_present(item, product):
    if item == 'preferredSize':
        available_sizes = product['availableSize']
        for pref_size in user_pref.preferences['preferredSize']:
            if pref_size in available_sizes:
                return True
    elif item == 'preferredColor':
        available_colors = product['availableColor']
        for pref_color in user_pref.preferences['preferredColor']:
            if pref_color in available_colors:
                return True
    elif item == 'preferredStyle':
        product_feature = product['productfeature']
        for style in user_pref.preferences['preferredStyle']:
            ocassion = (str(product_feature[2]).split(":")[1]).strip()
            if ocassion in style:
                return True



def get_recommended_product():
    max_discount_id = ''
    max_discount = 0
    for product in product_pref.products:
        id = product['productId']
        for item in weights:
            if user_pref_present(item, product):
                item_weight = set_item_weight(id)
                sorted_products[id] = item_weight

        curr_product_discount = (str(product['discountPer']).split('%'))[0]
        curr_product_discount = int(curr_product_discount)
        if curr_product_discount > max_discount:
            max_discount = curr_product_discount
            max_discount_id = id

    discount_weight = set_item_weight(max_discount_id)
    sorted_products[max_discount_id] = discount_weight
    return sorted_products