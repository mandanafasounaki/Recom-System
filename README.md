# Recommendation System

In this project a related products recommendation system is implemented.
The recommender is a Gensim Word2Vec model, trained on the items bought together in one session. 
The API which retrieves products in the cart as request parameters and returns recommended products (top ten) with scores is created using Starlette toolkit.

To run the API, install the requirements;

```
pip install requirements.txt
```
Select one of the cart*.json in carts folder as the input cart. 

```
python main.py
```

Send the selected cart as request to http://127.0.0.1:8000/product/recommends. The list of the recommended products will be receieved.

  
## Notebooks

notebooks folder contains "Word2Vec.ipynb" for trainig the model, "recomm_notebook.ipynb" for creating a random list of products and getting the recommendations, "evaluate.ipynb" for evaluating the method
using Mean Average Precision at K (MAP@K).
