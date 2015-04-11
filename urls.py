from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from mipt_hack_server import views

urlpatterns = patterns("",
  url(r"^$", views.index, name="index"),
  url(r"^thanks/$", TemplateView.as_view(template_name="mipt_hack_server/thanks.html"), name="thanks"),

  url(r"^confirm/(?P<activation_key>[a-z0-9]{,32})/$", views.confirm, name="confirm-key"),
  url(r"^logout/$", "django.contrib.auth.views.logout", {"next_page": "/test/"}, name="logout"),
  url(r"^reset-password/$", views.ResetPassword.as_view(), name="reset-password"),
  url(r"^settings/$", views.settings, name="settings"),

  url(r"^category/(?P<pk>\d+)/$", views.CategoryView.as_view(), name="category"),
  # TODO:: add form for creation of category if user is_staff

  url(r"^event/(?P<pk>\d+)/$", views.EventView.as_view(), name="event"),
  url(r"^event/(?P<pk>\d+)/join/$", views.join_event, name="join-event"),
  url(r"^event/(?P<pk>\d+)/leave/$", views.leave_event, name="leave-event"),
  url(r"^event/my/$", views.MyEventsList.as_view(), name="myevents"),
  url(r"^event/all/$", views.AllEventsList.as_view(), name="allevents"),
  url(r"^event/create/$", views.CreateEventView.as_view(), name="create-event"),
  url(r"^search/$", views.SearchList.as_view(), name="search"),

)
