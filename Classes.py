class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('Red')
cookie_two = Cookie('Green')

cookie_color = (cookie_one.get_color())
print(cookie_color)
address_one = id(cookie_color)
print(address_one)
cookie_one_change = (cookie_one.set_color('Yellow'))
print(cookie_one_change)
change_address = id(cookie_one_change)
print(change_address)
