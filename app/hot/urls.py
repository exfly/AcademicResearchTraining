# conding:utf-8

from app.hot.hot import (
    HotHandler,
)

urlprefix = r''

urlpattern = (
    (r'/hot', HotHandler),
)
