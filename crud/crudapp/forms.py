from django import forms
from .models import Address
class credaddform(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'
        labels = {
            'add':'Address'
         }
    def __init__(self,*args,**kwargs):
        super(credaddform,self).__init__(*args,**kwargs)
        self.fields['state'].empty_label="Select"