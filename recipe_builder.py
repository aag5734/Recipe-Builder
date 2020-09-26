def list_create(list):
    ingredients = []
    for i in range(len(list)):
        if list[i] == ',':
            ingredients.append(list[0:i])
    print(ingredients[0])


def main():
    ingredient_list = input("Input list of different ingredients (a, b, c): ")
    list_create(ingredient_list)


if __name__ == "__main__":
    main()
