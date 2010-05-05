from django.utils.translation import ugettext_noop as _

from multilang.defaults import *


urlpatterns = patterns('garfield.views',
    url(r'^$', 'landing', name='garfield_landing'),
    url(_(r'^the-president/$'), 'the_president', name='garfield_the_president'),
    url(_(r'^the-cat/$'), 'comic_strip_list', name='garfield_the_cat'),
    url(_(r'^the-cat/(?:P<strip_id>\d+)/$'), 'comic_strip_detail',
            name='garfield_comic_strip_detail'),
    url(r'^jim-davis/$', 'jim_davis', name='garfield_jim_davis'),
)
