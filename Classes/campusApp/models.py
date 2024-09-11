from django.db import models

# Creates model of University names
class UniversityName(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=False, null=False)
    campus_state = models.CharField(max_length=2, default="", blank=False, null=False)
    campus_id = models.IntegerField(default="", blank=False, null=False)

    # Creates model manager
    objects = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.campus_name}: {0.campus_state}'
        return display_course.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
