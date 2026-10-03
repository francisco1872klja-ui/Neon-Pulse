import keyboard as key
import json
from pesquisa_dashbord import *


def abrir_janela(nome: str, url: str):
    app = JanelaGenerica(nome, url)

    app.mainloop()


class KeyBoard:

    def __init__(self):
        self.atalhos = []

    def colocando_atalhos(self):
        with open("atalhos.json", "r", encoding="utf-8") as arquivo:
            atalhos = json.load(arquivo)["atalhos"][0:]

        for atalho in atalhos:
            if "hotkey" in atalho:
                self.atalhos.append(
                    key.add_hotkey(
                        atalho["hotkey"],
                        lambda x=atalho["nome"], y=atalho["url_busca"]: abrir_janela(
                            x, y
                        ),
                    )
                )

        key.wait()
