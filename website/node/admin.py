from django.contrib import admin

from node.models import Node, NodeConnect
# Register your models here.


class NodeDisplayList(admin.ModelAdmin):
    list_display = ('name', 'show_name', 'hint', 'type', 'x', 'y')


admin.site.register(Node, NodeDisplayList)
admin.site.register(NodeConnect)
