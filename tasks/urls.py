from tasks.apps import TasksConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from tasks.views import (
    EmployeeViewSet,
    TaskListAPIView,
    TaskRetrieveAPIView,
    TaskUpdateAPIView,
    TaskDeleteAPIView,
    TaskCreateAPIView,
    EmployeeTrackAPIView,
    ImportantTasksAPIView,
)

app_name = TasksConfig.name

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employees")

urlpatterns = [
    path("task_list/", TaskListAPIView.as_view(), name="task_list"),
    path("retrieve/<int:pk>/", TaskRetrieveAPIView.as_view(), name="task_retrieve"),
    path("create/", TaskCreateAPIView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateAPIView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteAPIView.as_view(), name="task_delete"),
    path(
        "employee_track/employee_track_list/",
        EmployeeTrackAPIView.as_view(),
        name="employee_track_list",
    ),
    path(
        "important_tasks/important_tasks_list/",
        ImportantTasksAPIView.as_view(),
        name="important_tasks_list",
    ),
] + router.urls
