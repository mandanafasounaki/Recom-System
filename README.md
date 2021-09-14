# Recommendation System

In this project a related products recommendation system is implemented.
The recommender is a Gensim Word2Vec model, trained on the items bought together in one session. 
The API which retrieves products in the cart as request parameters and returns recommended top ten products with scores is created using Starlette toolkit.

To run the API, install the requirements;

```
pip install -r requirements.txt
```
For providing the user cart, you can either select one of the "cart*.json" files in carts folder or create a cart of randomly selected items with ```create_random_cart(count, c_name)``` function in create_cart.py, where `count` is the number of items and `c_name` is the name of the file. This function creates a json file in the current directory.   

```
python main.py
```

Send the selected cart as request to http://127.0.0.1:8000/product/recommends. The list of the recommended products will be receieved.

  
## Notebooks

notebooks folder contains "Word2Vec.ipynb" for trainig the model, "recomm_notebook.ipynb" for creating a random list of products and getting the recommendations, "evaluate.ipynb" for evaluating the method
using Mean Average Precision at K (MAP@K).
