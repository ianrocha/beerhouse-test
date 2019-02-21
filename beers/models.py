import os
import random
import string
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 39010209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{}{}'.format(new_filename, ext)
    return 'beers-img/{}/{}'.format(new_filename, final_filename)


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class Beer(models.Model):
    HARMONIZATION_CHOICES = (
        ('Aves', 'Aves'),
        ('Balada', 'Balada'),
        ('Bolinho de Bacalhau', 'Bolinho de Bacalhau'),
        ('Carne de Caça', 'Carne de Caça'),
        ('Chocolate', 'Chocolate'),
        ('Churrasco', 'Churrasco'),
        ('Costelinha de Porco', 'Costelinha de Porco'),
        ('Doces', 'Doces'),
        ('Frutos do Mar', 'Frutos do Mar'),
        ('Hambúrguer', 'Hambúrguer'),
        ('Massas', 'Massas'),
        ('Panna Costa', 'Panna Costa'),
        ('Petiscos de Boteco', 'Petiscos de Boteco'),
        ('Pizza', 'Pizza'),
        ('Queijos', 'Queijos'),
        ('Quitutes Apimentados', 'Quitutes Apimentados'),
        ('Saladas', 'Saladas')
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    harmonization = models.CharField(max_length=25, choices=HARMONIZATION_CHOICES)
    color = models.CharField(max_length=120, blank=True, null=True)
    alcohol_content = models.CharField(max_length=5)
    temperature = models.CharField(max_length=5)
    ingredients = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)

    def __str__(self):
        return self.name


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Beer)
