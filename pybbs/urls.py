from django.conf.urls.defaults import url, patterns

urlpatterns = patterns ( 'pybbs.views',
    #url ( r'(?P<category_slug>\w+)/$', 'topic_list', name = 'topic_list' ),
    #url ( r'(?P<category_slug>\w+)/(?P<page>\d+)/$', 'topic_list', name = 'topic_list' ),
    url ( r'reply/add\.py$', 'reply_add', name = 'reply_add' ),
    url ( r'reply/update\.py$', 'reply_update', name = 'reply_update' ),
    url ( r'topic/add\.py$', 'topic_add', name = 'topic_add' ),
    url ( r'topic/update\.py$', 'topic_update', name = 'topic_update' ),
    url ( r'(?P<category_slug>\w+)/(?P<topic_id>\d+)\-(?P<topic_slug>\w+)/$', 'topic', name = 'topic' ),
)