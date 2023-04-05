from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    print(request.method)
    if request.method == 'POST':
        r = request.POST
        # print(request.POST)
        # print(request.POST.get('cars'))          # returns the name of a single car 
        # print(request.POST.getlist('cars'))        # returns the names of multiple cars in a list 
        bid = r.get('book_id')
        name = r.get('book_name')
        qty = r.get('book_qty')
        price = r.get('book_price')
        author = r.get('book_author')
        is_pub = r.get('book_is_published')
        print(request.POST)
        # print(name, qty, price, author, is_pub)
        if is_pub == 'Yes':
            is_pub = True
        else:
            is_pub = False

        if not bid:
            Book.objects.create(name=name, qty=qty, price=price, author=author, is_published=is_pub)
        else:
            book_obj = Book.objects.get(id=bid)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published=is_pub
            book_obj.save()
            

        return redirect('home')
        # return HttpResponse('Success')
    elif request.method == 'GET':
        # print(request.GET)
        return render(request, 'home.html')
        # return render(request, 'home.html', context={'all_books': Book.objects.all()}) # context is a dynamic data to display this on ui we need to add it to our html page as {{person_name}}

def show_books(request):
    return render(request, 'show_books.html', context={'books': Book.objects.filter(is_active=True)})

def update_books(request, id):
    return render(request, 'home.html', context={'single_book': Book.objects.get(id=id)})

def delete_books(request, id):                                  # this is hard delete which is removes records from database too 
    Book.objects.get(id=id).delete()
    return redirect('show_active_books')
    

def soft_delete_books(request, id):                                  # this is hard delete which is removes records from database too 
    book_obj = Book.objects.get(id=id)
    book_obj.is_active = False
    book_obj.save()
    return redirect('show_inactive_books')

def show_inactive_books(request):
    return render(request, 'show_books.html', context={'books': Book.objects.filter(is_active=False),  'inactive':True})

def restore_books(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_active = True
    book_obj.save()
    return redirect('show_active_books')
    