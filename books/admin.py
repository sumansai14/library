from django.contrib import admin
from books.models import Book, BookUserMap, ReturnRequestList


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(BookUserMap)
admin.site.register(ReturnRequestList)
