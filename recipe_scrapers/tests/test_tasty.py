import os
import unittest

from recipe_scrapers.tasty import Tasty


class TestTastyScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'tasty.testhtml'
        )) as file_opened:
            self.harvester_class = Tasty(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'tasty.co',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Crème Brûlée French Toast'
        )

    def test_total_time(self):
        self.assertEqual(
            33,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertListEqual(
            [
                '4 cups (960 mL) heavy cream',
                '1 ¼ cups (250 g) sugar, divided',
                '1 tablespoon cinnamon',
                '6 large egg yolks',
                '2 teaspoons vanilla extract',
                '18 slices brioche bread',
                '½ lb (225 g) strawberry',
                '1 cup (60 g) whipped cream'
            ], 
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Preheat the oven to 350˚F (180˚C). Line a baking sheet with parchment paper and set a wire rack on top.\nPour the heavy cream into a 9x13-inch (23x33 cm) baking dish.\nMix 1 cup of sugar (200 g) and the cinnamon in a small bowl and add to the cream, followed by the egg yolks and vanilla. Whisk well to combine.\nDip each slice of bread into the cream mixture, coating both sides well. Place the dipped bread on the wire rack set over the baking sheet. Bake for 15 minutes, flip the bread over, then bake for another 15 minutes, until slightly crispy.\nSlice the strawberries into decorative shapes of your choosing. For a strawberry rose, place a strawberry stem side down and carefully make thin slices around the outer edge of the strawberry, making sure not to cut all the way through. Continue cutting and rotating the strawberry until you get to the center. Fan out the “petals”.\nFor a strawberry fan, lay a strawberry on its flattest side. Tilt the knife at a 45˚ angle and make thin, angled slices through the strawberry, keeping the top of the strawberry connected and slicing all the way through the bottom of the berry. Fan out the slices.\nSprinkle the remaining sugar on top of the bread and broil on high for 3 minutes, until the sugar has melted and browned, or carefully use a kitchen torch to brûlée the sugar.\nTop with whipped cream and strawberries and serve.\nEnjoy!',
            self.harvester_class.instructions()
        )
