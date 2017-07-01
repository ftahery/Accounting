from django.shortcuts import render,redirect
from django.views.generic import View


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