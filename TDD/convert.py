import sys

def inches_to_mm(inches):
    return inches * 25.4

def inches_to_cm(inches):
    return inches * 2.54

def inches_to_m(inches):
    return inches * 0.0254

def convert_length(inches, unit):
    if unit == "mm":
        return inches_to_mm(inches)
    elif unit == "cm":
        return inches_to_cm(inches)
    elif unit == "m":
        return inches_to_m(inches)
    else:
        raise ValueError("Invalid unit")

def run_tests():
    test_cases = [
        (3, "cm", 7.62),
        (56, "m", 1.4224)
    ]

    for inches, unit, expected_result in test_cases:
        result = convert_length(inches, unit)
        assert result == expected_result
        print(f"Test passed: {inches} inches = {result} {unit}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        run_tests()
    else:
        if len(sys.argv) != 4:
            print("Usage: python convert.py <inches> <unit>")
            sys.exit(1)

        inches = float(sys.argv[1])
        unit = sys.argv[2]
        result = convert_length(inches, unit)
        print(f"{result} {unit}")
