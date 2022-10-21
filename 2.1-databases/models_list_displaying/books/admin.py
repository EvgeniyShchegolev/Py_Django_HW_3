from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('pub_date',)}
    list_display = ('name', 'author', 'pub_date', 'slug')


admin.site.register(Book, BookAdmin)
