from django.db import models

class HomePage(models.Model):
    description = models.TextField(verbose_name="Опис факультету")
    main_info = models.TextField(verbose_name="Основна інформація")
    contacts = models.TextField(verbose_name="Контакти")

class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва кафедри")
    head = models.CharField(max_length=200, verbose_name="Завідувач кафедри")

class Specialty(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва спеціальності")
    code = models.CharField(max_length=50, verbose_name="Код")
    description = models.TextField(verbose_name="Опис")
    coordinator_name = models.CharField(max_length=200, verbose_name="Координатор")
    coordinator_contact = models.CharField(max_length=200, verbose_name="Контакти координатора")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    disciplines = models.TextField(verbose_name="Дисципліни")

class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я викладача")
    position = models.CharField(max_length=100, verbose_name="Посада")
    degree = models.CharField(max_length=100, verbose_name="Ступінь")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)