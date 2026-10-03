# 🚀 CyberDeck Search Launcher

Un utilitário de pesquisa rápida leve e modular com estética **Cyberpunk Neon**, desenvolvido em Python e CustomTkinter. O sistema permite disparar janelas popup centralizadas de busca a partir de atalhos globais de teclado, lendo as configurações diretamente de um arquivo JSON.

---

## 🎨 Funcionalidades

* **Atalhos Globais:** Pesquisa rápida disparada por combinações de teclas (ex: `Ctrl + Alt + G`, `Ctrl + Alt + Y`) em qualquer lugar do sistema.
* **Modularidade via JSON:** Adiciona novas plataformas, URLs e atalhos facilmente sem precisar alterar o código Python.
* **Interface Cyberpunk Neon:** Design moderno em tema escuro com destaques em Ciano e Magenta.
* **Suporte a DPI / Resolução:** Tratamento automático de escala no Windows para alinhamento e centralização perfeitos.
* **Usabilidade Fluida:** Feche a janela rapidamente pressionando `Esc` ou confirme a busca direto com `Enter`.

---

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (UI)
* `keyboard` (Captura de atalhos globais)
* `json` (Persistência e configuração)
* `ctypes` (Ajuste de DPI no Windows)

---

## 📂 Estrutura do Arquivo `atalhos_teclado.json`

O comportamento das pesquisas é controlado por um arquivo JSON na raiz do projeto:

```json
{
  "atalhos": [
    {
      "nome": "Google",
      "hotkey": "ctrl+alt+g",
      "url_busca": "[https://www.google.com/search?q=](https://www.google.com/search?q=)"
    },
    {
      "nome": "YouTube",
      "hotkey": "ctrl+alt+y",
      "url_busca": "[https://www.youtube.com/results?search_query=](https://www.youtube.com/results?search_query=)"
    },
    {
      "nome": "Stack Overflow",
      "hotkey": "ctrl+alt+s",
      "url_busca": "[https://stackoverflow.com/search?q=](https://stackoverflow.com/search?q=)"
    }
  ]
}
