# main.py

# Importamos las funciones necesarias de nuestros módulos modularizados
from color_code_system.color_converter import (
    get_color_from_pair_number,
    get_pair_number_from_color,
    generate_reference_manual,
    color_pair_to_string # Aunque no se use directamente en este main, es parte de la lógica
)
from color_code_system.color_constants import MAJOR_COLORS, MINOR_COLORS

def run_tests():
    """
    Ejecuta las pruebas unitarias.
    Nota: Lo ideal es usar 'python -m unittest color_code_system/test_color_converter.py'
    o simplemente 'python color_code_system/test_color_converter.py' desde la terminal.
    Esta función es solo para demostrar que las pruebas existen.
    """
    print("\n--- Ejecutando Pruebas (simulación de llamada) ---")
    print("Para ejecutar las pruebas completas, usa el comando:")
    print("python -m unittest color_code_system/test_color_converter.py")
    # Si quieres ejecutar los tests directamente desde aquí, tendrías que importar unittest
    # import unittest
    # from color_code_system.test_color_converter import TestColorConverter
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestColorConverter))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)


def demonstrate_color_conversion():
    """
    Demuestra el uso de las funciones de conversión de colores.
    """
    print("\n--- Demostración de Conversión de Colores ---")

    # Ejemplo de número a par de colores
    test_number = 4
    major, minor = get_color_from_pair_number(test_number)
    print(f"El par número {test_number} es: {color_pair_to_string(major, minor)}")

    test_number = 5
    major, minor = get_color_from_pair_number(test_number)
    print(f"El par número {test_number} es: {color_pair_to_string(major, minor)}")

    # Ejemplo de par de colores a número
    major_color_test = 'Black'
    minor_color_test = 'Orange'
    pair_num = get_pair_number_from_color(major_color_test, minor_color_test)
    print(f"El par '{major_color_test} {minor_color_test}' es el número: {pair_num}")

    major_color_test = 'Violet'
    minor_color_test = 'Slate'
    pair_num = get_pair_number_from_color(major_color_test, minor_color_test)
    print(f"El par '{major_color_test} {minor_color_test}' es el número: {pair_num}")

    major_color_test = 'Red'
    minor_color_test = 'Orange'
    pair_num = get_pair_number_from_color(major_color_test, minor_color_test)
    print(f"El par '{major_color_test} {minor_color_test}' es el número: {pair_num}")


def generate_and_display_manual():
    """
    Genera y muestra el manual de referencia de colores.
    """
    print("\n--- Generando y Mostrando Manual de Referencia ---")
    manual_output = generate_reference_manual()
    print(manual_output)

    # Opcional: Guardar el manual en un archivo
    try:
        with open("color_code_manual.txt", "w", encoding="utf-8") as f:
            f.write(manual_output)
        print("\nManual de referencia guardado en 'color_code_manual.txt'")
    except IOError as e:
        print(f"Error al guardar el manual: {e}")


if __name__ == '__main__':
    print("Iniciando la aplicación de codificación de colores...")

    # Ejecutar las demostraciones y funcionalidades
    demonstrate_color_conversion()
    generate_and_display_manual()
    run_tests() # Mostrar cómo se ejecutarían las pruebas

    print("\nAplicación finalizada. ¡Done :)!")
