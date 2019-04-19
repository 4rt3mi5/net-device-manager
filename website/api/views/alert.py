
from django.views.generic import View
from django.views.generic.edit import BaseDeleteView, BaseFormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import JsonResponse


from website.settings import BASE_DIR


class AlertUsers(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        with open(BASE_DIR + '/users.txt') as f:
            users = f.readlines()
        return JsonResponse({'data': users})
        

    def post(self, requst, *args, **kwargs):
        with open(BASE_DIR + '/users.txt', 'a') as f:
            username = requst.POST.get('username')
            f.write(username + '\n')
        return JsonResponse({'msg':'添加成功'})


class DeleteAlertUser(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        with open(BASE_DIR + '/users.txt') as f:
            users = f.readlines()
            for user in users:
                if username.strip() == user.strip():
                    users.pop(users.index(user))
        with open(BASE_DIR + '/users.txt', 'w') as w:
            w.write(''.join(users))
        return JsonResponse({'msg':'删除成功'})