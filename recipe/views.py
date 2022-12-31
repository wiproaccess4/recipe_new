from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import RecipeForm, ContactForm


@login_required(login_url="/")
def recipe_info(request):
    print(request.user)
    print(request.session["user_name"])
    print(request.session["email"])
    recipes = Recipe.objects.all()
    return render(request, "recipe/recipe_list.html", {
        "recipes": recipes, "name": request.session["user_name"],
        "email": request.session["email"]
    })


def create_recipe(request):
    if request.method == "GET":
        return render(request, "recipe/create_page.html",
                      {"form": RecipeForm(), "contact_form": ContactForm()})
    form_obj = RecipeForm(request.POST)
    contact_obj = ContactForm(request.POST)
    if form_obj.is_valid() and contact_obj.is_valid():
        form_obj.save()
        # Send email
        return HttpResponseRedirect("/recipe/info/")
    else:
        return render(request, "recipe/create_page.html", {"form": RecipeForm(),
                                                           "contact_form": ContactForm(),
                                                           "contact_error": contact_obj.errors,
                                                           "error": form_obj.errors})
    # if request.POST.get("name") and request.POST.get("ingredients") and request.POST.get("process"):
    #     Recipe.objects.create(name=request.POST.get("name"),
    #                           ingredients=request.POST.get("ingredients"),
    #                           process=request.POST.get("process"))
    #     return HttpResponseRedirect("/recipe/info/")
    # else:
    #     pass
    # if not request.POST.get("name"):
    #     return render(request, "recipe/create_page.html", {"error": "Name missing"})
    # elif not request.POST.get("ingredients"):
    #     return render(request, "recipe/create_page.html", {"error": "Ingredients missing"})
    # else:
    #     return render(request, "recipe/create_page.html", {"error": "process missing"})

def contact(request):
    return render(request, "recipe/contact_form.html", {"form": ContactForm()})