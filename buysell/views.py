import operator
from functools import reduce
from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Product, Category

# home page and search view
class IndexView(generic.ListView):
    template_name = 'buysell/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # add list of categories to context of buysell index view
        context['categories'] = Category.objects.all()
        # get selected categories to maintain selection after submit
        context['q_category'] = self.request.GET.getlist('category')
        context['q_type'] = self.request.GET.getlist('type')
        context['q_keyword'] = self.request.GET.get('keyword') if self.request.GET.get('keyword') else ''
        return context

    def get_queryset(self):
        # prepare paramaters for query
        category = self.request.GET.getlist('category')
        keyword = self.request.GET.get('keyword')
        product_type = self.request.GET.getlist('type')

        # build up query filter for search view
        filters = Q(name__isnull = False)
        if category:
            filters = filters & Q(category__in = category)
        if keyword:
            filters = filters & Q(name__contains = keyword)
        if product_type:
            filters = filters & reduce(operator.or_, (Q(product_type__contains = item) for item in product_type))
        products_list = Product.objects.filter(filters).order_by('-modified_date')

        # add pagination to search results
        paginator = Paginator(products_list, 10)
        page = self.request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        return products

# list of products created/added by current user for dashboard
class UserProductView(generic.ListView):
    template_name = 'buysell/user_product.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(author=self.request.user,).order_by('-modified_date')

# product create form for logged in users
class ProductCreate(CreateView):
    model = Product
    fields = ['name','price','image','category','product_type','description']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(ProductCreate, self).form_valid(form)

# product updated by user
class ProductUpdate(UpdateView):
    model = Product
    fields = ['name','price','image','category','product_type','description']
    success_url = reverse_lazy('buysell:user_product')

    def get_object(self):
        # prevent non authorised users to edit product
        obj = super(ProductUpdate, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj

class ProductDelete(DeleteView):
    model = Product
    # redirect url after delete confirmation
    success_url = reverse_lazy('buysell:user_product')

    def get_object(self):
        # prevent non authorised users to delete product
        obj = super(ProductDelete, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj