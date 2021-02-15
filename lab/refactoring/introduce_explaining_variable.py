# By Kami Bigdely
# Introduce explaining variable (alias extract variable)
# Reference: https://www.researchgate.net/publication/305768969_The_role_of_eye_characteristics_in_facial_beauty_likability_and_attractiveness
# Background: You are a computer engineer trying to sift through many profiles to find
# your soulmate. Unfortunately, there are too many profiles and it's getting tedious. You write a
# python script to scrape profiles info (such as height, age, etc) and images (for image processing)
# to figure out automatically who is attractive to you.  Here is a part of the script:
import math
# assuming you have extracted the following info from the profile's image.

# eye_size = 0.47    # [cm^2]
# eye_width = 24.2   # [mm]
# eye_height = 23.7  # [mm]

# iris_width = 20.2  # [mm]
# iris_height = 19.7  # [mm]

# if eye_size > 0.45 and (math.pi*iris_width/2*iris_height/2) / eye_size >= 0.69 and \
#         eye_height/eye_width >= 0.59:
#     print("I’m sorry I wasn’t part of your past, can I make it up by being in your future?")


class Soulmate:
    def __init__(self, eye_size, eye_height, eye_width, iris_height, iris_width):
        self.eye_size = eye_size
        self.eye_height = eye_height
        self.eye_width = eye_width
        self.iris_height = iris_height
        self.iris_width = iris_width

    def meet_requirements(self):
        iris_rating = (math.pi*self.iris_width/2 *
                       self.iris_height/2) / self.eye_size
        eye_ratio = self.eye_height / self.eye_width

        return self.eye_size > 0.45 and iris_rating >= 0.69 and eye_height >= 0.59

    def is_match(self):
        if self.meet_requirements():
            print(
                "I’m sorry I wasn’t part of your past, can I make it up by being in your future?")


eye_size = 0.47    # [cm^2]
eye_width = 24.2   # [mm]
eye_height = 23.7  # [mm]

iris_width = 20.2  # [mm]
iris_height = 19.7  # [mm]

soulmate = Soulmate(eye_size, eye_height, eye_width, iris_height, iris_width)
soulmate.is_match()
