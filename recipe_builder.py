from dataclasses import dataclass


def list_create(list):
    """
    creates list with user input
    :param list: user inputted list
    :return: list of ingredients
    """
    ingredients = list.split(', ')
    return sorted(ingredients)


@dataclass()
class Recipe:
    """
    name: name of recipe
    ingredients: ingredients list in recipe
    instruct: recipe description
    """
    name: str
    ingredients: list
    instruct: str


def readme(filename: str):
    """
    Read people from a file into a list of Person dataclass objects.
    :param filename: The name of the file
    :return: A list of merchants
    """
    recipes = []
    with open(filename) as f:
        for line in f:
            fields = line.split(',')
            list1 = []
            for i in range(1, len(fields) - 1):
                word = fields[i].strip(' "\'\t\r\n')
                list1.append(word)
            recipes.append(Recipe(
                name=str(fields[0]),
                ingredients=list1,
                instruct=str(fields[len(fields) - 1])
            ))
    return recipes


def search(ingredience: list, resippy: list):
    """
    finds matching recipes
    :param ingredience: ingredients list
    :param resippy: recipe list
    :return:
    """
    show = []
    for entry in resippy:
        if len(ingredience) > len(entry.ingredients):
            result = all(elem in ingredience for elem in entry.ingredients)
            if result:
                show.append(entry)
        elif len(ingredience) == len(entry.ingredients):
            if ingredience == entry.ingredients:
                show.append(entry)
    if show == []:
        print("Sorry, there are no recipes available")
    else:
        for piece in show:
            print("With these ingredients, you can make " + piece.name + " : " + piece.instruct)

def main():
    ingredient_list = input("Input list of different ingredients (a, b, c): ")
    ingre = list_create(ingredient_list)
    resip = readme("rec1test.csv")
    search(ingre, resip)


if __name__ == "__main__":
    main()
