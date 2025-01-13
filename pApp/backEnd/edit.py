from django.shortcuts import redirect, render

from pApp.models import user


def Edit(request,userId):
    if request.method == "POST":
        _user = user.objects.get(id=userId)
        _user.name = request.POST['name']
        _user.lastName = request.POST['lastName'] 
        _user.save()

 
        return redirect("/showProfile")
    else:
        #get edit data
        _user = user.objects.get(id=userId)
        return render(request,"Edit.html",{"user":_user})
