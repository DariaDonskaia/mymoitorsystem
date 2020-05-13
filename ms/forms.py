from django import forms
from .models import Node, Gateway
from django.utils.translation import gettext_lazy as _

NODE_CHOICES =( 
    
) 

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ('node_description','node_MAC','node_type')
        labels = {
            'node_description': _('Описание'),
            'node_MAC': _('MAC'),
            'node_type': _('Тип узла'),
        }

class GatewayForm(forms.ModelForm):
    class Meta:
        model = Gateway
        fields = ('gateway_description', 'gateway_MAC', 'gateway_image', 'gateway_node')
        labels = {
            'gateway_description': _('Описание'),
            'gateway_MAC': _('MAC'),
            'gateway_image': _('Изображение'),
            'gateway_node':_('Узлы'),
        }