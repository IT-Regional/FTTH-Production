from django.db import models


# Create your models here.
class Cluster(models.Model):
    TIPO_CHOICES = [
        ("mufa", "Mufa"),
        ("nap", "NAP"),
        ("cliente", "Cliente"),
    ]
    TIPOS_CHOICES = [
        ("Horizontal", "Horizontal"),
        ("Vertical", "Vertical"),
        ("Tipo Domo", "Tipo Domo"),
    ]
    BANDEJAS_CHOICES = [
        (1, "numero de bandejas: 1"),
        (2, "numero de bandejas: 2"),
        (3, "numero de bandejas: 3"),
        (4, "numero de bandejas: 4"),
        (5, "numero de bandejas: 5"),
        (6, "numero de bandejas: 6"),
    ]
    FUSIONES_CHOICES = [
        (6, "6 fusiones"),
        (12, "12 fusiones"),
        (24, "24 fusiones"),
        (48, "48 fusiones"),
    ]
    COLORS_CHOICES = [
        ("Azul", "Azul"),
        ("Anaranjado", "Anaranjado"),
        ("Verde", "Verde"),
        ("Cafe", "Cafe"),
        ("Plateado", "Plateado"),
        ("Blanco", "Blanco"),
        ("Rojo", "Rojo"),
        ("Negro", "Negro"),
        ("Amarillo", "Amarillo"),
        ("Violeta", "Violeta"),
        ("Rosa", "Rosa"),
        ("Agua", "Agua"),
    ]
    name = models.CharField(max_length=250, verbose_name="Nombre del Cluster")
    addres = models.CharField(max_length=250, verbose_name="Direccion del Cluster")
    lat = models.FloatField(verbose_name="Latitud")
    Ing = models.FloatField(verbose_name="Longitud")
    c_cluster = models.CharField(
        max_length=10, verbose_name="Codigo del Cluster", null=False, blank=False
    )
    tipo = models.CharField(
        max_length=20, choices=TIPO_CHOICES, default="horizontal", verbose_name="Tipo"
    )
    n_bandejas = models.IntegerField(
        choices=BANDEJAS_CHOICES, default=1, verbose_name="Numero de Bandejas"
    )

    n_fusiones = models.IntegerField(
        choices=FUSIONES_CHOICES, default=1, verbose_name="Numero de Fusiones"
    )
    colors = models.CharField(
        choices=COLORS_CHOICES,
        max_length=20,
        default="Azul",
        verbose_name="Color de Tubo",
    )
    tipos = models.CharField(
        choices=TIPOS_CHOICES,
        max_length=20,
        default="Horizontal",
        verbose_name="Tipo",
    )

    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Bandeja(models.Model):
    PORTS_CHOICES = [
        ("Puerto 1", "Puerto 1"),
        ("Puerto 2", "Puerto 2"),
        ("Puerto 3", "Puerto 3"),
        ("Puerto 4", "Puerto 4"),
        ("Puerto 5", "Puerto 5"),
        ("Puerto 6", "Puerto 6"),
    ]

    COLORS_CHOICES = [
        ("Azul", "Azul"),
        ("Anaranjado", "Anaranjado"),
        ("Verde", "Verde"),
        ("Cafe", "Cafe"),
        ("Plateado", "Plateado"),
        ("Blanco", "Blanco"),
        ("Rojo", "Rojo"),
        ("Negro", "Negro"),
        ("Amarillo", "Amarillo"),
        ("Violeta", "Violeta"),
        ("Rosa", "Rosa"),
        ("Agua", "Agua"),
    ]
    servicio = models.CharField(max_length=250, verbose_name="Nombre del Servicio")
    color = models.CharField(
        max_length=20, choices=COLORS_CHOICES, default="Azul", verbose_name="Color"
    )
    perdida = models.FloatField()
    color_salida = models.CharField(
        max_length=20,
        choices=COLORS_CHOICES,
        default="Azul",
        verbose_name="Color Salida",
    )
    servicio_salida = models.CharField(
        max_length=250, verbose_name="Nombre del Servicio de Salida"
    )
    cluster = models.ForeignKey(
        Cluster,
        verbose_name="Cluster",
        on_delete=models.CASCADE,
        related_name="bandejas",
    )


class Ruta(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre de la ruta")
    geojson_data = models.TextField()
    color = models.CharField(max_length=20, default="blue")
    comentario = models.CharField(max_length=255, verbose_name="Comentario de la ruta")

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"
        ordering = ["id"]

    def __str__(self):
        return "Ruta " + self.nombre
