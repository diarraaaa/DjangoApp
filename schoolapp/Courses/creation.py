import os
import django
import sys

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolapp.settings')

# Setup Django
django.setup()


from Courses.models import Department

biology=Department.objects.create(name='Biology',chief_name='Dr. Smith',id=1)
biology.save()

