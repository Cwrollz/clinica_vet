from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"

    def __str__(self):
        return self.nome

class Animal(models.Model):
    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
        related_name="animais"
    )
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=100, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

    def __str__(self):
        return self.nome

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nome

class Veterinario(models.Model):
    especialidades = models.ManyToManyField(
        Especialidade,
        blank = True,
        related_name="veterinarios"
    )
    nome = models.CharField(max_length=150)
    crmv = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Veterinário"
        verbose_name_plural = "Veterinários"

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    animal = models.ForeignKey(
        Animal,
        on_delete= models.CASCADE,
        related_name="consultas"
    )
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.PROTECT,
        related_name = "consultas"
    )
    data_hora = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    diagnostico = models.TextField(blank=True)
    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null = True,
        blank = True
    )

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return f"{self.animal} - {self.data_hora}"

class Prontuario(models.Model):
    animal = models.OneToOneField(
        Animal,
        on_delete=models.CASCADE,
        related_name="prontuario"
    )
    tipo_sanguineo = models.CharField(max_length=10,blank=True)
    alergias = models.TextField(blank=True)
    observacoes_gerais = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Prontuário"
        verbose_name_plural = "Prontuários"

    def __str__(self):
        return f"Prontuário - {self.animal}"