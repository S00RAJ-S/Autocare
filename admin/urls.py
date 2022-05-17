from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('viewusers/',views.viewusers),
    path('viewpartners/',views.viewpartners),
    path('deluser/',views.deluser),
    path('delpartner/',views.delpartner),
    path('approvals/',views.approvals),
    path('approved/',views.approved),
    path('approvedp/',views.approvedp),
    path('feedbacks/',views.feedbacks),
]
