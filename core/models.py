from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(
        max_length=50,
        help_text="Bootstrap Icon class e.g. bi-truck"
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title

class QuoteRequest(models.Model):

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    service = models.ForeignKey(
    Service,
    on_delete=models.CASCADE
)

    message = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class ContactMessage(models.Model):

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name    