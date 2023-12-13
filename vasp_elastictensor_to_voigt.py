def read_elastic_tensor(outcar_file):
    """
    Reads the elastic tensor from a VASP OUTCAR file and converts it to Voigt format in GPa.
    """
    with open(outcar_file, 'r') as file:
        lines = file.readlines()

    # Find the elastic tensor in the OUTCAR file
    start = None
    for i, line in enumerate(lines):
        if 'TOTAL ELASTIC MODULI (kBar)' in line:
            start = i + 3
            break

    if start is None:
        raise ValueError("Elastic tensor not found in OUTCAR file.")

    # Extract the elastic tensor and convert to GPa
    tensor = []
    for i in range(start, start + 6):
        values = lines[i].split()
        tensor.append([float(val) * 0.1 for val in values[1:7]])  # Convert from kBar to GPa

    return tensor

def convert_to_voigt(tensor):
    """
    Converts the elastic tensor to Voigt format.
    """
    # Voigt notation conversion
    voigt_tensor = [
        [tensor[0][0], tensor[1][1], tensor[2][2], tensor[3][3], tensor[4][4], tensor[5][5]],
        [tensor[1][0], tensor[1][1], tensor[1][2], tensor[1][3], tensor[1][4], tensor[1][5]],
        [tensor[2][0], tensor[2][1], tensor[2][2], tensor[2][3], tensor[2][4], tensor[2][5]],
        [tensor[3][0], tensor[3][1], tensor[3][2], tensor[3][3], tensor[3][4], tensor[3][5]],
        [tensor[4][0], tensor[4][1], tensor[4][2], tensor[4][3], tensor[4][4], tensor[4][5]],
        [tensor[5][0], tensor[5][1], tensor[5][2], tensor[5][3], tensor[5][4], tensor[5][5]]
    ]

    return voigt_tensor

def main():
    outcar_file = 'OUTCAR'  # Path to your OUTCAR file
    tensor = read_elastic_tensor(outcar_file)
    voigt_tensor = convert_to_voigt(tensor)

    print("#Elastic Tensor in Voigt Format (GPa):")
    for row in voigt_tensor:
        print(' '.join(f'{val:10.3f}' for val in row))

if __name__ == "__main__":
    main()
