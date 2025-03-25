import cv2
import numpy as np
import os
import pandas as pd

def calcular_momentos_hu(imagen):
    # Calcular momentos centrales
    momentos = cv2.moments(imagen)
    
    # Calcular momentos de Hu
    momentos_hu = cv2.HuMoments(momentos).flatten()
    
    # Aplicar transformación logarítmica para normalización
    momentos_hu_log = np.sign(momentos_hu) * np.log(np.abs(momentos_hu))
    
    return momentos_hu_log

def procesar_imagen(imagen_path):
    # Cargar imagen en escala de grises
    imagen = cv2.imread(imagen_path, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar suavizado para reducir ruido
    imagen = cv2.GaussianBlur(imagen, (3, 3), 0)
    
    # Umbralización adaptativa
    imagen = cv2.adaptiveThreshold(imagen, 255, 
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    
    return imagen

carpeta_original = "Imagenes_binarias/"
carpeta_escalada = "Imagenes_escaladas/"

# Crear lista de imágenes originales y escaladas
archivos = [f for f in os.listdir(carpeta_original) if f.endswith(".png")]

# Tabla para almacenar resultados
resultados = []

for archivo in archivos:
    # Procesar imágenes original y escalada
    imagen_original_path = os.path.join(carpeta_original, archivo)
    imagen_escalada_path = os.path.join(carpeta_escalada, archivo)
    
    imagen_original = procesar_imagen(imagen_original_path)
    imagen_escalada = procesar_imagen(imagen_escalada_path)

    # Calcular momentos de Hu
    momentos_original = calcular_momentos_hu(imagen_original)
    momentos_escalada = calcular_momentos_hu(imagen_escalada)

    # Agregar resultados
    resultados.append([archivo] + list(momentos_original) + list(momentos_escalada))

# Crear DataFrame
columnas = (["Imagen"] + 
            [f"Hu_Original_{i+1}" for i in range(7)] + 
            [f"Hu_Escalada_{i+1}" for i in range(7)])

df = pd.DataFrame(resultados, columns=columnas)

# Calcular diferencias porcentuales
for i in range(7):
    df[f'Diferencia_{i+1}%'] = np.abs((df[f'Hu_Original_{i+1}'] - df[f'Hu_Escalada_{i+1}']) / df[f'Hu_Original_{i+1}'] * 100)

# Guardar resultados
df.to_csv("momentos_hu_invariantes.csv", index=False)
print(df)

# Estadísticas de diferencias
print("\nEstadísticas de diferencias porcentuales:")
print(df[[f'Diferencia_{i+1}%' for i in range(7)]].describe())
