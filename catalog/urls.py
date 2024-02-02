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
        
        re_path ( r'^author/$' , 
                    views.AuthorDetailView.as_view() ,
                    name= 'author_detail' 
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
        re_path ( r'^author/create/$' , 
                                    views.AuthorCreate.as_view() , 
                                    name= 'author_create' ),
        #_________________________
        re_path ( r'^author/(?P<pk>\d+)/update/$', 
                                            views.AuthorUpdate.as_view() , 
                                            name= 'author_update' 
                ),
        #_________________________
        re_path ( r'^author/(?P<pk>\d+)/delete/$', 
                                            views.AuthorDelete.as_view() , 
                                            name= 'author_delete' 
                ),
]

#_________________________________________________________________________________Dr.
