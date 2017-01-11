def get_name(name):
    def my_name():
        return "Hello " + name

    return my_name


name = get_name("Umesh")
print(name())
