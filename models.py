from django.db import models

class Soil(models.Model):
    SOIL_TYPES = [
        ('clay', 'Arcilla'),
        ('sand', 'Arena'),
        ('rock', 'Roca')
    ]

    type = models.CharField(max_length=10, choices=SOIL_TYPES)
    density = models.FloatField(help_text="Densidad (kg/m³)")
    elasticity = models.FloatField(help_text="Módulo de Elasticidad (Pa)")
    poisson_ratio = models.FloatField(help_text="Relación de Poisson")

    def __str__(self):
        return f"{self.get_type_display()}"

class SeismicSignal(models.Model):
    frequency = models.FloatField(help_text="Frecuencia inicial (Hz)")
    amplitude = models.FloatField(help_text="Amplitud inicial")
    wave_type = models.CharField(max_length=10, choices=[('P', 'Onda P'), ('S', 'Onda S'), ('R', 'Rayleigh')])
    duration = models.FloatField(help_text="Duración de la señal (s)")

    def __str__(self):
        return f"{self.wave_type} - {self.frequency} Hz"
