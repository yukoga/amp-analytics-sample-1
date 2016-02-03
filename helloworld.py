#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['charset'] = 'utf-8'
        #mymsg = u'Hello World!, 日本語追加'.encode('utf-8')
        mymsg = 'amp-analytics のテスト'
        self.response.write(mymsg)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
