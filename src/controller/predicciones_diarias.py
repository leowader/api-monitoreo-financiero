import threading
import time
from src.controller.Dolar import GetDatos,Clear,Predicciones
def get_data_prediccion():
    while True:
        data = GetDatos()
        
        # Limpiar los datos
        df = Clear(data)
        
        # Realizar predicciones
        data = Predicciones(df)
        
        # Guardar o procesar las predicciones según sea necesario
        
        # Esperar un día antes de la próxima ejecución
        time.sleep(24 * 60 * 60)  # Espera 24 horas

data_thread = threading.Thread(target=get_data_prediccion)

# Iniciar el hilo
data_thread.start()

# El programa principal puede seguir ejecutándose aquí

# Espera a que el hilo termine (si alguna vez deseas detenerlo)
data_thread.join()        