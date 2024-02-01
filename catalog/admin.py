# V__I__C__T__O__R_______________________________________________________________Dr.

from django.contrib import admin
from . import models
#_________________________________________________________________________________Dr.
class BookInstanceInline ( admin.TabularInline ):
    model = models.BookInstance
    extra = 2

#_________________________________________________________________________________Dr.
class BookInline ( admin.TabularInline ):
    model = models.Book
    extra = 2

#_________________________________________________________________________________Dr.
@admin.register ( models.Author )
class AuthorAdmin ( admin.ModelAdmin ):
    inlines= [BookInline]
    #_________________________
    list_display = ( 'last_name' , 'first_name' , 'birth_day' , 'death_day' )
    #_________________________
    list_filter = ( 'last_name' , 'birth_day' )
    #_________________________
    fieldsets = (
                    ( 'first & last name', 
                    { 'fields': ('first_name' , 'last_name' ) }
                    ),
                    #_________________________
                    ( 'birth & death day', 
                    { 'fields': ('birth_day' , 'death_day' ) }
                    ),
                )

#_________________________________________________________________________________Dr.
@admin.register ( models.BookInstance )
class BookInstanceAdmin ( admin.ModelAdmin ):
    list_display = ( 'book' , 'status' , 'borrower' , 'due_back' , 'id' )
    #_________________________
    list_filter = ( 'status' , 'due_back' , 'id' )
    #_________________________
    fieldsets = (
                    ( 'information', 
                    { 'fields' : ( 'book','imprint', 'id' ) }
                    ),
                    #_________________________
                    ( 'Availability', 
                    { 'fields' : ( 'status', 'due_back','borrower' ) } 
                    ),
                )

#_________________________________________________________________________________Dr.
@admin.register ( models.Book )
class BookAdmin ( admin.ModelAdmin ):
    inlines = [ BookInstanceInline ]
    #_________________________
    list_display = ('title' , 'author' , 'isbn' )
    #_________________________
    list_filter = ( 'title' , 'author' , 'genre' )
    #_________________________
    fieldsets = (
                    ( 'info', 
                    { 'fields': ( 'title' , 'author' ) } 
                    ),
                    #_________________________
                    ( 'about book', 
                    {'fields': ( 'summary' , 'isbn' , 'genre' ) } 
                    ),
                )
#_________________________________________________________________________________Dr.
@admin.register ( models.Genre )
class GenreAdmin ( admin.ModelAdmin ):
    pass

#_________________________________________________________________________________Dr.
