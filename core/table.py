import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
    # name = tables.Column(footer=f"Total:{Person.objects.all().count()}")
    class Meta:
        model = Person
        template_name = "django_tables2/semantic.html"
        fields = ("name", "email", )