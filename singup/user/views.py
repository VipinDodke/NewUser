from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import User,UserCreationForm
class CreateUserView(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'user/create.html',context={'form':form})

    def post(self,request):
        bound_form = UserCreationForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()
            #return render(request,'blog/index.html',context={'user':new_user})
            return render(request,'user/login.html',context={'user':new_user})
        return render(request,'user/create.html',context={'form': bound_form})

