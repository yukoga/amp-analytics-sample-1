#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['charset'] = 'utf-8'
        #mymsg = u'Hello World!, $BF|K\8lDI2C(B'.encode('utf-8')
        mymsg = 'amp-analytics $B$N%F%9%H(B'
        self.response.write(mymsg)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
