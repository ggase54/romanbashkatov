from django.core.management.base import BaseCommand
from service.models import Post

class Command(BaseCommand):

  def handle(self, *args, **kwargs):
    Post.objects.create(title='check', description='str_1')
    Post.objects.create(title='check', description='str_2')
    Post.objects.create(title='check', description='str_3')
    Post.objects.create(title='check', description='str_4')
    Post.objects.create(title='check', description='str_5')
    print('Check_posts created!')