

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]


def get_all_color_combinations():
    combinations = []
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            combinations.append(f"{major} {minor}")
    return combinations

