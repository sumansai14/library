# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from books.models import Book, BookUserMap, ReturnRequestList
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
#from books.forms import RegistrationForm


@login_required(login_url='/login')
def index(request):
    books_list = Book.objects.all().values('name', 'slug', 'author').distinct().order_by('name')
    context = {'books_list': books_list}
    return render_to_response('index.html', context, context_instance=RequestContext(request))


@login_required(login_url='/login')
def book(request, book_slug):
    book = Book.objects.filter(slug=book_slug).filter(is_issued=False)
    if book:
        count = book.count()
        context = {'book': book[0], 'count': count}
        return render_to_response('book.html', context, context_instance=RequestContext(request))
    else:
        book = Book.objects.filter(slug=book_slug)
        if book:
            count = 0
            context = {'book': book[0], 'count': count}
            return render_to_response('book.html', context, context_instance=RequestContext(request))



def request_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user
    test = BookUserMap(book=book, user=user)
    test.save()
    return HttpResponseRedirect('/books/')


def loginview(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/books/')
            else:
                return HttpResponse("you are not a valid user")
        else:
            return HttpResponse("you are not a valid user")
    else:
        context = {}
        context.update(csrf(request))
        return render_to_response('login.html', context, context_instance=RequestContext(request))


def signup(request):
    if (request.method == "POST"):
        #form = RegistrationForm(request.POST)
        #if (form.is_valid()):
        if not user_exists(request.POST['username']):
            User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        return HttpResponseRedirect('/login/')
    else:
        context = {}
        context.update(csrf(request))
        return render_to_response('signup.html', context, context_instance=RequestContext(request))


def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True


@login_required
def logout_req(request):
    logout(request)
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render_to_response('logout.html')


@login_required
def profile(request):
    issued_list = Book.objects.filter(issued_to=request.user.id)
    request_list = BookUserMap.objects.select_related().filter(user=request.user.id)
    context = {'issued_list': issued_list, 'request_list': request_list}
    return render_to_response('profile.html', context, context_instance=RequestContext(request))


def add_books(request):
    if(request.method == "POST"):
        copies = int(request.POST['number'])
        for x in xrange(0,copies):
            book = Book(name=request.POST['book'],author=request.POST['author'])
            book.slug = slugify(request.POST['book'])
            book.save()      
        text = "Book/s Created"
        context = {'text': text}
        return render_to_response('addbooks.html', context, context_instance=RequestContext(request))
    else:
        context = {}
        return render_to_response('addbooks.html', context, context_instance=RequestContext(request))


def requests(request):
    issue_request_list = BookUserMap.objects.all().select_related()
    return_request_list = ReturnRequestList.objects.all().select_related()
    context = {'issue_request_list': issue_request_list, 'return_request_list': return_request_list}
    return render_to_response('requests.html', context, context_instance=RequestContext(request))


def issue(request, book_id, user_id):
    requested_book = Book.objects.get(id=book_id)
    #assert False, "%s"%requested_book
    requested_user = User.objects.get(id=user_id)
    requested_book.issued_to = requested_user
    requested_book.is_issued = True
    requested_book.save()
    BookUserMap.objects.filter(book=requested_book, user=requested_user)[0].delete()
    #text = "Book Issued"
    #context = {'text': text
       #             }
    return HttpResponseRedirect('/requests')
