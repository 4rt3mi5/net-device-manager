from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from node.models import Node, NodeConnect


class NodeListView(LoginRequiredMixin, ListView):
    """节点的列表"""
    template_name = 'node_list.html'
    model = Node


class NodeConnectListView(LoginRequiredMixin, ListView):
    """节点连接列表"""
    template_name = 'node_connect_list.html'
    model = NodeConnect