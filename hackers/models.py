from django.db import models


class School(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Campus(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hackathon(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EventEdition(models.Model):

    name = models.CharField()
    edition = models.IntegerField()

    def __str__(self):
        return self.name


class Hacker(models.Model):

    # Step 1
    email = models.EmailField()

    # Step 2
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    
    age = models.IntegerField(null=True)

    male = models.BooleanField(default=False)
    female = models.BooleanField(default=False)

    phone_number = models.CharField(max_length=30, blank=True)

    # Step 3
    school = models.ForeignKey(School, null=True)
    campus = models.ForeignKey(Campus, null=True)
    school_id = models.CharField(max_length=50, blank=True)

    E_LEVELS = (
        ('Secundaria', 'Secundaria'),
        ('Preparatoria', 'Preparatoria'),
        ('Bachillerato', 'Bachillerato'),
        ('Maestría', 'Maestría'),
        ('Doctorado', 'Doctorado'),
    )
    education_level = models.CharField(choices=E_LEVELS, blank=True, max_length=20)
    major = models.CharField(max_length=80, blank=True)

    school_join_date = models.DateField(null=True)
    school_graduation_date = models.DateField(null=True)

    T_SHIRT_SIZES = (
        ('Chica - Mujer', 'S-W'),
        ('Mediana - Mujer', 'M-W'),
        ('Grande - Mujer', 'L-W'),
        ('Extra Grande - Mujer', 'XL-W'),
        ('Chica - Hombre', 'S-M'),
        ('Mediana - Hombre', 'M-M'),
        ('Grande - Hombre', 'L-M'),
        ('Extra Grande - Hombre', 'XL-M'),
    )

    tshirt_size = models.CharField(choices=T_SHIRT_SIZES, blank=True, max_length=60)

    dietary_restrictions = models.TextField(blank=True)

    first_time_hacker = models.BooleanField(default=True)
    hackathons = models.ManyToManyField(Hackathon, null=True, blank=True)

    first_time_event = models.BooleanField(default=True)
    event_participations = models.ManyToManyField(EventEdition, null=True, blank=True)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
