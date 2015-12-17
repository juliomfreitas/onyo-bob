from django.db import models
from datetime import date
from jsonfield import JSONField


class Prize(models.Model):
    draw_date = models.DateField(default=date.today)
    code = models.CharField(max_length=100)

    def __str__(self):
        return "#{} Draw Date {}".format(self.pk, self.draw_date.strftime('%Y-%m-%d'))


class Ticket(models.Model):
    prize = models.ForeignKey(Prize, related_name="tickets")
    numbers = JSONField()
    winning = models.NullBooleanField()
    code = models.CharField(max_length=100)

    def drawed(self):
        return self.winning is not None

    def __str__(self):
        return "Ticket {} - Prize {}".format(str(self.numbers), str(self.prize))
