## Recipe scrapers

"A simple web scraping tool for recipe sites I use in a project of mine that makes sense to live as
a separate package. **No Python 2 support.** " hhursev
I have added to the original scraper to add JSON parsing to simplify scraping web sites that follow the schema.org format for ld+json. I have also added more data to scrape for my project.
In addition I have added a random user agent and scraping through random proxy servers to limit getting blocked.

    pip install git+git://github.com/levinems/recipe-scrapers.git

then:

    from recipe_scrapers import scrape_me

    url = "https://www.101cookbooks.com/archives/quick-blistered-cherry-tomato-spaghetti/"
    scrape_me = scrape_me(url)

    title = scrape_me.title()
    totalTime = scrape_me.total_time()
    ingredients = scrape_me.ingredients()
    instructions = scrape_me.instructions()
    description = scrape_me.description()
    category = scrape_me.category()
    imgURL = scrape_me.imgURL()
    sodium = scrape_me.sodium()
    fat = scrape_me.fat()
    carbs = scrape_me.carbs()
    calories = scrape_me.calories()
    datePublished = scrape_me.datePublished()

Note: scrape_me.links() returns a dictionary object containing all of the <a> tag attributes. The attribute names are the dictionary keys.

### Contribute

Part of the reason I want this open sourced is because if a site makes a design change, the scraper
for it should be modified.

If you spot a design change (or something else) that makes the scrapers unable to work for the given
site - please fire an issue asap.

### Scrapers available for:

- [http://101cookbooks.com/](http://101cookbooks.com/) //JSON parser
- [http://allrecipes.com/](http://allrecipes.com/)
- [http://bbc.co.uk/](http://bbc.co.uk/food/recipes/)
- [http://bbcgoodfood.com/](http://bbcgoodfood.com/)
- [http://bonappetit.com/](http://bonappetit.com/)
- [http://closetcooking.com/](http://closetcooking.com/)
- [http://cookstr.com/](http://cookstr.com/)
- [http://epicurious.com/](http://epicurious.com/)
- [http://finedininglovers.com/](https://www.finedininglovers.com/)
- [http://foodnetwork.com/](http://www.foodnetwork.com)
- [http://foodrepublic.com/](http://foodrepublic.com)
- [http://giallozafferano.it/](http://giallozafferano.it)
- [https://inspiralized.com/](https://inspiralized.com/)
- [http://jamieoliver.com/](http://www.jamieoliver.com/)
- [http://mybakingaddiction.com/](http://mybakingaddiction.com/)
- [https://healthyeating.nhlbi.nih.gov/](https://healthyeating.nhlbi.nih.gov/)
- [http://paninihappy.com/](http://paninihappy.com/)
- [http://realsimple.com/](http://www.realsimple.com/)
- [http://simplyrecipes.com/](http://www.simplyrecipes.com)
- [http://steamykitchen.com/](http://steamykitchen.com/)
- [http://tastykitchen.com/](http://tastykitchen.com/)
- [http://thepioneerwoman.com/](http://thepioneerwoman.com/)
- [http://thevintagemixer.com/](http://www.thevintagemixer.com/)
- [http://twopeasandtheirpod.com/](http://twopeasandtheirpod.com/)
- [http://whatsgabycooking.com/](http://whatsgabycooking.com/)


### If you want a scraper for a new site added

- Open an [Issue](https://github.com/levinems/recipe-scraper/issues/new) providing us the site name, as well as a recipe link from it.
- If you are a developer and want to code the scraper on your own, [this is a wonderful example](https://github.com/hhursev/recipe-scraper/pull/29/files) of how to do it.

#### For Devs

Assuming you have [virtualenv](https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) installed, navigate to the directory where you want this project to live in and drop these lines

    git clone git@github.com:levinems/recipe-scrapers.git &&
    cd recipe-scrapers &&
    mkvirtualenv -a `pwd` -p python3 -r requirements.txt recipe-scrapers &&
    coverage run tests.py &&
    coverage report

For a full setup and project check.
