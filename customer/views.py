from django.shortcuts import render, redirect
from io import TextIOWrapper
import csv
from .models import Customer
# Create your views here.


def import_data(request):
    print('here request---')
    print(request.FILES['dd'])
    cs = TextIOWrapper(request.FILES['dd'], encoding='utf-8', errors='replace')
    csr = csv.reader(cs)
    csr.__next__()
    for line in csr:
        name = line[0]
        phone = line[1]
        Customer.objects.create(name=name,phone_no=phone)
    return redirect('admin/customer/customer')


def calculate1(request):
    res = None
    if request.method == 'POST':
        x = int(request.POST['input_x'])
        i = int(request.POST['input_i'])
        res = serise_cal_rec(i, x)

    return render(request, 'add_data.html', {'res': res})


def power_num(numb, times):
    res = 1
    for i in range(times):
        res = res * numb
    return res


def serise_cal_rec(i, x):
    if i == 0:
        return 0
    else:
        return 1/power_num(x, i) + serise_cal_rec(i-1, x)


def serise_cal(i, x):
    sum = 0
    for i in range(1, i+1):
        return sum+power_num(x, i)
    return sum


def guess_serise(i):
    # i is number of element in serise
    if i%2 == 0:
        return i*i-1
    else:
        return i * i - 1





def eq_part(a,b,action):
    if action:
        return a+(1/b)
    else:
        return a - (1 / b)


def equation(x,y,a,b):
    res1 = power_num(eq_part(x, y, True), a)
    res1 *= power_num(eq_part(x, y, False), b)
    res2 = power_num(eq_part(y, x, True), a)
    res2 *= power_num(eq_part(y, x, False), b)
    return res1/res1


