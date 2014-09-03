import os

from google.appengine.dist import use_library
use_library('django', '1.2')
os.environ['DJANGO_SETTINGS_MODULE'] = '__init__'

import webapp2 as webapp
from webapp2_extras import sessions
from google.appengine.ext.webapp import template

import apis
import seeds

sessions.default_config['secret_key'] = 'dev'

class IndexView(webapp.RequestHandler):

    def get(self):

        s = seeds.Seeder()
        s.clean()
        s.seed()

        template_values = {}
        path = os.path.join(
            os.path.dirname(__file__), 'template.html'
        )
        self.response.out.write(template.render(path, template_values))


urls = apis.urls + [
    ('/', IndexView),
]

app = webapp.WSGIApplication(urls, debug=True)
