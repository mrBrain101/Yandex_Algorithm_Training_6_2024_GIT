import random

def generate_inputs(num_inputs):
    inputs = []
    for _ in range(num_inputs):
        x1 = random.randint(-99, 98)
        y1 = random.randint(-99, 98)
        x2 = random.randint(x1 + 1, 99)
        y2 = random.randint(y1 + 1, 99)
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        while (x >= x1 and x <= x2 and y >= y1 and y <= y2) and\
              (x == x1 or x == x2 or y == y1 or y == y2):
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
        inputs.append(f"{x1} {y1} {x2} {y2} {x} {y}")
    return inputs

num_inputs = 100
inputs = generate_inputs(num_inputs)

with open("input_test.txt", "w") as file:
    file.write("\n".join(inputs))