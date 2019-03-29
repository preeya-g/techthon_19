from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Volunteer,City
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages
from evelist.models import Event,Signup,EventImages
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			cityy=form.cleaned_data['city']
			try:
				t_user=User.objects.filter(username=username).first()
				cittyy=City.objects.filter(name=cityy).first()
				p=Volunteer(user=t_user,my_city=cittyy)
				p.save()
			except:
				new_city=City(name=cityy)
				new_city.save()
				p=Volunteer(user=t_user,my_city=new_city)
				p.save()
			messages.success(request, f'Account created for {username}!')
			return redirect('register')
	else:
			form = UserRegisterForm()
	return render(request, 'volunteer/register.html', {'form': form})


@login_required
def profile(request):
	current_user = request.user
	try:
		v=current_user.volunteer
		e=Event.objects.filter(venue=v.my_city)
		context={
		"Events":e
		}
		return render(request,'volunteer/profile.html',context)
	except:
		return render(request,'organization/home.html')


def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
