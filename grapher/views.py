from django.shortcuts import render
from django.http import HttpResponse
from . import graph, geometric_brownian

def invalid(s):
    for c in s:
        if c!='-' and c !='.' and (c<'0' or c>'9'):
            return True
    return False 
# Create your views here.

def std(request):
    D=request.GET
    if len(D)==0:
        return render(request, 'std.html', context={'show':False, 'error':False})
    if invalid(D['drift']) or invalid(D['diff_coeff']):
        return render(request, 'std.html', context={'show':False, 'error':True})
    image=graph.compute( int(D['no_of_points']), int(D['end_point']), int(D['no_of_graphs']), float(D['drift']), float(D['diff_coeff']))
    return render(request, 'std.html', context={'image':image.decode(), 'show':True, 'error':False})  

def geom(request):
    D=request.GET
    if len(D)==0:
        return render(request, 'geom.html', context={'show':False, 'error':False})
    if invalid(D['start_point']) or invalid(D['mean']) or invalid(D['volatility']):
        return render(request, 'geom.html', context={'show':False, 'error':True})
    image=geometric_brownian.compute( int(D['no_of_points']), float(D['start_point']), int(D['end_point']), int(D['no_of_graphs']), float(D['mean']), float(D['volatility']))
    return render(request, 'geom.html', context={'image':image.decode(), 'show':True, 'error':False})  