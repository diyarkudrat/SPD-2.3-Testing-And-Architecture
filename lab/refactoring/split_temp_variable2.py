# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


username_input = input('Please enter your username: ')
save_into_db(username_input)
user_age_input = int(input('Please enter your birth year: '))
age = 2020 - user_age_input
print("You are", age, "years old.")
