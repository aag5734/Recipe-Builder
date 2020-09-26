def list_create(list):
    ingredients = list.split(', ')
    print(ingredients)


def main():
    ingredient_list = input("Input list of different ingredients (a, b, c): ")
    list_create(ingredient_list)


if __name__ == "__main__":
    main()

