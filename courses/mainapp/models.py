from django.db import models


class Toolbox(models.Model):
    title = models.CharField(max_length=30, verbose_name='Технология')

    def __str__(self):
        return self.title


class WorkDay(models.Model):
    title = models.CharField(max_length=30, verbose_name='День недели')

    def __str__(self):
        return self.title


class WorkTime(models.Model):
    part_day = models.CharField(max_length=30, verbose_name='Часть дня')
    time_on = models.CharField(max_length=30, verbose_name='Время начала занятия')
    time_off = models.CharField(max_length=30, verbose_name='Время конца занятия')

    def __str__(self):
        return self.part_day


class Timetable(models.Model):
    time = models.ForeignKey(WorkTime, verbose_name='Время занятий', on_delete=models.CASCADE)
    practice = models.ForeignKey(WorkDay, verbose_name='Практика', on_delete=models.CASCADE, related_name='related_practice')
    lecture = models.ForeignKey(WorkDay, verbose_name='Лекции', on_delete=models.CASCADE, related_name='related_lecture')

    def __str__(self):
        return "{}, практика - {}, лекции - {}".format(self.time, self.practice, self.lecture)


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
    timetable = models.ForeignKey(Timetable, default='', verbose_name='Расписание', on_delete=models.CASCADE)
    toolbox_1 = models.ForeignKey(Toolbox, default='', verbose_name='Технология 1', on_delete=models.CASCADE, related_name='related_toolbox_1')
    toolbox_2 = models.ForeignKey(Toolbox, default='', verbose_name='Технология 2', on_delete=models.CASCADE, related_name='related_toolbox_2')
    toolbox_3 = models.ForeignKey(Toolbox, default='', verbose_name='Технология 3', on_delete=models.CASCADE, related_name='related_toolbox_3')
    toolbox_4 = models.ForeignKey(Toolbox, default='', verbose_name='Технология 4', on_delete=models.CASCADE, related_name='related_toolbox_4')

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

