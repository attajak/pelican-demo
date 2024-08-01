AUTHOR = 'Attajak Janrak'
SITEURL = ""
SITENAME = 'Pelican'
SITESUBTITLE = 'Pelican + Pelican-Twitchy'

PATH = "content"
STATIC_PATHS = ["images"]
ARTICLE_PATHS = ['blog']

RECENT_POST_COUNT = 5
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True

THEME = "themes/pelican-twitchy"

TIMEZONE = 'Asia/Bangkok'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Pelican-Twitchy", "https://github.com/ingwinlu/pelican-twitchy"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Facebook", "https://www.facebook.com/attajak"),
    ("Twitter", "https://twitter.com/attajak"),
    ("GitHub", "https://github.com/attajak"),
    # ("You can add links in your config file", "#"),
    # ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True