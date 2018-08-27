from ._abstract import JSONScraper
from ._utils import get_minutes, normalize_string, dateCleaner

class HundredAndOneCookbooks(JSONScraper):

    @classmethod
    def host(self):
        return '101cookbooks.com'

    def title(self):
        return self.data["name"]

    #need to figure out something for date published
    def datePublished(self):
        date = dateCleaner(self.data["datePublished"],6)
        return date

    def description(self):
        return self.data["description"]


    def total_time(self):
        return get_minutes(data["prepTime"])


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
            instr += instrList[i]["text"] + "\n"
            i += 1

        return instr

    def category(self):
        return self.data["recipeCategory"][0]

    def imgURL(self):
        return self.data["image"][0]


    def sodium(self):
        return self.data["nutrition"]["sodiumContent"]

    def fat(self):
        return self.data["nutrition"]["fatContent"]

    def carbs(self):
        return self.data["nutrition"]["carbohydrateContent"]

    def calories(self):
        return self.data["nutrition"]["calories"]
