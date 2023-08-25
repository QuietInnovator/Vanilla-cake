class CakeRecipe:
    def __init__(self):
        self.dry_ingredients = {
            "all-purpose flour": "2 1/2 cups",
            "baking powder": "2 1/2 tsp",
            "salt": "1/2 tsp"
        }
        
        self.wet_ingredients = {
            "unsalted butter": "1 1/4 cups, softened",
            "granulated sugar": "2 cups",
            "large eggs": "4",
            "pure vanilla extract": "1 tsp",
            "whole milk": "1 cup"
        }

    def welcome(self):
        print("Welcome to the Classic Vanilla Cake Recipe!")
        print("\nDry Ingredients:")
        for ingredient, quantity in self.dry_ingredients.items():
            print(f"- {ingredient}: {quantity}")
        
        print("\nWet Ingredients:")
        for ingredient, quantity in self.wet_ingredients.items():
            print(f"- {ingredient}: {quantity}")
        print("\nLet's start baking!")
        input("Press return to continue...")

    def preparation(self):
        print("Preheat your oven to 350°F (175°C).")
        print("Grease two 9-inch round cake pans or line them with parchment paper.\n")
        input("Press return to continue...")

    def mix_dry_ingredients(self):
        print("In a medium-sized bowl, whisk together the flour, baking powder, and salt. Set aside.\n")
        input("Press return to continue...")

    def cream_butter_and_sugar(self):
        print("In a large bowl, using an electric mixer, cream together the softened butter and sugar until the mixture is light and fluffy.\n")
        input("Press return to continue...")

    def add_eggs_and_vanilla(self):
        print("Beat in the eggs one at a time, ensuring each egg is fully incorporated before adding the next.")
        print("Stir in the vanilla extract.\n")
        input("Press return to continue...")

    def alternate_dry_and_milk(self):
        print("Begin by adding a third of the dry ingredient mixture to the butter and sugar mixture, mixing until just combined.")
        print("Pour in half of the milk, mixing again until just combined.")
        print("Repeat this process, ending with the dry ingredients.\n")
        input("Press return to continue...")

    def pour_and_bake(self):
        print("Evenly distribute the cake batter between the two prepared cake pans.")
        print("Place in the preheated oven and bake for 25-30 minutes, or until a toothpick inserted into the center of the cakes comes out clean.\n")
        input("Press return to continue...")

    def cool_and_decorate(self):
        print("Once baked, remove the cakes from the oven and allow them to cool in the pans for about 10 minutes.")
        print("Afterward, transfer the cakes onto a wire rack to cool completely.")
        print("Once cooled, you can frost and decorate as desired.\n")
        input("Press return to continue...")

    def make_cake(self):
        self.welcome()
        self.preparation()
        self.mix_dry_ingredients()
        self.cream_butter_and_sugar()
        self.add_eggs_and_vanilla()
        self.alternate_dry_and_milk()
        self.pour_and_bake()
        self.cool_and_decorate()


# To make the cake:
cake = CakeRecipe()
cake.make_cake()
