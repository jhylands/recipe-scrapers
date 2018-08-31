from bs4 import BeautifulSoup as bs
# some sites close their content for 'bots', so user-agent must be supplied using random user agent


class AbstractScraper():

    def __getattribute__(self, name):
        """
        Decorate custom methods to handle exceptions as we want and as we
        specify in the "on_exception_return" method decorator
        """
        to_return = None
        decorated_methods = [
            'title',
            'total_time',
            'instructions',
            'ingredients',
            'links',
            'URL',
            'description',
            'imgURL',
            'sodium',
            'fat',
            'cholesterol',
            'carbs',
            'calories',
            'category',
            'datePublished'
        ]
        if name in decorated_methods:
            to_return = ''
        if name == 'total_time':
            to_return = 0
        if name == 'ingredients':
            to_return = []
        if name == 'links':
            to_return = []


        if to_return is not None:
            return on_exception_return(to_return)(object.__getattribute__(self, name))

        return object.__getattribute__(self, name)

    def __init__(self, request):
        self.soup = BeautifulSoup(request.text,"html.parser")
        self.url = request.url

    def url(self):
        return self.url

    def host(self):
        """ get the host of the url, so we can use the correct scraper """
        raise NotImplementedError("This should be implemented.")

    def title(self):
        raise NotImplementedError("This should be implemented.")

    def total_time(self):
        """ total time it takes to preparate the recipe in minutes """
        raise NotImplementedError("This should be implemented.")

    def ingredients(self):
        raise NotImplementedError("This should be implemented.")

    def instructions(self):
        raise NotImplementedError("This should be implemented.")

    def URL(self):
        raise NotImplementedError("This should be implemented.")

    def description(self):
        raise NotImplementedError("This should be implemented.")

    def imgURL(self):
        raise NotImplementedError("This should be implemented.")

    def sodium(self):
        raise NotImplementedError("This should be implemented.")

    def fat(self):
        raise NotImplementedError("This should be implemented.")

    def cholesterol(self):
        raise NotImplementedError("This should be implemented.")

    def carbs(self):
        raise NotImplementedError("This should be implemented.")

    def calories(self):
        raise NotImplementedError("This should be implemented.")

    def category(self):
        raise NotImplementedError("This should be implemented.")

    def datePublished(self):
        raise NotImplementedError("This should be implemented.")

    def links(self):
        invalid_href = ('#', '')
        links_html = self.soup.findAll('a', href=True)

        return [
            link.attrs
            for link in links_html
            if link['href'] not in invalid_href
        ]



