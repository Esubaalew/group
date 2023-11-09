from django.urls import reverse
from django.db import models

class FocusField(models.Model):
    '''
    A field that a member is focusing on, e.g., Mobile Development.
    '''

    name = models.CharField(max_length=200, verbose_name='FocusField')

    def __str__(self):
        return self.name


class Member(models.Model):
    '''
    A member person.

    Attributes:
        first_name (str): The first name of the member.
        last_name (str): The last name of the member.
        focus_fields (ManyToManyField): Fields a member is focusing on.
        about (str): A brief summary about this person.
    '''

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    focus_fields = models.ManyToManyField(FocusField, help_text='Fields a member is focusing on', verbose_name='Focus Fields')
    about = models.TextField(help_text='A brief summary about this person')
    class Meta:
        ordering = ['first_name','last_name']
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('member_detail', args=[str(self.id)])

