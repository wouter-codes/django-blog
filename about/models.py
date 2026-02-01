from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        formatted_date = self.updated_on.strftime("%Y-%m-%d %H:%M")
        return f"{self.title} | updated on {formatted_date}"