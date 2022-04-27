from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Person

from django_tables2 import SingleTableView
from .table import PersonTable

class PersonListView(ListView):
    model = Person
    template_name = 'table.html'


class PersonListView2(SingleTableView):
    model = Person
    table = PersonTable # pagination
    table_class = PersonTable
    template_name = 'table2.html'

