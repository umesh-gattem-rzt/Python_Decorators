def get_name(name):
    def say_hello():
        return "Hello "

    my_name = say_hello() + name
    return my_name


print(get_name("Umesh"))
