from ._abstract import AbstractScraper
from ._utils import get_minutes_from_string, normalize_string


class Tasty(AbstractScraper):

    @classmethod
    def host(self):
        return 'tasty.co'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        prep_steps = self._get_prep_steps()
        return get_minutes_from_string(' '.join(prep_steps))

    def ingredients(self):
        ingredients = self.soup.find(
            'div',
            {'class': 'ingredients__section'}
        ).findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        return '\n'.join(self._get_prep_steps())

    def _get_prep_steps(self):
        instructions_html = self.soup.find(
            'ol',
            {'class': 'prep-steps'}
        ).findAll('li')

        return [normalize_string(instruction.get_text()) for instruction in instructions_html]
