from django.contrib import admin
from .models import Category, Product

# alter admin product page to save current user as author of content
class ProductAdmin(admin.ModelAdmin):
    # save function triggered on form admin
    def save_model(self, request, obj, form, change):
        # set author as user who created/modified the content
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

# register admin models forms
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
