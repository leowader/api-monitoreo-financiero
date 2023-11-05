from fastapi import FastAPI
from src.controller.Dolar import Predicciones, Clear, GetDatos

app = FastAPI()


@app.get("/predicciones")
def read_root():
    data = GetDatos()
    df = Clear(data)
    return Predicciones(df)