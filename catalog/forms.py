# V__I__C__T__O__R_______________________________________________________________Dr.

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

#_________________________________________________________________________________Dr.
class RenewBookForm ( forms.Form ):
    renewal_date    =   forms.DateField ( help_text= 'enter a date between(default 3)' )
    #_________________________
    def clean_renewal_date ( self ):
        data = self.cleaned_data['renewal_date']
        
        if data < datetime.date.today():
            raise ValidationError ('invalid date - renewal in past')
        
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('invalid data - renewal more than 4 weeks ahead'))
        
        return data
    
#_________________________________________________________________________________Dr.
