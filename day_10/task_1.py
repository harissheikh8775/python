def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()

    full_name = f_name + " " + l_name
    return full_name


output = format_name(f_name="haris", l_name="sheikh")
print(output)
