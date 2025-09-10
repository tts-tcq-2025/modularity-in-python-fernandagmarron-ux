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
    raise IndexError(f'Índice mayor fuera de rango para el número de par {pair_number}. '
                     f'El número máximo de par es {num_major_colors * num_minor_colors}.')
  
  minor_index = zero_based_pair_number % num_minor_colors
  # La siguiente verificación es redundante si `num_minor_colors` es el divisor
  # y `pair_number` ya pasó la verificación de `major_index`.
  # if minor_index >= num_minor_colors:
  #   raise IndexError(f'Índice menor fuera de rango para el número de par {pair_number}.')
  
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

# --- NUEVA FUNCIÓN ---
def generate_reference_manual():
  """
  Genera un texto formateado que actúa como manual de referencia
  para el mapeo de colores a números de par.
  """
  manual_lines = ["--- Manual de Referencia de Codificación de Colores ---"]
  manual_lines.append("Número de Par | Color Principal | Color Secundario")
  manual_lines.append("--------------------------------------------------")

  total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
  for pair_number in range(1, total_pairs + 1):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    manual_lines.append(
        f"{pair_number:<13} | {major_color:<15} | {minor_color:<16}"
    )
  manual_lines.append("--------------------------------------------------")
  manual_lines.append(f"Total de pares de colores: {total_pairs}")
  manual_lines.append("--------------------------------------------------")
  
  return "\n".join(manual_lines)
