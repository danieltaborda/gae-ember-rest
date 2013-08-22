import os
import webapp2 as webapp
from google.appengine.ext.webapp import template
import apis


class IndexView(webapp.RequestHandler):

    def get(self):
        template_values = {}
        path = os.path.join(
            os.path.dirname(__file__), 'template.html'
        )
        self.response.out.write(template.render(path, template_values))


urls = apis.urls + [
    ('/', IndexView),
]

app = webapp.WSGIApplication(urls, debug=True)
