#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

def main():
    urls = [
        ('/', MainHandler),
        ('/spreadsheet/', SpreadsheetHandler),
        ('/query/', AdsQueryHandler),
        ('/.*', CatchAll),
    ]
    application = webapp.WSGIApplication(urls, debug=True)
    wsgiref.handlers.CGIHandler().run(application)

# TODO: see http://github.com/DocSavage/bloog/blob/master/main.py for non trivial examples
class MainHandler(webapp.RequestHandler):

    def get(self):
        self.response.out.write(
            template.render('sexy.html', {
                'title': 'Advertise Amazon products on Facebook'
            })
        )

class SpreadsheetHandler(webapp.RequestHandler):

    def get(self):
        self.response.out.write('hello spreadsheet')

class AdsQueryHandler(webapp.RequestHandler):

    def get(self):
        self.response.out.write(
            template.render('toosexy.html', {'title': 'Query Facebook Ads'})
        )


class CatchAll(webapp.RequestHandler):

    def get(self):
        # TODO: redirect to /
        self.response.out.write('catch all')

if __name__ == '__main__':
  main()