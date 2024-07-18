from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm


# Create your views here.

def booklistview(request):
    bookqueryset = Book.objects.all()

    if request.GET.get('search'):
        bookqueryset = Book.objects.filter(title__icontains=request.GET.get('search'))

    form = BookForm()
    context = {
        'books' : bookqueryset,
        'form' : form
    }
    return render(request,'myapp/booklist.html',context)


def addbookview(request):
    if request.method=='POST':
        formdata = BookForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Book Added Successfully")
            return redirect('booklistview')
        messages.error(request,"Somthing Went Wrong")
        return redirect('booklistview')
        
def updatebook(request,pk):
    book_object = Book.objects.get(pk=pk)
    if request.method=='POST':
        title_ = request.POST.get('title')
        author_ = request.POST.get('author')

        book_object.title = title_
        book_object.autor = author_
        book_object.save()
        messages.success(request,"Details Updated Successfully")
        return redirect('booklistview')
        

def deletebook(request,pk):
    if request.method=='POST':
        book_object = Book.objects.get(pk=pk)   
        book_object.delete()
        messages.success(request,"Book Deleted Successfully")
        return redirect('booklistview')