def air_conditioner(troom, tcond, mode):
    """
    Simulates the air conditioner's behavior.

    Args:
        troom (float): The current temperature in the room.
        tcond (float): The desired temperature set on the air conditioner.
        mode (str): The operation mode of the air conditioner. Can be "freeze", "heat", "auto", or "fan".

    Returns:
        float: The temperature in the room after an hour.
    """
    if mode == "freeze":
        return min(troom, tcond)
    elif mode == "heat":
        return max(troom, tcond)
    elif mode == "auto":
        return tcond
    elif mode == "fan":
        return troom
    else:
        raise ValueError("Invalid mode. Must be 'freeze', 'heat', 'auto', or 'fan'.")

# Example usage:
troom = 25  # Current temperature in the room
tcond = 22  # Desired temperature set on the air conditioner
mode = "auto"  # Operation mode

result = air_conditioner(troom, tcond, mode)
print(f"The temperature in the room after an hour will be: {result:.2f}°C")
# with open('input_tests.txt', 'r') as f:
#     lines = f.readlines()
#     for l in lines[1:]:
#         troom, tcond, mode = l.strip().split()
#         print(air_conditioner(int(troom), int(tcond), mode))