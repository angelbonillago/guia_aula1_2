from django.db import models

# Create your models here.

#modelos que luego se convierten en una TABLAS!
class Proyecto(models.Model):
    nombre=models.CharField(max_length=200)
    caracteristica=models.CharField(max_length=300)

    def __str__(self):
        return self.nombre 



class Tarea(models.Model):
    nombre=models.CharField(max_length=100)
    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +" -> Proyecto: "+self.proyecto.nombre

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class PersonaProxy(Person):
    class Meta:
        proxy = True

















"""
class ExtensionTarea(Proyecto):
    class Meta:
        ordering=['nombre']
        proxy=True

"""

 #Abtract

""" class CommonInfo(models.Model):

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
    #No tengo declarada una clase Meta, por lo cual,cuando haga la migracion, heredo los campos de mi clase CommonInfo(HERENCIA PADRE->HIJO) """


#Modelo proxy

""" class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    #fullname = models.CharField(max_length=30)
    class Meta:
        proxy = True """