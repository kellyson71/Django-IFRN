from django.db import models

# Create your models here.

class paciente (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    def __str__(self):
        return self.nome
    
class medico (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    especialidade = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class consulta (models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(medico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.paciente.nome + ' - ' + self.medico.nome + ' - ' + str(self.data) + ' - ' + str(self.hora)

class medicamento (models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    

class prescricao (models.Model):
    medicamento = models.ManyToManyField(medicamento)
    descriçao = models.TextField()
    consulta = models.ForeignKey(consulta, on_delete=models.CASCADE)
    def __str__(self):
        return self.consulta.nome + ' - ' + self.medicamento + ' - ' + self.descriçao