from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from .forms import FormItemNew,FormItemEdit
from .models import Item


# Create your views here.
#view for details page
def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    #get items on the same category
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    
    
    return render(request,'item/detail.html',
                  {
                      'item':item,
                      'related_items':related_items
  
                  })

#View for creating a new item

@login_required
def newItem(request):

    if request.method == 'POST':
        #display items form
        form=FormItemNew(request.POST,request.FILES)
        #check if form is valid
        if form.is_valid():
            #save form
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            #redirect to the details page
            return redirect ('items:detail',pk=item.id)
    else:
             form=FormItemNew()
    
    return render(request,'item/form.html',
                  {
                      'form':form,
                      'title':'New Item',
                  })
#view for delete items

@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('userdashboard:index')

#view for editing items

@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        
        form=FormItemEdit(request.POST,request.FILES,instance=item)
        #check if form is valid
        if form.is_valid():
            #save the form
            item=form.save()
           
            #redirect after saving to details page
            return redirect ('items:detail',pk=item.id)
    else:
             form=FormItemEdit(instance=item)
    
    return render(request,'item/form.html',
                  {
                      'form':form,
                      'title':'Edit Item',
                  })

