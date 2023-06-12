from django.db import models
import uuid
from users.models import Profile

# class User(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False)
#     username = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username


# class Message(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False)
#     sender = models.CharField(max_length=200)
#     recipient = models.CharField(max_length=200)
#     name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200)
#     subject = models.CharField(max_length=200)
#     body = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.sender

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    # Many to One Relationship for the Profile
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    """This will fix the proper character for the Title in the database"""

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # owner = models.ForeignKey()
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
