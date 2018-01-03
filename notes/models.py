from django.db import models
from datetime import datetime

class Note(models.Model):
    responsavel = models.CharField(max_length=80)
    descricao = models.CharField(max_length=800)
    data = models.DateField('Data')    
    def __str__(self):
        return self.descricao

class Responsavel(models.Model):
    responsavel = models.CharField('Codigo', max_length=80)
    descricao = models.CharField('Nome Completo', max_length=800)
    data_registro = models.DateField('Date', null=True)    
    def __str__(self):
        return self.responsavel