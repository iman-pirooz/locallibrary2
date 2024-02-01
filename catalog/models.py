from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

class Author ( models.Model ):
    first_name  =    models.CharField ( max_length= 100 , help_text= 'first name' )
    last_name   =    models.CharField ( max_length= 100 , help_text= 'last name' )
    birth_day   =    models.DateField ( null= True , blank= True )
    death_day   =    models.DateField ( null= True , blank= True )

    def __str__(self):
        return '%s , %s' % ( self.first_name , self.last_name )

    def get_absolute_url ( self ): 
        return ( reverse ( 'catalog:author-detail', args= [str( self.id )] ) )
    
    
class BookInstance ( models.Model ):
    id         =     models.UUIDField ( primary_key= True , default= uuid.uuid4 , help_text= 'unique code for particular book' )
    book       =     models.ForeignKey ( 'Book' , on_delete= models.SET_NULL , null= True )
    imprint    =     models.CharField ( max_length= 100 , help_text= 'imprints book' )
    due_back   =     models.DateField ( null= True , blank= True )

    LOAN_STATUS = (
        ('m' , 'Maintenance'),
        ('o' , 'On loan'),
        ('a' , 'Available'),
        ('r' , 'Reserved'),
    )
    status     =   models.CharField ( max_length= 1 , choices= LOAN_STATUS , blank= True , default= 'a' , help_text= 'selected in tuple (m,a,r,o)' )
    borrower   =   models.ForeignKey ( User , on_delete= models.SET_NULL , null= True , blank= True )
    
    class Meta:
        ordering = ['due_back']
        
    def __str__ ( self ):
        return '%s , %s' % ( self.book.title , self.id )
    
    @property
    def is_overduo ( self ):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    
    
    
class Book ( models.Model ):
    title     =    models.CharField ( max_length= 100 , help_text= 'titles book' )
    author    =    models.ForeignKey ( 'Author' , on_delete= models.SET_NULL , null= True )
    summary   =    models.TextField ( max_length= 1000 , help_text= 'summarys book' )
    isbn      =    models.CharField ( max_length= 13 , help_text= 'isbn book' )
    genre     =    models.ManyToManyField ( 'Genre' , help_text= 'genres book' )
    
    def __str__ ( self ):
        return '%s , %s' % ( self.title , self.author )
    
    def get_absolute_url ( self ):
        return ( reverse ( 'catalog:book-detail', args= [str( self.id )] ) )
class Genre ( models.Model ):
    name      =    models.CharField ( max_length= 100 , help_text= 'genres book' )
    
    def __str__ ( self ):
        return ( self.name )