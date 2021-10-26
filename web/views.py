from django.shortcuts import render, redirect
from .forms.diarista_form import DiaristaForm
from .models import Diarista

# Create your templates here.

def home_web(requests):
    return redirect("listar_diaristas")


def cadastrar_diarista(request):
    if request.method == 'POST':
        diarista_form = DiaristaForm(request.POST, request.FILES)
        if diarista_form.is_valid():
            diarista_form.save()
            return redirect("listar_diaristas")
    if request.method == "GET":
        diarista_form = DiaristaForm()
        # import ipdb; ipdb.set_trace()

    return render(
        request, "diarista_form.html",
        {"diarista_form": diarista_form, "title": "Inserir Diarista", "btn_name": "Cadastrar"}
    )

def listar_diaristas(request):
    diaristas = Diarista.objects.all()
    return render(
        request, "lista_diaristas.html",
        {"diaristas": diaristas, "title": "Listar Diarista" }
    )

def update_diarista(request, id):
    diarista = Diarista.objects.get(id=id)
    if request.method == "POST":
        diarista_form = DiaristaForm(request.POST or None, request.FILES or None,instance=diarista)
        if diarista_form.is_valid():
            diarista_form.save()
            return redirect('listar_diaristas')
    else:
        diarista_form = DiaristaForm(instance=diarista)
    return render(
        request, 'diarista_form.html',
        {"diarista_form": diarista_form, "btn_name": "Salvar", "title": "Editar Diarista"}
    )

def delete_diarista(request, id):
    diarista = Diarista.objects.get(id=id)
    diarista.delete()
    return redirect("listar_diaristas")