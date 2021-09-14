from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.endpoints import HTTPEndpoint
import json
from recommend import recomm_json
import uvicorn

class Recommend(HTTPEndpoint):
    
    async def post(self, request):
        cart = await request.body()
           
        ##Get the recommendation list
        recoms = recomm_json(json.loads(cart.decode('utf-8')), 'models/word2vec_noneg_cbow.model')
        recom_dict = recoms.to_dict('records')
        
        return JSONResponse(recom_dict)
#           return JSONResponse({'groceryList' : cart, 'recommendations':recom_dict})


app = Starlette(debug=True, routes=[
    Route('/product/recommends', Recommend),
])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)