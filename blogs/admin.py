from django.contrib import admin
from blogs import models
import csv
from django.shortcuts import render, redirect
from django.urls import path
from .models import Blog
from .forms import CsvImportForm
# Register your models here.
admin.site.register(models.contactTable)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'is_published']
    change_list_template = "admin/blog_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return my_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            form = CsvImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES["csv_file"]
                decoded_file = csv_file.read().decode("utf-8").splitlines()
                reader = csv.DictReader(decoded_file)

                for row in reader:
                    Blog.objects.create(
                        title=row['title'],
                        slug=row.get('slug') or None,
                        author=row['author'],
                        content=row['content'],
                        is_published=row.get('is_published', 'True') == 'True'
                    )
                self.message_user(request, "Your blogs were successfully uploaded!")
                return redirect("..")
        else:
            form = CsvImportForm()

        return render(request, "admin/csv_form.html", {"form": form})
