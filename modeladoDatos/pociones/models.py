from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User


class Efecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = "Efectos"
    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200)
    origen = models.CharField(max_length=100)

    efectos = models.ManyToManyField(Efecto)

    class Meta:
        verbose_name_plural = "Ingredientes"
    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Especialidades"
    def __str__(self):
        return self.nombre

class Aquelarre(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Aquelarres"
    def __str__(self):
        return self.nombre

class Bruja(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    aquelarre = models.ForeignKey(Aquelarre, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Brujas"
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=400)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.usuario.username

class Pocion(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)

    class Tamano(models.TextChoices):
        PEQUENA = 'PQ', 'Pequeña',
        MEDIANA = 'MED', 'Mediana',
        GRANDE = 'GR', 'Grande'

    tamano = models.CharField(max_length=3, choices=Tamano.choices, default=Tamano.MEDIANA)
    bruja = models.ForeignKey(Bruja, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Pociones"
    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    pociones = models.ManyToManyField(Pocion, through='PocionesPedido')

    @property
    def precio_total(self):
        total = sum(item.precio_unidad * item.cantidad for item in self.items.all())
        return total

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha']
    def __str__(self):
        return str(self.pk)


class PocionesPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    pocion = models.ForeignKey(Pocion, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unidad = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Pociones Pedidos"

    def save(self, *args, **kwargs):
        if not self.precio_unidad:
            self.precio_unidad = self.pocion.precio
        super().save(*args, **kwargs)

    class Meta:
        models.UniqueConstraint(fields=['pedido', 'pocion'], name='unique_pocion')

    def __str__(self):
        return f"{self.cantidad} unidades de la poción {self.pocion} en el pedido {self.pedido}"