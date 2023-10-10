import pandas as pd
#vizualización de como carga el excel desde pandas
#PIB
def CargaDeDatoPIB():
    ruta = 'PIB.xlsx'
    df = pd.read_excel(ruta)
    primera_fila = df.iloc[0,:]
    print(primera_fila)
#CargaDeDatoPIB(); 
#Inflación     
def CargaDatosInflacion():
    ruta = 'INFLACION.xlsx'
    df = pd.read_excel(ruta)
    print(df)   
#CargaDatosInflacion();
#La deuda
def CargarDatosDeuda():
    ruta = 'DEUDA.xlsx'
    df = pd.read_excel(ruta)
    print(df)
#CargarDatosDeuda();    

def CargarDatosDesempleo():
    ruta = 'DESEMPLEO.xlsx'
    df = pd.read_excel(ruta)
    print(df)
#CargarDatosDesempleo();    
    