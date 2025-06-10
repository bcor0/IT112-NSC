from django.shortcuts import render

def home(request):
    user_name = request.GET.get('user_name', None)
    context = {'user_name': user_name}
    return render(request, 'myapp/base.html', context)
