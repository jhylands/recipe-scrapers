from ._abstract import JSONScraper
from ._utils import get_minutes, normalize_string, dateCleaner

class PinchOfYum(JSONScraper):

    @classmethod
    def host(self):
        return 'pinchofyum.com'

    def title(self):
        return self.data["name"]
    '''{
    "@context": "https:\/\/schema.org\/",
    "@type": "Recipe",
    "name": "Chopped Thai Noodle Salad with Peanut Dressing",
    "description": "Thai Noodle Salad with Peanut Lime Dressing - veggies, chicken, brown rice noodles, and an easy homemade dressing. My favorite salad ever!",
    "author": {
        "@type": "Thing",
        "name": "Pinch of Yum"
    },
    "image": [
        "https:\/\/pinchofyum.com\/wp-content\/uploads\/Thai-Salad-Recipe-225x225.jpg",
        "https:\/\/pinchofyum.com\/wp-content\/uploads\/Thai-Salad-Recipe-260x195.jpg",
        "https:\/\/pinchofyum.com\/wp-content\/uploads\/Thai-Salad-Recipe-320x180.jpg",
        "https:\/\/pinchofyum.com\/wp-content\/uploads\/Thai-Salad-Recipe.jpg"
    ],
    "url": "https:\/\/pinchofyum.com\/thai-noodle-salad",
    "recipeIngredient": [
        "1\/2 cup canola oil",
        "2 large cloves garlic, peeled",
        "1\/3 cup low sodium soy sauce",
        "1\/4 cup white distilled vinegar",
        "2 tablespoons water",
        "2 tablespoons honey",
        "2 tablespoons sesame oil",
        "1 tablespoon lemongrass or ginger paste",
        "a couple BIG squeezes of lime juice (to taste)",
        "1\/4 cup peanut butter",
        "4 ounces brown rice noodles (affiliate link)",
        "1 lb. boneless skinless chicken breasts",
        "5-6 cups baby kale or spinach",
        "3 large carrots, cut into small, thin pieces*",
        "3 bell peppers, cut into small, thin pieces*",
        "1 cup packed cilantro leaves, chopped",
        "4 green onions, green parts only, chopped",
        "1\/2 cup cashews or peanuts"
    ],
    "recipeInstructions": [
        "PREP: Start soaking the rice noodles in a bowl of cold water. Preheat the oven to 400 degrees.",
        "DRESSING: Pulse all the dressing ingredients in a food processor EXCEPT peanut butter. Place the chicken in a plastic bag and use about 1\/4 to 1\/2 cup of the dressing (without peanut butter) to marinate the chicken in the fridge for about 15-30 minutes. Add the peanut butter to the dressing in the food processor; pulse, then taste and adjust. Set aside.",
        "VEGGIES: Prep all your veggies and toss together in a bowl.",
        "CHICKEN: Bake the marinated chicken for 15-20 minutes. Rest for 5-10 minutes, then cut and add to the veggies.",
        "NOODLES: Drain the noodles (they should be softened at this point). Finish cooking them in a skillet over medium high heat. Add a little oil and a little dressing and toss them around until they are soft and pliable (if you need to add a little water to soften them, that works, too).",
        "ASSEMBLY: Toss stir-fried noodles with the chicken and veggie mixture. Serve hot or cold. Top with extra peanuts and cilantro (and dressing, and lime juice, and sesame seeds, and...)"
    ],
    "prepTime": "PT45M",
    "cookTime": "PT20M",
    "totalTime": "PT1H5M",
    "recipeYield": "6",
    "aggregateRating": {
        "@type": "AggregateRating",
        "reviewCount": 34,
        "ratingValue": 4.7
    }
   '''


    #need to figure out something for date published
    def datePublished(self):
        date = dateCleaner("null",6)
        return date

    def description(self):
        return self.data["description"]


    def total_time(self):
        return get_minutes(data["totalTime"])


    def ingredients(self):
        ing = ""
        ingList = self.data['recipeIngredient']
        i = 0
        while i < len(ingList):
            ing += ingList[i] + "\n"
            i += 1
        return ing


    def instructions(self):
        #this is a nested array
        instrList = self.data['recipeInstructions']
        i = 0
        instr = ""
        while i < len(instrList):
            instr += instrList[i] + "\n"
            i += 1

        return instr

    def category(self):
        return self.data["recipeCategory"][0]

    def imgURL(self):
        return self.data["image"][3]


    def sodium(self):
        return self.data["nutrition"]["sodiumContent"]

    def fat(self):
        return self.data["nutrition"]["fatContent"]

    def carbs(self):
        return self.data["nutrition"]["carbohydrateContent"]

    def calories(self):
        return self.data["nutrition"]["calories"]
