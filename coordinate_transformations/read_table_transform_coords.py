import numpy as np
from astropy.io import votable
from astropy.table import Table

from coordinate_transformations.coords_transformation import *
from coordinate_transformations.gaia_astropy_to_simbad import *
from gaia_query import *

# Suponiendo que ya tienes las funciones definidas, como:
# ecuatorial_a_cartesiana_con_distancia, cartesianas_a_galacticas, galacticas_a_cartesianas, cartesiana_a_ecuatorial_con_distancia,
# rotacion_3d y transformar_coordenadas_con_paralaje.

# Aquí iría la definición de las funciones previamente mencionadas

def procesar_votable(archivo_votable, delta_alpha, delta_delta, desplazamiento):
    # Leer el archivo VOTable
    votable_data = votable.parse(archivo_votable)
    table = votable_data.get_first_table().to_table()

    # Crear listas para almacenar los resultados
    ra_new = []
    dec_new = []
    distance = []

    # Procesar cada fila en la table
    for fila in table:
        alpha = fila['ra']  # Ascensión recta
        delta = fila['dec']  # Declinación
        distancia = 1 / (fila['parallax'] * 0.001) if fila['parallax'] > 0 else np.inf  # Convertir paralaje a distancia (en parsecs)

        # Transformar coordenadas
        alpha_new, delta_new, distancia_new = transformar_coordenadas_con_paralaje(
            alpha, delta, distancia, delta_alpha, delta_delta, desplazamiento
        )

        # Guardar los resultados en las listas
        ra_new.append(alpha_new)
        dec_new.append(delta_new)
        distance.append(distancia_new)

    # Crear new table con los resultados
    new_table = Table()
    new_table['SOURCE_ID'] = table['SOURCE_ID']
    new_table['ra_new'] = ra_new
    new_table['dec_new'] = dec_new
    new_table['distance'] = distance
    new_table['phot_g_mean_mag'] = table['phot_g_mean_mag']

    # Guardar la new table en un archivo VOTable
    new_table.write('gaia_simbad_new.vot', format='votable', overwrite=True)

    return new_table

# Parámetros de desplazamiento y rotación
desplazamiento_alpha = 289.6579478868345  # Desplazamiento en ascensión recta (grados)
desplazamiento_delta = 49.56965248175413    # Desplazamiento en declinación (grados)
desplazamiento_espacial = [0.5, -0.2, 0.3]  # Desplazamiento en el espacio (x, y, z)

# Generar y procesar el VOTable
transf_astropy_to_simbad()
resultados = procesar_votable('gaia_simbad.xml', desplazamiento_alpha, desplazamiento_delta, desplazamiento_espacial)
