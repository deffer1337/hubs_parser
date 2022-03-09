from django.db import models

from app.internal.models.hub import Hub


class Publication(models.Model):
    """
    Publication model
    """

    header = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    author_name = models.CharField(max_length=255)
    author_url = models.CharField(max_length=255)
    text = models.TextField()
    datetime = models.DateTimeField()
    hub = models.ForeignKey(Hub, on_delete=models.SET_NULL, null=True)

    def get_information(self):
        return (
            f"\n"
            f"--------------------------------------------\n"
            f"Header - {self.header}\n"
            f"Url - {self.url}\n"
            f"Author name - {self.author_name}\n"
            f"Author url - {self.author_url}\n"
            f"Date and time - {self.datetime}\n"
            f"--------------------------------------------"
        )

    def __str__(self):
        return f"{self.header}"
