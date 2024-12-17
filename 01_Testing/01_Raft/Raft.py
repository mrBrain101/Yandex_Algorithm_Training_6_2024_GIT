def find_direction_to_closest_point(input : str) -> str:
    sw_x, sw_y, ne_x, ne_y, x, y = map(int, input.split())

    if x < sw_x:
        return 'W' if y < sw_y else 'NW' if y > ne_y else 'SW'
    elif x > ne_x:
        return 'E' if y < ne_y else 'SE' if y > sw_y else 'NE'
    else:
        return 'N' if y > ne_y else 'S' if y < sw_y else 'W' if x < sw_x else 'E'
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.read().strip()

    with open("output.txt", "w") as file:
        file.write(find_direction_to_closest_point(input))