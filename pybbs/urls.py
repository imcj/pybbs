from django.conf.urls.defaults import url, patterns

urlpatterns = patterns ( 'pybbs.views',
    #url ( r'(?P<category_slug>\w+)/$', 'topic_list', name = 'topic_list' ),
    #url ( r'(?P<category_slug>\w+)/(?P<page>\d+)/$', 'topic_list', name = 'topic_list' ),
    url ( r'/topic/add\.py$', 'topic_add', name = 'topic_add' ),
    url ( r'(?P<category_slug>\w+)/(?P<topic_id>\d+)\-(?P<topic_slug>\w+)/$', 'topic', name = 'topic' ),
)