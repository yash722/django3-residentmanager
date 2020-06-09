from django.shortcuts import render, redirect, get_object_or_404
from .forms import OutgoingForm, VisitorForm, IsolatedForm
from .models import Resident, visitor
from django.utils import timezone
from accounts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request, 'management_system/home.html', {})
def aboutme(request):
    return render(request,'management_system/aboutme.html',{})
#Resident



def outgoing_entryform(request):
    if request.method == "GET":
        return render(request, 'management_system/outgoing_entryform.html', {'form':OutgoingForm()})
    else:
        if len(request.POST['mobile_no']) != 10:
            return render(request, 'management_system/outgoing_entryform.html', {'form':OutgoingForm(), 'error':'Invalid mobile number. Please try again!'})
        if request.POST['mobile_no'].isalpha() == True:
            return render(request, 'management_system/outgoing_entryform.html', {'form':OutgoingForm(), 'error':'Invalid mobile number. Please try again!'})
        else:
            form = OutgoingForm(request.POST)
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('outgoing_list')

def outgoing_list(request):
    people = Resident.objects.filter(cameback__isnull=True, corona_screening_positive=False, user=request.user)
    return render(request, 'management_system/outgoing_entrylist.html', {'people':people})

def outgoing_info(request, person_pk):
    if request.method == "GET":
        person = get_object_or_404(Resident, pk=person_pk,user=request.user)
        return render(request, 'management_system/outgoing_info.html', {'person':person})

def visitorreturn(request, person_pk):
    person = get_object_or_404(Resident, pk=person_pk,user=request.user)
    if request.method == "POST":
        person.cameback = timezone.now()
        person.save()
        return redirect('returned')

def returned(request):
    people = Resident.objects.filter(cameback__isnull=False, corona_screening_positive=False,user=request.user)
    return render(request, 'management_system/returned.html', {'people':people})

def returned_info(request, person_pk):
    person = get_object_or_404(Resident, pk=person_pk,user=request.user)
    return render(request, 'management_system/returned_info.html', {'person':person})

def positive(request, person_pk):
    person = get_object_or_404(Resident, pk=person_pk,user=request.user)
    if request.method == "POST":
        person.cameback = timezone.now()
        person.corona_screening_positive = True
        person.save()
        return redirect('isolated')

def isolate(request):
    people = Resident.objects.filter(corona_screening_positive = True, user=request.user)
    return render(request, 'management_system/isolated.html', {'people':people})

def isolated_remove(request, person_pk):
    person = get_object_or_404(Resident, pk=person_pk, user=request.user)
    if request.method == "POST":
        person.delete()
        return redirect('isolated')
    else:
        return render(request, 'management_system/isolated_remove.html', {'person':person})

def isolate_entryform(request):
    if request.method == "GET":
        return render(request, 'management_system/isolate_entryform.html', {'form':IsolatedForm()})
    else:
        form = IsolatedForm(request.POST)

        newform = form.save(commit=False)
        newform.user = request.user
        newform.save()
        return redirect('isolated')

#Visitors



def visitor_entryform(request):
    if request.method == "GET":
        return render(request, 'management_system/visitor_entryform.html', {'form':VisitorForm()})
    else:
        if len(request.POST['mobile_no']) != 10:
            return render(request, 'management_system/visitor_entryform.html', {'form':VisitorForm(), 'error':'Invalid mobile number. Please try again!'})
        if request.POST['mobile_no'].isalpha() == True:
            return render(request, 'management_system/visitor_entryform.html', {'form':VisitorForm(), 'error':'Invalid mobile number. Please try again!'})
        else:
            form = VisitorForm(request.POST)
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('visitor_list')

def visitor_list(request):
    people = visitor.objects.filter(vis_returned_time__isnull=True,user=request.user)
    return render(request, 'management_system/visitor_entrylist.html', {'people':people})

def visitor_info(request, person_pk):
    if request.method == "GET":
        person = get_object_or_404(visitor, pk=person_pk)
        return render(request, 'management_system/visitor_info.html', {'person':person})


def visitordepart(request, person_pk):
    person = get_object_or_404(visitor, pk=person_pk)
    if request.method == "POST":
        person.vis_returned_time = timezone.now()
        person.save()
        return redirect('departed')

def departed(request):
    people = visitor.objects.filter(vis_returned_time__isnull=False)
    return render(request, 'management_system/departed.html', {'people':people})

def departed_info(request, person_pk):
    person = get_object_or_404(visitor, pk=person_pk)
    return render(request, 'management_system/departed_info.html', {'person':person})
