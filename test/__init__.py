import webapp2 as webapp
import apis
import views

urls = apis.urls + views.urls

app = webapp.WSGIApplication(urls, debug=True)
