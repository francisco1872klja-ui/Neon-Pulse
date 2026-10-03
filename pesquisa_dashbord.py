import customtkinter as ctk
import webbrowser


class JanelaGenerica(ctk.CTk):
    ctk.set_appearance_mode("dark")

    def __init__(self, nome, url):
        self.link_url = url
        super().__init__()
        self.title("Janela Generica")
        self.configure(fg_color="#0F0F1B")
        self.titulo(nome)
        self.centralizar_janela()
        self.barra_pesquisa()
        self.after(100, self.focar_janela)
        self.bind("<Escape>", lambda event: self.destroy())

    def titulo(self, nome_pesquisa):

        self.texto_titulo = ctk.CTkLabel(
            self,
            text=nome_pesquisa,
            font=("Segoe UI", 22, "bold"),
            text_color="#00F5FF",
        )
        self.texto_titulo.pack(pady=(25, 5))

    def barra_pesquisa(self):
        self.freme_pesquisa = ctk.CTkFrame(self, fg_color="transparent")
        self.freme_pesquisa.pack(pady=(5, 20), padx=20, fill="x")

        self.pesquisa_barra = ctk.CTkEntry(
            self.freme_pesquisa,
            placeholder_text="Digite algo...",
            width=200,
            fg_color="#1A1A2E",
            border_color="#00F5FF",
            text_color="#FFFFFF",
            placeholder_text_color="#7A7A9E",
        )
        self.pesquisa_barra.pack(side="left", fill="x", expand=True, padx=(0, 8))

        self.pesquisa_barra.bind("<Return>", self.on_enter)

        self.botao_pesquisa = ctk.CTkButton(
            self.freme_pesquisa,
            text="🔎",
            width=30,
            command=lambda x=self.link_url: self.pesquisa_web(x),
            fg_color="#FF007F",
            hover_color="#D10068",
        )
        self.botao_pesquisa.pack(side="right")

    def pesquisa_web(self, url):
        pesquisa = url + f"{self.pesquisa_barra.get()}"

        webbrowser.open_new(pesquisa)
        self.destroy()

    def focar_janela(self):
        self.attributes("-topmost", True)
        self.update_idletasks()
        self.attributes("-topmost", False)
        self.focus_force()
        self.pesquisa_barra.focus_set()

    def on_enter(self, event):
        self.pesquisa_web(self.link_url)

    def centralizar_janela(self):
        largura_janela, altura_janela = 400, 200
        x = (self.winfo_screenwidth() // 2) - (largura_janela // 2)
        y = (self.winfo_screenheight() // 2) - (altura_janela // 2)

        self.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
