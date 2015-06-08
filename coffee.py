
class Coffeeshop(object):
    def __init__(self, name):
        self.name = name
        self.menu = []

    def greeting(self, menu):
        print "Welcome to Mole Rat's coffee house! How can I help you?"
        raw_input()
        print "We have..."
        raw_input()
        for drink in self.menu:
            print drink    #shows drinks they have
        raw_input()

    def order_drink(self, drink):
        print "I will take {}.".format(drink.drink_name)
        raw_input()
        print "${}, please.".format(drink.drink_price)
        raw_input()
        while True:
            your_name = raw_input("What is your name?")
            if len(your_name) > 0:
                print "Ok Just a second!"
                break
            else:
                print "What?"    #asks name until user inputs something

        raw_input()
        print "{}! This is your {}.".format(your_name, self.name)
            #give the drink, calling your name
        raw_input()


class Drink(object):
    def __init__(self, name, price, coffeeshop, calories=0):
        self.drink_name = name
        self.drink_price = price
        self.calories = calories
        coffeeshop.menu.append(self.drink_name)

    def display_calories(self):
        print "This has {} calories..".format(self.calories)
        raw_input()


class Additive(object):
    def __init__(self, name, sweetness, calories=0):
        self.name = name
        self.calories = calories
        self.sweetness = sweetness

    def add_calories(self, drink):
        total_calories = drink.calories + self.calories
        print 'The total calories are {}..'.format(total_calories)
        # culculates total calorie intake and gives feedback
        raw_input()
        if total_calories <= 30:
            print "It's totally guilty free!"
            raw_input()
        elif total_calories >= 200:
            print "Shoot it was too much.. I need to go to gym."
            raw_input()
        else:
            print "It's not bad."
            raw_input()

    def how_sweet(self):
        print "This is {} sweet.".format(self.sweetness)
        raw_input()

    def display_calories(self):
        print "I added {} calories".format(self.calories)
        raw_input()

    def display_flavor(self):
        print "Smells {}.".format(self.name)
        raw_input()


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
    cinnamon = Additive('cinnamon', calories=2, sweetness='kind of')
    brown_sugar = Additive('brown sugar', '30', 'pretty')
    honey = Additive('honey', calories=20, sweetness='kind of')

    #let's go to this coffeeshop
    nmr_coffee.greeting(nmr_coffee.menu)
    nmr_coffee.order_drink(mocha)
    mocha.display_calories()
    honey.display_flavor()
    honey.how_sweet()
    honey.display_calories()
    honey.add_calories(mocha)

    #comes to the coffeeshop again
    print "Next day"
    raw_input()

    nmr_coffee.greeting(nmr_coffee.menu)
    nmr_coffee.order_drink(caramel_frappuchino)
    caramel_frappuchino.display_calories()
    cinnamon.display_flavor()
    cinnamon.how_sweet()
    cinnamon.display_calories()
    cinnamon.add_calories(caramel_frappuchino)

