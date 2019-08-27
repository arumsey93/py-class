class Pizza:

    def __init__(self):
        self.size = 0
        self.style = ""
        self.new_topping = []

    def add_topping(self, topping):
        self.new_topping.append(topping)

    def print_order(self):
        space = " and "
        new_string = f"I would like a {self.size}-inch, {self.style} pizza"
        if self.new_topping:
            new_string += f" with {space.join(self.new_topping)}"
        print(new_string)





meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()
