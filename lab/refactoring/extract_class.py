# by Kami Bigdely
# Extract Class
import json

foods = ['{"name": "butternut squash soup", "prep_time": 45, "is_veggie": True, "food_type": "soup", "cuisine": "North African", "ingredients": ["butter squash", "onion", "carrot", "garlic", "butter", "black pepper", "cinnamon", "coconut milk"], "recipe": "1. Grill the butter squash, onion, carrot and garlic in the oven until" "they get soft and golden on top 2. Put all in blender with" "butter and coconut milk. Blend them till they become puree. Then move the content into a pot" ". Add coconut milk. Simmer for 5 mintues.""}',
         '{"name": "shirazi salad", "prep_time": 5, "is_veggie": True, "food_type": "salad", "cuisine": "Iranian", "ingredients": ["cucumber", "tomato", "onion", "lemon juice"], "recipe": "1. dice cucumbers, tomatoes and onions 2. put all into a bowl 3. pour lemon juice 3. add salt" "4. Mixed them thoroughly" }',
         '{"name": "Home-made Beef Sausage", "prep_time": 60, "is_veggie": False, "food_type": "soup", "cuisine": "All", "ingredients": ["sausage casing", "regular ground beef", "garlic", "corriander seeds", "black pepper seeds", "fennel seed", "paprika"], "recipe": "1. In a blender, blend corriander seeds, black pepper seeds, fennel seeds and garlic to make the seasonings 2. In a bowl, mix ground beef with the seasoning 3. Add all the content to a sausage stuffer. Put the casing on the stuffer funnel. Rotate the stuffers handle (or turn it on) to make your yummy sausages!"}']

for food in foods:
    data = json.loads(food)
    print("Name:", data["name"])
    print("Prep time:", data["prep_time"], "mins")
    print("Is Veggie?", "Yes" if data["is_veggie"] else "No")
    print("Food Type:", data["food_type"])
    print("Cuisine:", data["cuisine"])
    for item in data["ingredients"]:
        print(item, end=', ')
    print()
    print("recipe", data["recipe"])
    print("***")
