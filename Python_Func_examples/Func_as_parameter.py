def get_name(name):
    return "Hello " + name


def my_name(func):
    return func("Umesh")


print(my_name(get_name))
