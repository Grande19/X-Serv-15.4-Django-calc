from django.conf.urls import patterns, include, url
from django.contrib import admin
#from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/' , 'calc.views.calc_start'),
    url(r'^calc/(?P<num1>\d+)\+(?P<num2>\d+)' , 'calc.views.calc_sum'),
    url(r'^calc/(?P<num1>\d+)\*(?P<num2>\d+)' , 'calc.views.calc_mul'),
    url(r'^calc/(?P<num1>\d+)\-(?P<num2>\d+)' , 'calc.views.calc_res'),
    url(r'^calc/(?P<num1>\d+)/(?P<num2>\d+)' , 'calc.views.calc_div'),
    #d+ uno o mas digitos llevan la etiqueta num1 y num2
    url(r'.*','calc.views.Error')
]
