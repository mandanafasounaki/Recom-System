from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
import json
from recommend import recomm_json


class Homepage(HTTPEndpoint):
    
    async def post(self, request):
        cart = await request.body()
        with open('user_cart.json', 'w') as f:
            json.dump(cart.decode('utf-8'), f)
           
        ##Get the recommendation list
        recoms = recomm_json('user_cart.json', 'word2vec_noneg_cbow.model')
        recom_dict = recoms.to_dict('recoms')
        
        return JSONResponse(recom_dict)
#           return JSONResponse({'groceryList' : cart, 'recommendations':recom_dict})


app = Starlette(debug=True, routes=[
    Route('/', Homepage),
])
