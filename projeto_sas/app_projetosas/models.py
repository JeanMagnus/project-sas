from django.db import models

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    matricula = models.IntegerField()
    email = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)
    
class Professor(models.Model):
    id_prof = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    setor = models.TextField(max_length=255)
    numeracao = models.TextField(max_length=255)
    status = models.TextField(max_length=255)
    horario_disp = models.TextField(max_length=255)
    
class Solicitacao(models.Model):
    id_solicitacao = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, default=1)  # Relacionamento com Aluno
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)    # Relacionamento com Sala
    horario = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    situacao = models.TextField(max_length=255, default="Em análise")
    
class Cancelamento(models.Model):
    id_cancelamento = models.AutoField(primary_key=True)
    Solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, default=1)
    

    
    

