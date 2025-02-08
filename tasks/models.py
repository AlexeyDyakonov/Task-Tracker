from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Employee(models.Model):
    """Модель сотрудника"""

    user = models.ForeignKey(
        User, **NULLABLE, on_delete=models.CASCADE, verbose_name="Сотрудник"
    )
    full_name = models.CharField(
        max_length=200,
        **NULLABLE,
        verbose_name="ФИО",
        help_text="Введите Фамилию, имя и отчество",
    )
    position = models.CharField(
        max_length=250,
        **NULLABLE,
        verbose_name="Должность",
        help_text="Укажите должность работника",
    )

    def __str__(self):
        return f"{self.full_name} - {self.position}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Task(models.Model):
    """Модель задачи"""

    JOB_STATUS = "ToDo"
    PROGRESS_STATUS = "Progress"
    DONE_STATUS = "Done"
    CLOSED_STATUS = "Closed"

    STATUS_CHOICES = (
        (JOB_STATUS, "В работу"),
        (PROGRESS_STATUS, "В работе"),
        (DONE_STATUS, "Выполнен"),
        (CLOSED_STATUS, "Отменен"),
    )

    title = models.CharField(max_length=250, verbose_name="Название задачи")
    description = models.TextField(**NULLABLE, verbose_name="Описание задачи")
    executor = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        **NULLABLE,
        related_name="tasks",
        verbose_name="исполнитель задачи",
    )
    status = models.CharField(max_length=50, **NULLABLE, verbose_name="Статус")
    time_complete = models.DateTimeField(
        **NULLABLE, verbose_name="Дата и время выполнения"
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="parent",
        verbose_name="Родительская задача",
    )
    is_active = models.BooleanField(
        default=False, verbose_name="Признак активной задачи"
    )
    is_related = models.BooleanField(
        default=False, verbose_name="Признак связанной задачи"
    )

    def __str__(self):
        return (
            f"{self.title} {self.parent_task} {self.executor}"
            f"{self.time_complete} {self.status} {self.is_related} {self.is_active}"
        )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
