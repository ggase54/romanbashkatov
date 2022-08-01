from django.core.management.base import BaseCommand
from service.models import Post

class Command(BaseCommand):
    
    help = 'Checking DB'

    def add_arguments(self, parser):
        parser.add_argument('post_ids', help='post id', type=int, nargs='+')    
    
    def handle(self, *args, **kwargs):
        post_ids = kwargs['post_ids']
        for post_id in post_ids:
            try:
                Post.objects.get(pk=post_id)
                self.stdout.write(self.style.SUCCESS("post with pk = '%s' exist" % post_id))
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR("post with pk = '%s' is not found" % post_id))