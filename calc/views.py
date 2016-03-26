from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def calc_start(request) :
    return HttpResponse ('Iniciando Calculadora')

def calc_sum(request,num1,num2) :
    suma = int(num1) + int(num2)
    return HttpResponse ('La suma de es:' + str(suma) )


def calc_res(request,num1,num2) :
    resta = int(num1)-int(num2)
    return HttpResponse ('La resta es:' + str(resta))

def calc_mul(request,num1,num2) :
    mul = int(num1) * int(num2)
    return HttpResponse ('La multiplicacion es :' + str(mul))

def calc_div(request,num1,num2) :
    div = int(num1) / int (num2)
    return HttpResponse ('La division es : ' + str(div))

def Error(request):
    return HttpResponse ('404 Not Found : Invalid URL')
