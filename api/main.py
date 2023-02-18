from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from .models import CaliforniaHouse
import pickle
import numpy as np
import uvicorn

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'status_code': 200}


@app.get('/home')
async def home():
    return FileResponse('templates/index.html')    


# California Home Price Predictor
@app.post('/predict_price')
async def california_house_price(content : CaliforniaHouse):
    try:
        ## Loading Model
        regmodel = pickle.load(open('ml/regmodel.pkl', 'rb'))

        ## Loading scaler for transformation
        scaler = pickle.load(open('ml/scaler.pkl', 'rb'))
        
        # Getting form data from client
        data = [ float(x) for x in content.dict().values()]
        final_input = scaler.transform(np.array(data).reshape(1, -1))
        output = regmodel.predict(final_input)[0]

    except Exception as Error:
        print(Error)
        return {"error": str(Error)}
    return {'result': round(output,2)}

