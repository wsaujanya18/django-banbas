from django.shortcuts import render, HttpResponse

def reservation_form(request):
    return HttpResponse('Reservation Page')

def reservation_success(request): return render(request, 'reservation/reservation_success.html')
