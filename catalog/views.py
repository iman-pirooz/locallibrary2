# V__I__C__T__O__R_______________________________________________________________Dr.

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.views import generic
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponse , HttpResponseRedirect
import datetime 
from django.contrib.auth.decorators import permission_required
from .forms import RenewBookForm

#_________________________________________________________________________________Dr.
class index ( generic.TemplateView ):
    template_name = 'catalog/index.html'
    #_________________________
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['num_books']  =  models.Book.objects.all().count()
        context['num_instances']  =  models.BookInstance.objects.all().count()
        context['num_instances_available']  =  models.BookInstance.objects.filter(
                                                                    status__exact='a').count()
        context['num_authors']=             models.Author.objects.count()

        return context

#_________________________________________________________________________________Dr.
class BookListView ( generic.ListView ):    
    model = models.Book
    template_name = 'catalog/book_list.html'

#_________________________________________________________________________________Dr.
class BookDetailView ( generic.DetailView ):
    model = models.Book
    template_name = 'catalog/book_detail.html'
    
#_________________________________________________________________________________Dr.
class AuthorListView ( generic.ListView ) :
    model = models.Author
    template_name = 'catalog/author_list.html'
    
#_________________________________________________________________________________Dr.
class AuthorDetailView ( generic.DetailView ):
    model = models.Author
    template_name = 'catalog/author_detail.html'

#_________________________________________________________________________________Dr.
class LoanedBooksByUserListView ( LoginRequiredMixin,generic.ListView ):
    model= models.BookInstance
    template_name = 'catalog/bookinstance_list_borrowered_user.html'
    paginate_by = 10
    #_________________________
    def get_queryset ( self ):
        return models.BookInstance.objects.filter( borrower=self.request.user ).filter( status__exact='o' ).order_by( 'due_back' )

#_________________________________________________________________________________Dr.
#@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    #View function for renewing a specific BookInstance by librarian
    book_inst=get_object_or_404(models.BookInstance, pk = pk)
    #_________________________
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)
    #_________________________
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('catalog:my-borrowered') )
    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
    #_________________________
    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})

#_________________________________________________________________________________Dr.
class AuthorCreate ( generic.CreateView ):
    model = models.Author
    fields = '__all__' 
    initial = {'date_of_death':'05/01/2018'}
    #_________________________
class AuthorUpdate ( generic.UpdateView ):
    model = models.Author
    fields = ['first_name' , 'last_name' , 'birth_day' , 'death_day']
    #_________________________
class AuthorDelete ( generic.DeleteView ):
    model = models.Author
    success_url = reverse_lazy('catalog:authors')

#_________________________________________________________________________________Dr.

                                #((function base))                  
'''
def index ( request ):
    num_books = models.Book.objects.all().count()
    num_instances = models.BookInstance.objects.all().count()
    num_instances_available = models.BookInstance.objects.filter( status__exact='a' ).count()
    num_authors = models.Author.objects.count()
    return render   ( 
                    request,
                    'catalog/index.html',
                    context= {
                            'num_books':num_books, 
                            'num_instances':num_instances , 
                            'num_instances_available':num_instances_available , 
                            'num_authors':num_authors 
                            }
                    )

'''
#_________________________________________________________________________________Dr.