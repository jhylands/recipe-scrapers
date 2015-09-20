from ._abstract import AbstractScraper

from ._consts import TIME_REGEX


class TwoPeasAndTheirPod(AbstractScraper):

    @classmethod
    def host(self):
        return 'twopeasandtheirpod.com'

    def publisher_site(self):
        return 'http://twopeasandtheirpod.com/'

    def title(self):
        return self.soup.find('h2').get_text()

    def total_time(self):
        try:
            time = self.soup.find('span', {'class': 'duration'})
            matched = TIME_REGEX.search(time.get_text())

            if matched is None:
                raise AttributeError

            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)

        except AttributeError:  # when there is no span or no time regex match
            return 0

    def ingredients(self):
        ingredients_html = self.soup.find('div', {'class': 'ingredient'}).findAll('p')
        ingredients_flatten = []
        for ingredient in ingredients_html:
            ingredients_flatten.extend(ingredient.get_text().split('\n'))

        return [
            ingredient for ingredient in ingredients_flatten
            if ingredient[0].isdigit()
        ]

    def instructions(self):
        return self.soup.find('div', {'class': 'instructions'}).get_text()
