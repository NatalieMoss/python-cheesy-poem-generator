import valid as v

def main():
    cheeses = [] # List of cheeses
    colors = [] #list of colors
    fridge = 0

    print("\nCheesy Poem Generator\n")

    # Inputs
    big_fridgename = ask_big_name()
    snack_fridgename = ask_snack_name()

    fridge = ask_fridge(big_fridgename, snack_fridgename)
    if fridge == 1:
        cheese_sonnet(cheeses)
    if fridge == 2:
        cheese_freeverse(colors,cheeses)

def ask_big_name():
    """Asks user to name their refrigerators.
    return: string, name of big fridge."""
    big_fridgename = v.get_string("By what term of affection do you refer to your big fridge? ")
    return big_fridgename

def ask_snack_name():
    """Asks user to name their snack fridge.
    return: string, name of snack fridge."""
    snack_fridgename = v.get_string("By what term of affection do you refer to your snack fridge? ")
    return snack_fridgename

def ask_fridge(big_fridgename, snack_fridgename):
    """Asks the user which fridge we are writing a poem for."""
    fridge = v.get_integer(f"\nPick your fridge. Enter 1 for {big_fridgename}, 2 for {snack_fridgename}: ")
    if fridge in [1, 2]:
        return fridge
    else:
        print(f"Invalid choice, defaulting to {big_fridgename}.")
        return 1

def cheese_sonnet(cheeses):
    """Modifies Pablo Neruda"""
    for i in range(4):
        cheese = v.get_string("Stock that cheese drawer. Enter a type of cheese: ")  # Store user input
        cheeses.append(cheese)  # Append the actual input

    print("Cheese Sonnet XI\n")
    print(f"I crave your {cheeses[0]}, your {cheeses[1]}, your {cheeses[2]}.\n"
          f"Silent and starving, I prowl through your cheese drawer.\n"
          f"Bread does not nourish me, dawn disrupts me\n"
          f"all day\n"
          f"I hunt for the liquid measure of your {cheeses[3]}.")  # Now this should work correctly


def cheese_freeverse(colors, cheeses):
    """Modifies william carlos william"""
    for i in range(2):
        color = v.get_string("Enter a favorite cheese color: ")
        colors.append(color)
    for i in range(2):
        cheese = v.get_string("Stock that cheese drawer. Enter a type of cheese: ")
        cheeses.append(cheese)

    print(f"\nthe {colors[0]} {cheeses[0]}\n ")
    print(f"so much depends\n"
          f"on the little {colors[0]} {cheeses[0]}\n"
          f"glazed with cheese water\n"
          f"beside the {colors[1]} {cheeses[1]}\n")

main()
