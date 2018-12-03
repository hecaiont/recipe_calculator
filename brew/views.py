from django.shortcuts import render
# from django.http import HttpResponse

# from django.template import loader
from django.utils import timezone
from .models import recipe


# def index(request):
#     template = loader.get_template('brew/index.html')
#     context = {
#         'latest_question_list': "test",
#     }
#     return HttpResponse(template.render(context, request))



def recipe_list(request):
    recipes = recipe.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'brew/recipe_list.html', {'recipes': recipes})

