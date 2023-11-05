from fastapi import FastAPI
from src.controller.Dolar import Predicciones, Clear, GetDatos
from src.controller.predicciones_diarias import get_data_prediccion
import threading
app = FastAPI()

data_thread = threading.Thread(target=get_data_prediccion)
data_thread.daemon = True
data_thread.start()

@app.get("/predicciones")
def read_root():
    data = GetDatos()
    df = Clear(data)
    return Predicciones(df)