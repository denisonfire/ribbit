from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ribbit.views.index'), # root
    url(r'^login$', 'ribbit.views.login_view'), # login
    url(r'^logout$', 'ribbit.views.logout_view'), # logout
    url(r'^ribbits$', 'ribbit.views.public'), # public ribbits
    url(r'^submit$', 'ribbit.views.submit'), # submit new ribbit
    url(r'^users/$', 'ribbit.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'ribbit.views.users'),
    url(r'^follow$', 'ribbit.views.follow'),
    # Examples:
    # url(r'^$', 'ribbit.views.home', name='home'),
    # url(r'^ribbit/', include('ribbit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
