from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import View

from node.models import Node


class GetNodeStatus(LoginRequiredMixin, View):
    """获得节点的状态"""

    def get(self, request, *args, **kwargs):
        result = {}
        for node in Node.objects.all():
            if node.type in ['switch','router','firewall']:
                status = cache.get(node.hint)
                result[node.name] = {'ip':node.hint,'status':status}
        return JsonResponse(result)