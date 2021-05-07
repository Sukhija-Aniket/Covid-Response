from django.db import models

# Create your models here.
class Check(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    fever = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    Tiredness = models.BooleanField(default=False)
    _other_symptoms = models.IntegerField(default=0, db_column='other_symptoms')
    breathing_problem = models.BooleanField(default=False)
    chest_pain = models.BooleanField(default=False)

    @property
    def other_symptoms(self):
        return self._other_symptoms

    @other_symptoms.setter
    def other_symptoms(self, count):
        self._other_symptoms = self._other_symptoms + (count-count)

    def is_severe(self):
        count = 0
        if self.breathing_problem or self.chest_pain:
            return True

        if self.fever:
            count = count + 3
        if self.cough:
            count = count + 3
        if self.Tiredness:
            count = count + 3

        if self.other_symptoms + count > 5:
            return True

        elif self.other_symptoms + count > 3:
            return False

        else:
            return False
