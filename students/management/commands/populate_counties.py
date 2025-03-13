from django.core.management.base import BaseCommand
from prac.students.models import County, SubCounty

class Command(BaseCommand):
    help = 'Populate counties and subcounties table with predefined data'

    def handle(self, *args, **kwargs):
        county_data = {
            "Nairobi": ["Westlands", "Lang'ata", "Dagoretti", "Embakasi", "Kasarani"],
            "Mombasa": ["Mvita", "Changamwe", "Kisauni", "Nyali"],
            "Kisumu": ["Kisumu East", "Kisumu West", "Nyando", "Muhoroni"],
            "Nakuru": ["Nakuru Town East", "Nakuru Town West", "Rongai"],
            "Kiambu": ["Kiambu Town", "Thika Town", "Juja", "Ruiru"],
        }

        for county_name, subcounties in county_data.items():
            county, created = County.objects.get_or_create(name=county_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added County: {county_name}'))

            for subcounty_name in subcounties:
                subcounty, sub_created = SubCounty.objects.get_or_create(name=subcounty_name, county=county)
                if sub_created:
                    self.stdout.write(self.style.SUCCESS(f'  - Added SubCounty: {subcounty_name}'))
