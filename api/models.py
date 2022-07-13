import datetime

from django.db import models as m


class Employee(m.Model):
    firstname = m.CharField(max_length=100)
    lastname = m.CharField(max_length=100)
    position = m.CharField(max_length=100)
    date_submitted = m.DateField(default=datetime.datetime.now())
    salary = m.IntegerField()
    ref_employee = m.ForeignKey('self', null=True, blank=True, on_delete=m.CASCADE)
    # ref_employee = m.ForeignKey('self', null=True, blank=True, on_delete=m.CASCADE)

    def __str__(self):
        return self.position
