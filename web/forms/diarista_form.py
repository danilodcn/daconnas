from django import forms
from ..models import Diarista
from ..services.cep_services import buscar_cidade_cep
import re

class DiaristaForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000.000.000-00'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00000-000'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))
    # codigo_ibge = forms.IntegerField(required=False)
    foto_usuario = forms.ImageField(required=False)

    class Meta:
        model = Diarista
        # fields = "__all__"
        exclude = ("codigo_ibge", "estado", "cidade")

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]

        return re.sub(r"\D", '', cpf)

    def clean_telefone(self):
        telefone = self.cleaned_data["telefone"]
        return re.sub(r'\D', '', telefone)

    def clean_cep(self):
        cep = self.cleaned_data["cep"]
        cep = re.sub(r'\D', '', cep)
        response = buscar_cidade_cep(cep)
        if response.status_code == 400:
            raise forms.ValidationError("O CEP informado está incorreto")

        response_json = response.json()
        if "erro" in response_json:
            raise forms.ValidationError("O CEP informado não foi encontrado")

        # # estado: str = self.data.get("estado")
        # # import ipdb; ipdb.set_trace()
        # if estado.upper() != response_json["uf"].upper():
        #     raise forms.ValidationError(f"Esse CEP não pertence ao estado {estado}")

        self.__codigo_ibge = response_json["ibge"]
        self.__estado = response_json["uf"]
        self.__cidade = response_json["localidade"]
        return cep

    def save(self, commit=False):
        instance = super(DiaristaForm, self).save(commit=False)
        instance.codigo_ibge = self.__codigo_ibge
        instance.cidade = self.__cidade
        instance.estado = self.__estado

        instance.save()
        return instance