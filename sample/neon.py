import sys
import os

class Example(object):

    backquotes = `backquotes`

    @memoize(size=10)
    def Call(self, param1=None):
        u'''unicode'''
        return param1 + 10 * 10

    def Call2(self):
        b'''bytes'''
        # Comment
        return self.Call(param1=10)
