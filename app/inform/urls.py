# conding:utf-8

from app.inform.inform import (
    InformHandler,
)

urlprefix = r''

urlpattern = (
    (r'/inform', InformHandler),
)
