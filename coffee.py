
class Coffeeshop(object):
    def __init__(self, name):
        self.name = name
        self.menu = []

    def greeting(self, menu):
        print "Welcome to Mole Rat's coffee house! How can I help you?"
        print "We have..."
        for drink in self.menu:
            print drink    #shows drinks they have

    def order_drink(self, drink):
        print "I will take {}.".format(drink.drink_name)
        print "${}, please.".format(drink.drink_price)
        raw_input()
        while True:
            your_name = raw_input("What is your name? ")
            if len(your_name) > 0:
                print "Ok Just a second!"
                break
            else:
                print "What?"    #asks name until user inputs something

        raw_input()
        print "{}! This is your {}.".format(your_name, drink.drink_name)
            #give the drink, calling your name


class Drink(object):
    def __init__(self, name, price, coffeeshop, calories=0):
        self.drink_name = name
        self.drink_price = price
        self.calories = calories
        coffeeshop.menu.append(self.drink_name)
        self.additives = []

    def __str__(self):
        additive_string = ""
        for additive in self.additives:
            additive_string += str(additive)
        return "I got {} for ${}. {}.".format(self.drink_name, self.drink_price, additive_string)
        
    def display_calories(self):
        print "This has {} calories..".format(self.calories)
        if self.calories <= 30:
            print "It's totally guilty free!"
        elif self.calories >= 200:
            print "Shoot it was too much.. I need to go to gym."
        else:
            print "It's not bad."

    def add(self, additive):
        self.additives.append(additive)
        self.calories += additive.calories


class Additive(object):
    def __init__(self, name, sweetness, calories=0):
        self.name = name
        self.calories = calories
        self.sweetness = sweetness

    def __str__(self):
        return "This is {} sweet and smells {}".format(self.sweetness, self.name)


if __name__ == '__main__':

    nmr_coffee = Coffeeshop("Mole Rat's Coffee")

    #these are drinks the coffee shop have
    americano = Drink('Americano', '1.80', nmr_coffee)
    earl_grey = Drink('Earl Grey', '2', nmr_coffee)
    green_tea = Drink('Green Tea', '2', nmr_coffee)
    drip_coffee = Drink('Drip Coffee', '1.80', nmr_coffee)
    mocha = Drink('Mocha', '1.75', nmr_coffee, calories=90)
    caramel_frappuchino = Drink('Caramel Frappuchino', '4.99', nmr_coffee, calories=400)
    lemonade = Drink('Lemonade', '3', nmr_coffee, calories=150)

    #additives they have
    cinnamon = Additive('cinnamon', 'kind of', 2)
    brown_sugar = Additive('brown sugar', 'pretty', 30)
    honey = Additive('honey', 'kind of', 20)

    #let's go to this coffeeshop
    nmr_coffee.greeting(nmr_coffee.menu)
    raw_input()
    nmr_coffee.order_drink(mocha)
    raw_input()
    mocha.add(honey)
    raw_input()
    mocha.display_calories()
    raw_input()
    print mocha
    print honey

    #comes to the coffeeshop again
    print "Next day"
    raw_input()

    nmr_coffee.greeting(nmr_coffee.menu)
    raw_input()
    nmr_coffee.order_drink(caramel_frappuchino)
    raw_input()
    caramel_frappuchino.add(cinnamon)
    raw_input()
    caramel_frappuchino.display_calories()
    raw_input()
    print cinnamon