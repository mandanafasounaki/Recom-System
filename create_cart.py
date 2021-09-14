from load_data import load_random_c
import json

def create_random_cart(count, c_name):
    
    item_list = load_random_c(count)
    
    dict_items = item_list.to_dict()
    
    with open(c_name + '.json', 'w') as f:
        json.dump(dict_items, f)
        print("%s.json is created." % (c_name))