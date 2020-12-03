from django.db import models


class Teacher(models.Model):

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(max_length=30, verbose_name='email')

    def __str__(self):
        return "Преподаватель: {} {}".format(self.first_name, self.last_name)


class Courses(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание', null=True)
    time = models.CharField(max_length=100, verbose_name='Продолжительность курсов')
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(max_length=30, verbose_name='email')
    course = models.ForeignKey(Courses, verbose_name='Курсы', on_delete=models.CASCADE)

    def __str__(self):
        return "Студент: {} {}".format(self.first_name, self.last_name)


# class Group(models.Model):
#
#     status = models.CharField(max_length=30, verbose_name='Статус группы')
#     course = models.ForeignKey(Courses, verbose_name='Курсы', on_delete=models.CASCADE)
#     student = models.ManyToManyField(Student, blank=True)
#
#     def __str__(self):
#         return "{}, {}".format(self.course.name, self.status)

