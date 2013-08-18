import os
import webapp2 as webapp
from google.appengine.ext.webapp import template


class IndexView(webapp.RequestHandler):

    def get(self):
        template_values = {}
        path = os.path.join(
            os.path.dirname(__file__), 'template.html'
        )
        self.response.out.write(template.render(path, template_values))


urls = [
    ('/', IndexView),
]
