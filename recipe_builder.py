from dataclasses import dataclass


def list_create(list):
    ingredients = list.split(', ')
    return sorted(ingredients)


@dataclass()
class Recipe:
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
    show = []
    for entry in resippy:
        if len(ingredience) > len(entry.ingredients):
            result = all(elem in ingredience for elem in entry.ingredients)
            if result:
                print(entry.name + ':')
                print(entry.instruct)
        elif len(ingredience) == len(entry.ingredients):
            if ingredience == entry.ingredients:
                print(entry.name + ':')
                print(entry.instruct)

def main():
    ingredient_list = input("Input list of different ingredients (a, b, c): ")
    ingre = list_create(ingredient_list)
    resip = readme("rec1test.csv")
    print(resip)
    search(ingre, resip)


if __name__ == "__main__":
    main()


