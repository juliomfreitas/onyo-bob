from powerball_backend import views
from django.conf.urls import url

urlpatterns = [
    url(r'^ticket/check-winner/', views.VerifyTicketView().as_view()),

    url(r'^ticket/create/', views.CreateTicketView().as_view()),
]
