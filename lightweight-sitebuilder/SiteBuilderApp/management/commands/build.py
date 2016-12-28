__author__ = 'Marcelo'

import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand,CommandError
from django.core.urlresolvers import reverse
from django.test.client import Client

def get_pages():
    for name in os.listdir(settings.SITE_PAGES_DIR):
        if name.endswith('.html'):
            yield name[:5]

class Command(BaseCommand):
    help = 'Build static basic output'

    def handle(self, *args, **options):
        """
        Requests pages and get output
        :param args:
        :param options:
        :return:
        """
        print('Command.Build: handle request...')
        settings.DEBUG = False

        if args:
            pages = args
            available = list(get_pages())
            invalid = []
            for page in pages:
                if page not in available:
                    invalid.append(page)
            if invalid:
                msg = 'Invalid pages: {}'.format(', '.join(invalid))
                raise CommandError(msg)
        else:
            if os.path.exists(settings.SITE_OUTPUT_DIR):
                shutil.rmtree(settings.SITE_OUTPUT_DIR)
            os.mkdir(settings.SITE_OUTPUT_DIR)
            os.makedirs(settings.STATIC_ROOT)

            call_command('collectstatic',interactive=False,clear=True,verbosity=0)
            client = Client()
            for page in get_pages():
                print('Command.Build: current page = ',page)
                url = reverse('page',kwargs={'slug': page})
                response = client.get(url)
                if page == 'index':
                    output_dir = settings.SITE_OUTPUT_DIR
                else:
                    output_dir = os.path.join(settings.SITE_OUTPUT_DIR,page)
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)

                with open(os.path.join(output_dir, page + '.html'), 'wb') as f:
                    f.write(response.content)