def sort_package(width: int, height: int, length: int, mass: int) -> str:
    """
    Sorts a package into the correct stack based on its size and weight.

    Args:
        width (int): Width of the package in centimeters.
        height (int): Height of the package in centimeters.
        length (int): Length of the package in centimeters.
        mass (int): Mass of the package in kilograms.

    Returns:
        str: One of ["STANDARD", "SPECIAL", "REJECTED"] depending on package classification.
    """

    volume = width * height * length
    bulky = volume >= 1000000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    # Quick manual tests
    print(sort_package(100, 50, 20, 10))   # STANDARD
    print(sort_package(200, 50, 20, 10))   # SPECIAL
    print(sort_package(100, 100, 100, 25)) # REJECTED
    print(sort_package(200, 200, 50, 25))  # REJECTED
