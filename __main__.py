from keybord_escuta import KeyBoard
import ctypes

# Informa ao Windows para não aplicar escala automática no Tkinter (DPI Awareness)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Per Monitor DPI Aware
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()  # Fallback para sistemas mais antigos
    except Exception:
        pass


def main():
    key_escuta = KeyBoard()
    key_escuta.colocando_atalhos()


if __name__ == "__main__":
    main()
