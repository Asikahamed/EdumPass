from django.conf import settings
from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Categories'

"""class Project(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)


    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'http://bulma.io/images/placeholders/1280x960.png'
    
    

class Lesson(models.Model):
    project = models.ForeignKey(Project, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    
    youtube_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title"""
    


class Project(models.Model):
    DRAFT = 'draft'
    IN_REVIEW = 'in_review'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (IN_REVIEW, 'In review'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    
    VIDEO = 'video'

    CHOICES_LESSON_TYPE = (
        (ARTICLE, 'Article'),
       
        (VIDEO, 'video')
    )

    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=DRAFT)

    lesson_type = models.CharField(max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)

   

    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'http://bulma.io/images/placeholders/1280x960.png'

    
class Lesson(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    
    VIDEO = 'video'

    CHOICES_LESSON_TYPE = (
        (ARTICLE, 'Article'),
       
        (VIDEO, 'video')
    )

    project = models.ForeignKey(Project, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    lesson_type = models.CharField(max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title