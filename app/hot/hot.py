# coding:utf-8

from app.cache import hot_post_cache, system_status_cache, topic_category_cache

from custor.handlers.basehandler import BaseRequestHandler
from custor.decorators import timeit, exception_deal, check_captcha
from custor.utils import get_cleaned_post_data, get_cleaned_query_data
from custor.utils import json_result, get_page_nav, get_page_number

from db.mysql_model.post import Post, PostTopic
from db.mysql_model.user import User

from custor.errors import RequestMissArgumentError, PageNotFoundError

class HotHandler(BaseRequestHandler):
    """
    社区首页
    """
    # 时间消耗装饰器
    @timeit
    # 异常捕获装饰器
    @exception_deal([RequestMissArgumentError,]) # 也许这个参数有其他用处先留着
    def get(self, *args, **kwargs):
        # profiling 性能分析
        # from profiling.tracing import TracingProfiler
        #
        # # profile your program.
        # profiler = TracingProfiler()
        # profiler.start()
        self.render('hot/hot.html',
                    topic_category_cache=topic_category_cache,
                    hot_post_cache=hot_post_cache,
                    systatus=system_status_cache,
                    current_topic=None,
                    pages_prefix_url='/?page=')
