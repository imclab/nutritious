from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tagz.views',
    # resources
    url(r'^tagz/lib/$', 'lib'),
    url(r'^tagz/lib/(?P<res_name>[^\/]+)/(?P<ref_str>[^\/]+)?$', 'resource'),

    # TAGS
    # all tags
    url(r'^tagz/tags/$', 'tags'),
    # specific tag (GET, DEL)
    url(r'^tagz/tags/(?P<tag_name>[^\/]+)/$', 'tag'),
    #url(r'^tagz/tags/(?P<tag_name>[^\/]+)/editform$', 'tag_edit'),

    # TAG REFERENCE
    # tag detail (GET, DEL)
    url(r'^tagz/tags/(?P<tag_name>[^\/]+)/refs/(?P<id>\d+)$', 'tagref_detail'),
    # create form for specific tag
    url(r'^tagz/tags/(?P<tag_name>[^\/]+)/refs/createform', 'tagref_createform'),
    # create form with arbitrary tag (create tag too)
    url(r'^tagz/tags/createform', 'tagref_createform'),
    # tag create (POST)
    url(r'^tagz/tags/(?P<tag_name>[^\/]+)/refs$', 'tagref_create'),
    # what is this for?
    #url(r'^tagz/tags/(?P<tag_name>[^\/]+)/refs', 'tagref_create'),

    #url(r'^tagz/refs/(?P<ref_name>[^\/]+)/$', 'ref'),

    # home
    url(r'^tagz/$', 'nasb'), # redir to tags
    url(r'^$', 'nasb'), # redir to tags

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
