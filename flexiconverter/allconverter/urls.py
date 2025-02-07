from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.Main,name='main'),
    path('imgtopdf/',views.ImageToPdf,name='imgtopdf'),
    path('download/<str:filename>/',views.download_pdf,name='download_pdf'),
    path('pdftoimg/', views.PdfToImage, name='pdftoimg'),
    path('pdftoword/', views.PdfToWord, name='pdftoword'),
    path('download_word/<str:filename>/', views.download_word, name='download_word'),
    path('wordtopdf/', views.WordToPdf, name='wordtopdf'),
    path('download_pdf/<str:filename>/', views.download_pdf, name='download_pdf'),
    path('pdfmerge/', views.PdfMerge, name='pdfmerge'),
    path('download_pdf/<str:filename>/', views.download_pdf, name='download_pdf'),
    path('pdfcompress/', views.PdfCompress, name='pdfcompress'),
    path('download_pdf/<str:filename>/', views.download_pdf, name='download_pdf'),
    path("contact/", views.contact_view, name="contact"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

