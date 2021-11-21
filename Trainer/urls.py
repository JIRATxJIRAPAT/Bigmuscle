
from django.urls import path
from . import views
from .views import PostDetailView
app_name = "Trainer"

urlpatterns = [
    path('', views.index, name="index"),
    path('trainer_course', views.trainer_course, name="trainer_course"),
    path('info/<int:id>', views.courseInfo, name="courseInfo"),
    path('info', views.courseInfo, name="courseInfo"),
    path('apply', views.registerPageTR, name="apply"),
    path('track/<int:id>', views.customerTrack, name="customerTrack"),
    path("addlink", views.add_link, name="addlink"),
    path('<int:id>/edit', views.program_customer, name="program_customer"),
    path("<int:customer_id>/<int:id>", views.show_program, name="show_program"),
    path("<int:id_program>/<int:customer_id>/remove",
         views.remove_program, name="remove_program"),
    path("<int:id>/approve <int:idprogram>",
         views.track_approve, name="trackapprove"),
    path("<int:id>/remove <int:idprogram>",
         views.track_remove, name="trackremove"),
    path("<int:id>/delete <int:idprogram>",
         views.deleteworkout, name="deleteworkout"),
    path('<int:customer_id>/edittrack', views.edittrack, name="edittrack"),
    path("<int:customer_id>/addprogram", views.addprogram, name="addprogram"),
    path("addworkout/<int:idprogram>", views.addworkout, name="addworkout"),
    path("social/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
]