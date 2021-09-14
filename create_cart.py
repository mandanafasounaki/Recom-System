from load_data import load_random_c
import json

def create_random_cart(count, name):
    
    item_list = load_random_c(count)
    
    dict_items = item_list.to_dict()
    
    with open(name + '.json', 'w') as f:
        json.dump(d, f)
    
    