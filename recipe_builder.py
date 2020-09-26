def list_create(list):
    ingredients = list.split(', ')
    return sorted(ingredients)


def main():
    ingredient_list = input("Input list of different ingredients (a, b, c): ")
    return list_create(ingredient_list)


if __name__ == "__main__":
    main()
