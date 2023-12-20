from django import forms

from .models import Item

CLASS_DESIGN='w-full py-4 px-6 rounded-xl border'
class FormItemNew(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image')

        widgets={
            'category':forms.Select(attrs=
                            {
                                'class':CLASS_DESIGN
                            }),
            'name':forms.Textarea(attrs=
                            {
                                'class':CLASS_DESIGN
                            }),
            'description':forms.Textarea(attrs=
                            {
                                'class':CLASS_DESIGN
                            }),
            'price':forms.TextInput(attrs=
                            {
                                'class':CLASS_DESIGN
                            }),
            'image':forms.FileInput(attrs=
                            {
                                'class':CLASS_DESIGN
                            })
            
            
            
            
            
        }

CLASS_DESIGN='w-full py-4 px-6 rounded-xl border'
class FormItemEdit(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','price','image','is_sold')

        widgets={
            
            'name':forms.Textarea(attrs=
                            {
                                'class':CLASS_DESIGN
                            }),
            'description':forms.Textarea(attrs=
                            {
                                'class':CLASS_DESIGN
                            }),
            'price':forms.TextInput(attrs=
                            {
                                'class':CLASS_DESIGN
                            }),
            'image':forms.FileInput(attrs=
                            {
                                'class':CLASS_DESIGN
                            })
            
            
            
            
            
        }