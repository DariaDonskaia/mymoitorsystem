from django.shortcuts import render
from django.http import HttpResponse
from .models import Node, Gateway, Node_Data, Type
from .forms import NodeForm, GatewayForm
import json

def index(request):
    if request.is_ajax():
        id = request.POST.get('id')
        x = request.POST.get('node_x')
        y = request.POST.get('node_y')
        node = Node.objects.get(pk=id)
        node.node_x = x
        node.node_y = y
        node.save()
        return HttpResponse(json.dumps({'result' : result}),content_type="application/json")
    gate = request.GET.get('gateway')
    print(gate)
    
    gateways = Gateway.objects.all()[:5]
    
    if gate:
        selected = Gateway.objects.get(id = gate)
        device = Gateway.objects.get(id = gate).gateway_node.all()
    else:
        selected = Gateway.objects.get(id = 1)
        device = Gateway.objects.get(id = 1).gateway_node.all()
    
    return render(request,'base.html',{'devices': device,'gateways':gateways, 'selected': selected})

def node(request,id_node):
    device = Node.objects.get(pk = id_node)
    if Node_Data.objects.filter(node_data_node = id_node).exists():
        data = Node_Data.objects.filter(node_data_node = id_node)[:5]
    else:
        data = []
    return render(request,'node.html',{'node': device, 'data':data})

def nodes(request):
    if request.is_ajax():
        name = request.POST.get('type_name')
        type_n = Type(type_name=name)
        type_n.save()
        return HttpResponse(json.dumps({'result' : result}),content_type="application/json")
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
        form = GatewayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'add_node.html', {'form': form})
    if request.method == 'GET':  
        form = GatewayForm()
        return render(request, 'add_node.html', {'form': form})


   

def edit(request, id):
    
    device = Node.objects.get(pk=id)
 
    return render(request, "edit.html", {'node': device})
  
def gateways(request):
    device = Gateway.objects.all()
    return render(request,'gateways.html',{'gateways': device})
# Create your views here.
