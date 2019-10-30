from django.conf.urls import url#se importa url, apare mai jos in urlpatterns
from django.contrib import admin#se importa admin, apare mai jos in urlpatterns
from .views import homePageView#din view.py importa functia homePageView; .views spune ca trebuie importat din directorul curent(main), mentiunea e pentru ca django sa stie de unde sa il importe sa nu il caute prin alta parte

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url('',homePageView,name="home"),
]
#s-a adaugat: url('',homePageView,name="home") in urlpatterns. are 3 argumente dupa cum urmeaza: primul "''" numele paginii. If it was something like about/aboutme then the page would be located at https://domain.name/about/aboutme (replacing domain.name with the domain name, obviously). However, it is just '' so the view will be located at just https://domain.name/., al doilea termen este functia din views.py, al treilea termen este numele pe care il dam paginii, 