import random
import sqlite3
import numpy as np
import json
import pandas as pd

def load_random(count=5):
    '''
    Loads a list of random items
    '''
    ##load the validation metadata
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM validation")
    val_data = c.fetchall()
    
    ##create a random length list from random items    
#     count = random.choice(range(1,10))
    _count = count
    ids = []
    temp2 = []
    rows = []
#     _dict = {'prodcutid':[], 'name':[], 'subcategory': [], 'category':[]}
    for i in range(_count):
        temp = val_data[random.choice(range(len(val_data)))]
        ids.append(temp)
    for _id in ids:
        c.execute("SELECT productid, brand, category, subcategory, name FROM Meta WHERE productid=?", _id)
        fetched = c.fetchall() 
        for row in fetched:
            rows.append(row)

    df_all = pd.DataFrame(rows, columns = ['productid', 'brand', 'category', 'subcategory', 'name'])
    df_all.reset_index()
    return df_all
