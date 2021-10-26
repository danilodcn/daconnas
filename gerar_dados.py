from typing import List
from selenium.webdriver.firefox.webdriver import WebDriver
import requests
from random import randint, choice
from time import sleep
import re
import os

IMAGES_DIR = "/home/danilo/Developer/imagens"

# import ipdb; ipdb.set_trace()

def remove_simbols(text):
    return re.sub(r"\D", "", text)

def get_diaristas(n, estado="SP", cidade="rio", pesquisa="rua"):
    url = f"https://random-data-api.com/api/users/random_user?size={n}"
    all_diaristas = requests.get(url).json()
    # import ipdb; ipdb.set_trace()
    url_ceps = f"https://viacep.com.br/ws/{estado}/{cidade}/{pesquisa}/json/"
    ceps_json = requests.get(url_ceps).json()
    ceps = [remove_simbols(cep_json["cep"]) for cep_json in ceps_json]
    ceps = ["65930000"]
    # print(ceps)

    diaristas = []
    for diarista in all_diaristas:
        dia = {
            "nome_completo": diarista["first_name"] + " " + diarista["last_name"],
            "cpf": remove_simbols(diarista["credit_card"]["cc_number"]),
            "email": diarista["email"],
            "telefone": remove_simbols(diarista["phone_number"]),
            "logradouro": diarista["address"]["street_name"],
            "numero": remove_simbols(diarista["address"]["zip_code"][:3]),
            "bairro": diarista["address"]["street_address"],
            "complemento": diarista["employment"]["title"],
            "cep": choice(ceps),
            "foto_usuario": os.path.join(IMAGES_DIR, choice(os.listdir(IMAGES_DIR)))
            }
        diaristas.append(dia)

    return diaristas

def inserir_dados(diaristas: List[dict], url: str):
    driver = WebDriver()
    print("Inicio ...")
    for diarista in diaristas:
        nome = diarista["nome_completo"]
        print(f"inserindo a diarista {nome}")
        sleep(.5)
        driver.get(url)
        sleep(.5)
        for name, valor in diarista.items():
            input = driver.find_element_by_name(name)
            sleep(.1)
            input.send_keys(valor)

        sleep(.5)
        driver.find_element_by_xpath("//button[contains(text(), 'Cadastrar') ]").click()

    print("fim ...")
    driver.quit()



url = "https://ediaristaspython.herokuapp.com/web/cadastrar_diarista"
diaristas = get_diaristas(9)
inserir_dados(diaristas, url)