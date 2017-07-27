from django.shortcuts import render,redirect
from django.views.generic import View
from highcharts.views import HighChartsBarView

import random


# Create your views here.

class Index(View):

    template_name = 'accounting/home.html'

    def get(self, request):
        return render(request,self.template_name)

class Invoice(View):

    template_name = 'accounting/invoice.html'

    def get(self,request):
        return render(request, self.template_name)

class About(View):

    template_name = 'accounting/about.html'

    def get(self, request):
        return render(request,self.template_name)

class Inventory(View):

    template_name = 'accounting/inventory.html'

    def get(self, request):
        return render(request,self.template_name)

class Dashboard(View):
    template_name = 'accounting/dashboard/orders.html'

    def get(self, request):
        return render(request, self.template_name)

class Customers(View):
    template_name = 'accounting/customers.html'

    def get(self, request):
        return render(request, self.template_name)

class Items(View):
    template_name = 'accounting/dashboard/items.html'

    def get(self, request):
        return render(request, self.template_name)

class Analytics(View):
    template_name = 'accounting/dashboard/analytics.html'

    def get(self, request):
        return render(request, self.template_name)

'''
class BarView(HighChartsBarView):
    categories = ['Orange', 'Bananas', 'Apples']

    @property
    def series(self):
        result = []
        for name in ('Joe', 'Jack', 'William', 'Averell'):
            data = []
            for x in range(len(self.categories)):
                data.append(random.randint(0, 10))
            result.append({'name': name, "data": data})
        return result
'''