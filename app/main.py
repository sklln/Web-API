from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from model import dt_classifier

app = FastAPI(
    title="LGC Covid Symptom Check",
    description="This is an initial model to check symptoms of Covid-19 \n "
                "Symptoms are rated be severity from No (0), Common (1), Mild (2), Sometimes (3), Rare (4)",
    version="0.0.1"
)

class Item(BaseModel):
    aches_pains: float
    diarrhea: float
    fatigue: float
    fever_chills: float
    headaches: float
    running_nose: float
    breathless: float
    sneezing: float
    sore_throat: float


@app.get("/prediction/{sent}", tags=['Data Science Test Models'])
async def read_item():
    return {'success': "successfully returned"}


#@app.post("/items/", response_model=Item, tags=['Data Science Test Models'])
@app.post("/items/", tags=['Data Science Test Models'])
async def created_item(item: Item):
    json_compatible_item = jsonable_encoder(item)
    d = {'age':item.Age, 'gender':item.Gender}
    return item


@app.post("/api/", tags=['Data Science Test Models'])
async def predict_item(item: Item):
    #json_compatible_item = jsonable_encoder(item)
    predicted_labels = dt_classifier.get_prediction(item)
    return predicted_labels
