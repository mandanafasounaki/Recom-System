from gensim.models import Word2Vec
import pandas as pd
import sqlite3 
import numpy as np
import json 
import ast

def recomm(shoplist, model_path):
    '''
    Gets a list of grocery and returns recommended items
    
    Arguments:
    shoplist = DataFrame of the grocery items
    model_path = path to the model for recommendation
    
    Returns:
    The DataFrame of first ten recommendations 
    '''
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    ##load the model
    model = Word2Vec.load(model_path)

    ##find the recommendations and sort based on the scores 
    ##and select the first ten recommendations
    scores = []
    sims = []
    nrmlzd_recoms = []
    norml = []   
    allsims = []
    probs = []
    
    for _item in shoplist['productid']:
        temp_sims = model.wv.most_similar(_item)
        for s in temp_sims:
            sims.append(s)
        for_norm = []    
        for n in range(len(temp_sims)):
            probs.append(temp_sims[n][1])
            for_norm.append(temp_sims[n][1])
        ##Normalize the scores for the recommendations of each item
        norm = np.linalg.norm(for_norm)
        middle_norm = for_norm / norm
        for mn in middle_norm:
            norml.append(mn)

    for i in range(len(sims)):
        nrmlzd_recoms.append((sims[i][0], norml[i]))
        
    _sorted = sorted(nrmlzd_recoms, key=lambda x: x[1], reverse=True)
    
    
    first_ten = _sorted[:10]
    
    ##extract the meta data of recommendation list
    recomms = []
    rows = []
    for r in first_ten:
        _id = r[0]
        c.execute("SELECT * FROM Meta WHERE productid=?" ,(_id,))
        fetched = c.fetchall()
        for row in fetched:
            row += (r[1],)
            rows.append(row)
    
    df_all = pd.DataFrame(rows, columns = ['productid', 'brand', 'category', 'subcategory', 'name' , 'score'])
    df_all.reset_index()
    
    return df_all

def recomm_json(cart_path, model_path):
    '''
    Gets the list of grocery items from json file
    
    Arguments:
    shoplist = DataFrame of the grocery items
    model_path = path to the model for recommendation
    
    Returns:
    The DataFrame of first ten recommendations 
    '''
    
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    ##load the model
    model = Word2Vec.load(model_path)

    ##find the recommendations and sort based on the scores 
    ##and select the first ten recommendations
    scores = []
    sims = []
    nrmlzd_recoms = []
    norml = []   
    allsims = []
    probs = []
    
    with open(cart_path) as f:
        str_cart = json.load(f)
    
    shoplist = json.loads(str_cart)
    
    for _item in shoplist['productid'].values():
        temp_sims = model.wv.most_similar(_item)
        for s in temp_sims:
            sims.append(s)
        for_norm = []    
        for n in range(len(temp_sims)):
            probs.append(temp_sims[n][1])
            for_norm.append(temp_sims[n][1])

        norm = np.linalg.norm(for_norm)
        middle_norm = for_norm / norm
        for mn in middle_norm:
            norml.append(mn)

    for i in range(len(sims)):
        nrmlzd_recoms.append((sims[i][0], norml[i]))
        
    _sorted = sorted(nrmlzd_recoms, key=lambda x: x[1], reverse=True)
    
    
    first_ten = _sorted[:10]
    
    recomms = []
    rows = []
    for r in first_ten:
        _id = r[0]
        c.execute("SELECT * FROM Meta WHERE productid=?" ,(_id,))
        fetched = c.fetchall()
        for row in fetched:
            row += (r[1],)
            rows.append(row)

    
    df_all = pd.DataFrame(rows, columns = ['productid', 'brand', 'category', 'subcategory', 'name' , 'score'])
    df_all.reset_index()
    return df_all