# color_code_system/color_converter.py

from .color_constants import MAJOR_COLORS, MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
  """
  Convierte un par de colores en una cadena de texto.
  Ej: ('White', 'Brown') -> "White Brown"
  """
  return f'{major_color} {minor_color}'


def get_color_from_pair_number(pair_number):
  """
  Dada una posición de par de colores (basada en 1), devuelve los colores mayor y menor.
  Ej: 4 -> ('White', 'Brown')
  """
  if not isinstance(pair_number, int) or pair_number <= 0:
      raise ValueError("El número de par debe ser un entero positivo.")

  zero_based_pair_number = pair_number - 1
  
  num_minor_colors = len(MINOR_COLORS)
  num_major_colors = len(MAJOR_COLORS)

  major_index = zero_based_pair_number // num_minor_colors
  if major_index >= num_major_colors:
    raise IndexError(f'Índice mayor fuera de rango para el número de par {pair_number}.')
  
  minor_index = zero_based_pair_number % num_minor_colors
  if minor_index >= num_minor_colors: # Esto es redundante si `num_minor_colors` es el divisor
    raise IndexError(f'Índice menor fuera de rango para el número de par {pair_number}.')
  
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color, minor_color):
  """
  Dados un color mayor y uno menor, devuelve la posición del par de colores (basada en 1).
  Ej: ('Black', 'Orange') -> 12
  """
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise ValueError(f"Color mayor '{major_color}' no encontrado en la lista de colores principales.")
  
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise ValueError(f"Color menor '{minor_color}' no encontrado en la lista de colores secundarios.")
  
  return major_index * len(MINOR_COLORS) + minor_index + 1
