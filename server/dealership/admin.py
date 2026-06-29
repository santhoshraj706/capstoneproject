from django.contrib import admin
from .models import CarMake, CarModel, CarDealer, DealerReview


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description']


class CarDealerAdmin(admin.ModelAdmin):
    list_display = ['dealer_id', 'full_name', 'city', 'state']
    list_filter = ['state', 'city']
    search_fields = ['full_name', 'city', 'state']


class DealerReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'dealership', 'sentiment', 'purchase']
    list_filter = ['sentiment', 'purchase']
    search_fields = ['name', 'review']


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
admin.site.register(CarDealer, CarDealerAdmin)
admin.site.register(DealerReview, DealerReviewAdmin)
