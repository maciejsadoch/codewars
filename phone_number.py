def create_phone_number(n):
    num_str = "".join([str(elem) for elem in n])
    return f"({num_str[0:3]}) {num_str[3:6]}-{num_str[6:10]}"
