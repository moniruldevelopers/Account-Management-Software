from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    
    path("books/upload/", book_upload_view, name="book_upload"),
    path("books/download-format/", download_book_format, name="download_book_format"),

    path("books/", book_list_view, name="book_list"),
    path("books/export/", export_books_to_excel, name="export_books"),


    path('library-records/', LibraryRecordListView.as_view(), name='libraryrecord_list'),
    path('library-records/add/', LibraryRecordCreateView.as_view(), name='libraryrecord_add'),
    path('library-records/edit/<int:pk>/', LibraryRecordUpdateView.as_view(), name='libraryrecord_edit'),
    path('library-records/delete/<int:pk>/', LibraryRecordDeleteView.as_view(), name='libraryrecord_delete'),
]
