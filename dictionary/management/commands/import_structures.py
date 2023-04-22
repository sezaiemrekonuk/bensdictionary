import os
import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand
from dictionary.models import Structure, typeOf

class Command(BaseCommand):
    help = 'Import structures from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        filename = options['filename']

        # read CSV file
        df = pd.read_csv(filename).fillna("Eklenecek...")

        created_typeOfs = []

        for _, item in df.iterrows():
            if item['idiom_type'] not in created_typeOfs:
                typeOf(type=item['idiom_type']).save()
                created_typeOfs.append(item['idiom_type'])

        for _, item in df.iterrows():
            obj = Structure(
                structureType=typeOf.objects.get(type=item['idiom_type']),
                turkish=item['idiom_searched'] if item['idiom_searched'] != 'nan' else '',
                english=item['idiom_equivalent'] if item['idiom_equivalent'] != 'nan' else '',
                description=item['idiom_explanation'] if item['idiom_explanation'] != 'nan' else '',
                etymology=item['idiom_etymology'] if item['idiom_etymology'] != 'nan' else '',
                extraInformation=item['idiom_extra_info'] if item['idiom_extra_info'] != 'nan' else '',
                example=item['idiom_example'] if item['idiom_example'] != 'nan' else '',
            )
            obj.save()

        self.stdout.write(self.style.SUCCESS('Import successful!'))
    