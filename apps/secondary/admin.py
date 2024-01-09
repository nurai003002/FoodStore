from django.contrib import admin
from apps.secondary import models
# Register your models here.

class AchievementFilterAdmin(admin.ModelAdmin):
    list_filter = ('name1', )
    list_display = ('name1', 'descriptions')
    search_fields = ('name1', 'descriptions')

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')

class BakeryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

class MenuFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

class CategoriesFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )

class DiscountFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

class ClientsAll(admin.TabularInline):
    model = models.ClientsInline
    extra = 1

class ClientsFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions1',)
    list_display = ('descriptions1' ,)
    search_fields = ('descriptions1' ,)
    inlines = [ClientsAll]

class LastPostFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions', )
    list_display = ('descriptions', )
    search_fields = ('descriptions', )

class BigCategoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )


class ReviewFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(models.Wishlist)
admin.site.register(models.Review, ReviewFilterAdmin)
admin.site.register(models.News, NewsFilterAdmin)
admin.site.register(models.Food)
admin.site.register(models.BigCategory, BigCategoryFilterAdmin)
admin.site.register(models.SlideAbout)
admin.site.register(models.LastPost, LastPostFilterAdmin)
admin.site.register(models.AllFood)
admin.site.register(models.Clients, ClientsFilterAdmin)
admin.site.register(models.Discount, DiscountFilterAdmin)
admin.site.register(models.Menu, MenuFilterAdmin)
admin.site.register(models.Category, CategoriesFilterAdmin)
admin.site.register(models.Bakery, BakeryFilterAdmin)
admin.site.register(models.Achievement, AchievementFilterAdmin)
admin.site.register(models.Slide, SlideFilterAdmin)