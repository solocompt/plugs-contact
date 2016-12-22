from rest_framework import routers

from plugs_contact import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'contacts', views.ContactViewSet)
urlpatterns = ROUTER.urls
