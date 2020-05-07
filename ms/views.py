from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Gateway
from .forms import NodeForm, GatewayForm

def index(request):
    
    device = Node.objects.all()[:5]
    gateways = Gateway.objects.all()[:5]
    return render(request,'base.html',{'devices': device,'gateways':gateways })

def node(request,id_node):
    device = Node.objects.get(pk = id_node)
    return render(request,'node.html',{'node': device})

def nodes(request):
    device = Node.objects.all()
    return render(request,'nodes.html',{'nodes': device})

def add_node(request):
    if request.method == 'POST':
        form = NodeForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'add_node.html', {'form': form})
    if request.method == 'GET':  
        form = NodeForm()
        return render(request, 'add_node.html', {'form': form})

def add_gateway(request):
    if request.method == 'POST':
        print(request.POST)
        data = {
            'gateway_descriptio':request.POST.get('gateway_descriptio'),
            'gateway_MAC':request.POST.get('gateway_MAC'),
            'gateway_image':request.POST.get('gateway_image'),
        }
        form = GatewayForm(data)
        if form.is_valid():
            form.save()
        return render(request, 'add_node.html', {'form': form})
    if request.method == 'GET':  
        form = GatewayForm()
        return render(request, 'add_node.html', {'form': form})

def gateways(request):
    device = Gateway.objects.all()
    return render(request,'gateways.html',{'gateways': device})
# Create your views here.
