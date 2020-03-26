from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from model import dt_classifier

app = FastAPI(
    title="LGC Covid Symptom Check",
    description="This is an initial model to check symptoms of Covid-19 \n "
                "Symptoms are rated be severity from No (0), Rare (1), Sometimes (2), Often (3), Severe (4)",
    version="0.0.1"
)


# class Item(BaseModel):
#     aches_pains: float
#     cough: float
#     diarrhea: float
#     fatigue: float
#     fever_chills: float
#     headache: float
#     running_nose: float
#     breathless: float
#     sneezing: float
#     sore_throat: float


class Item(BaseModel):
    aches_pains: float
    breathlessness: float
    cough: float
    diarrhea: float
    fatigue: float
    fever: float
    headache: float
    runny_nose: float
    sneezing: float
    sore_throat: float



@app.get("/test/", tags=['Data Science Test Models'])
async def read_item():
    return {'success': "successfully returned"}


@app.post("/api/", tags=['Data Science Test Models'])
async def predict_item(item: Item):
    #json_compatible_item = jsonable_encoder(item)
    predicted_labels = dt_classifier.get_prediction_from_single_vector(item)
    return predicted_labels
