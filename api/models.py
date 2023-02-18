from pydantic import BaseModel
from typing import Union


class CaliforniaHouse(BaseModel):
    MedInc : float
    HouseAge : float
    AveRooms : float
    AveBedrms : float
    Population : float
    AveOccup : float
    Latitude : float
    Longitude : float

# {
#     "MedInc":1111.0,
#     "HouseAge" : 11.0,
#     "AveRooms" : 11.0,
#     "AveBedrms" : 11.0,
#     "Population" : 11.0,
#     "AveOccup" : 11.0,
#     "Latitude" : 11.0,
#     "Longitude" : 11.0
# }