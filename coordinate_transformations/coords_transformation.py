import numpy as np

# Convertir de coordenadas ecuatoriales a coordenadas cartesianas (con distancia)
def ecuatorial_a_cartesiana_con_distancia(alpha, delta, distancia):
    x = distancia * np.cos(np.radians(delta)) * np.cos(np.radians(alpha))
    y = distancia * np.cos(np.radians(delta)) * np.sin(np.radians(alpha))
    z = distancia * np.sin(np.radians(delta))
    return np.array([x, y, z])

# Convertir de coordenadas cartesianas a coordenadas galácticas
def cartesianas_a_galacticas(coord_cart):
    # Ajuste de posición del Sol (aproximado)
    alpha0 = 266.4  # Ascensión recta del centro galáctico en grados
    delta0 = -28.9  # Declinación del centro galáctico en grados

    # Convertir ángulos a radianes
    alpha0_rad = np.radians(alpha0)
    delta0_rad = np.radians(delta0)

    # Crear matriz de rotación para la transformación de coordenadas
    R = np.array([
        [-np.sin(alpha0_rad), np.cos(alpha0_rad), 0],
        [-np.sin(delta0_rad) * np.cos(alpha0_rad), -np.sin(delta0_rad) * np.sin(alpha0_rad), np.cos(delta0_rad)],
        [np.cos(delta0_rad) * np.cos(alpha0_rad), np.cos(delta0_rad) * np.sin(alpha0_rad), np.sin(delta0_rad)]
    ])
    # Aplicar la rotación

    coord_galacticas = np.dot(R, coord_cart)
    x_g, y_g, z_g = coord_galacticas

    # Calcular longitud y latitud galáctica
    l = np.degrees(np.arctan2(y_g, x_g)) + 180  # Longitud galáctica
    b = np.degrees(np.arcsin(z_g / np.linalg.norm(coord_galacticas)))  # Latitud galáctica
    
    return l, b

# Convertir de coordenadas galácticas a cartesianas
def galacticas_a_cartesianas(l, b, distancia):
    # Convertir a radianes
    l_rad = np.radians(l)
    b_rad = np.radians(b)

    x = distancia * np.cos(b_rad) * np.cos(l_rad)
    y = distancia * np.cos(b_rad) * np.sin(l_rad)
    z = distancia * np.sin(b_rad)
    return np.array([x, y, z])

# Convertir de coordenadas cartesianas a coordenadas ecuatoriales
def cartesiana_a_ecuatorial_con_distancia(coord_cart):
    x, y, z = coord_cart
    distancia = np.sqrt(x**2 + y**2 + z**2)
    alpha = np.degrees(np.arctan2(y, x))
    delta = np.degrees(np.arcsin(z / distancia))
    return alpha, delta, distancia

# Aplicar matriz de rotación en 3D
def rotacion_3d(vector, angulo, eje):
    angulo = np.radians(angulo)
    if eje == 'x':
        matriz_rotacion = np.array([[1, 0, 0],
                                    [0, np.cos(angulo), -np.sin(angulo)],
                                    [0, np.sin(angulo), np.cos(angulo)]])
    elif eje == 'y':
        matriz_rotacion = np.array([[np.cos(angulo), 0, np.sin(angulo)],
                                    [0, 1, 0],
                                    [-np.sin(angulo), 0, np.cos(angulo)]])
    elif eje == 'z':
        matriz_rotacion = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                                    [np.sin(angulo), np.cos(angulo), 0],
                                    [0, 0, 1]])
    return np.dot(matriz_rotacion, vector)

# Transformar coordenadas teniendo en cuenta el desplazamiento
def transformar_coordenadas_con_paralaje(alpha, delta, distancia, delta_alpha, delta_delta, desplazamiento):
    # Paso 1: Convertir coordenadas ecuatoriales a cartesianas
    coord_cartesianas = ecuatorial_a_cartesiana_con_distancia(alpha, delta, distancia)

    # Paso 2: Aplicar rotaciones para ajustar el nuevo origen
    coord_rotada_z = rotacion_3d(coord_cartesianas, delta_alpha, 'z')
    coord_rotada = rotacion_3d(coord_rotada_z, delta_delta, 'y')

    # Paso 3: Convertir a coordenadas galácticas
    l, b = cartesianas_a_galacticas(coord_rotada)

    # Paso 4: Agregar el vector de desplazamiento (traslación en 3D)
    coord_trasladada = coord_rotada + np.array(desplazamiento)

    # Paso 5: Convertir de nuevo a coordenadas cartesianas galácticas
    distancia_nueva = np.linalg.norm(coord_trasladada)
    coord_final = galacticas_a_cartesianas(l, b, distancia_nueva)

    # Paso 6: Convertir de coordenadas cartesianas de vuelta a ecuatoriales
    alpha_nueva, delta_nueva, _ = cartesiana_a_ecuatorial_con_distancia(coord_final)
    
    return alpha_nueva, delta_nueva, distancia_nueva

