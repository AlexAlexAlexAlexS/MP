from django.db import models

class Group(models.Model):
    groupName = models.TextField(max_length=32)
    groupsize = models.IntegerField()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    
    def __str__(self):
        return f'{self.groupName}'


class Student(models.Model):
    studentName = models.TextField(max_length=32)
    studentAge = models.IntegerField()
    studentGender = models.TextField(max_length=10)
    studentGroup = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.studentName}'