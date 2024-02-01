# V__I__C__T__O__R_______________________________________________________________Dr.

from django.urls import path , re_path
from . import views

#_________________________________________________________________________________Dr.
app_name = 'catalog'
    #_________________________
urlpatterns = [
        path( '', views.index.as_view() , name= 'index' ),
        #_________________________
        re_path ( r'^books/$' , views.BookListView.as_view() , name= 'books' ),
        #_________________________
        re_path ( r'^book/(?P<pk>\d+)$', 
                                    views.BookDetailView.as_view() , 
                                    name= 'book-detail' 
                ),
        #_________________________
        re_path ( r'^author/$' , 
                            views.AuthorListView.as_view() ,
                            name= 'author' 
                ),
        #_________________________
        re_path ( r'^mybooks/$' , 
                            views.LoanedBooksByUserListView.as_view() , 
                            name= 'my-borrowered' 
                ),
        #_________________________
        re_path ( r'^book/(?P<pk>[-\w]+)/renew/$',
                                            views.renew_book_librarian, 
                                            name='renew-book-librarian'
                ),
        #_________________________
]

#_________________________________________________________________________________Dr.
