from django.shortcuts import render, redirect
from django.http import JsonResponse
from core.common.common import get_form, get_model
from core.forms.forms import UserForm, User

# Create your views here.

def create(request, name: str):
    name = name.lower()
    routes = ["user", "speaker", "topic", "post", "publication"]
    if name not in routes:
        return JsonResponse({"error": f'Route not in {routes}'})
    Form = get_form(name)
    # import ipdb; ipdb.set_trace()
    # print(Form)

    if request.method == "POST":
        form = Form(request.POST, request.FILES)
        # form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/web/list/{name}")

    if request.method == "GET":
        form = Form()
        # user = User()
        # import ipdb;
        # ipdb.set_trace()

    button_name = "Register"

    return render(request, "core/form.html", context={
        "form": form,
        "title": "Daconnas - Create {}".format(name.title()),
        "btn_name": button_name
    })


def list(request, name: str):
    name = name.lower()
    routes = ["user", "speaker", "topic", "post", "publication"]
    if name not in routes:
        return JsonResponse({"error": f'Route not in {routes}'})
    Model = get_model(name)
    # print(Model)
    field_names = [field.name for field in Model._meta.fields]
    data = [[getattr(obj, field) for field in field_names] for obj in Model.objects.all()]
    # print(field_names)

    # import ipdb;
    # ipdb.set_trace()
    return render(request, "core/list.html", context={
        "data": data,
        "field_names": field_names,
        "title": "Daconnas - List {}".format(name.title()),
        "name": name.lower(),
    })


def update(request, name: str, id:str):
    name = name.lower()
    routes = ["user", "speaker", "topic", "post", "publication"]
    if name not in routes:
        return JsonResponse({"error": f'Route not in {routes}'})

    Form = get_form(name)
    Model = get_model(name)
    model = Model.objects.get(id=id)

    # import ipdb;
    # ipdb.set_trace()

    if request.method == "POST":
        form = Form(request.POST or None, request.FILES or None, instance=model)
        # form = UserForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect(f"/web/list/{name}")
    else:
        form = Form(instance=model)

    button_name = "Update"

    return render(request, "core/form.html", context={
        "form": form,
        "title": "Daconnas - Update {}".format(name.title()),
        "btn_name": button_name
    })


def delete(request, name: str, id:str):
    name = name.lower()
    routes = ["user", "speaker", "topic", "post", "publication"]
    if name not in routes:
        return JsonResponse({"error": f'Route not in {routes}'})
    Model = get_model(name)
    model = Model.objects.get(id=id)
    model.delete()
    return redirect(f"/web/list/{name}")
