import logging
import datetime

now = datetime.datetime.now()
time_format = now.strftime("%Y_%m_%d")  # Por ejemplo: 2023-06-15_14-30-00
file_path = "./archivo_prueba_"+time_format+".log"
logging.basicConfig(filename = file_path , level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',filemode='a')

logging.info("Inicio del scipt")

def dividir(a, b):
    resultado = a / b
    return resultado

def realizar_operacion():
    try:

        resultado = str(dividir(10, 2))
        logging.info("El resultado de la división es: " +resultado)
    
    except Exception as e:
        logging.exception('Ocurrió un error')
        
realizar_operacion()
logging.info("Fin del scipt")