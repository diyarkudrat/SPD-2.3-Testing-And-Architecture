# by Kami Bigdely
# Consolidate duplicate conditional fragments
def add_to_mixer(main, addons, milkshake_ingredients=None):
    mix = []

    mix.append(main)
    for item in addons:
        mix.append(item)

    if milkshake_ingredients is not None:
        for item in milkshake_ingredients:
            mix.append(item)

    return mix


def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']


def make_drink(drink, addons):
    if 'coffee' in drink:
        return add_to_mixer('coffee', addons)
    if 'strawberry milkshake' in drink:
        milkshake_ingredients = mixer_ice_with_cream()
        return add_to_mixer('strawberry', addons, milkshake_ingredients)


final_drink = make_drink('strawberry milkshake', ['milk', 'sugar'])
print(final_drink)
