from django.shortcuts import render
from pApp.models import user,slips


def showProfile(request):
      all_user = user.objects.all()
      slips_list = slips.objects.all()
      return render(request, 'showProfile.html', {'all_user': all_user,'slips_list': slips_list})