from django.db import models
from .food import Food


def tag_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<filename>
    return 'tags/{0}'.format(filename)


class Tag(models.Model):

    title = models.CharField(max_length=255, default='')
    is_main = models.BooleanField(default=False)
    is_primary = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    food = models.ManyToManyField(Food, related_name="tags")
    image = models.ImageField(upload_to=tag_directory_path, null=True)


    def get_image(self):
        if not self.image:
            return 'no-image'
        return self.image.url
