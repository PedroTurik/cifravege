import unicodedata
import re
import sys


def higienizar(texto: str) -> str:
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z]", "", texto)
    return texto


def cifrar_vigenere(texto: str, chave: str) -> str:
    resultado = []
    for i, c in enumerate(texto):
        deslocamento = ord(chave[i % len(chave)]) - ord("a")
        cifrado = chr((ord(c) - ord("a") + deslocamento) % 26 + ord("a"))
        resultado.append(cifrado)
    return "".join(resultado)


def main():

    with open(sys.argv[1], "r") as f:
        texto_original = f.read()

    texto_limpo = higienizar(texto_original)
    texto_cifrado = cifrar_vigenere(texto_limpo, higienizar(sys.argv[2]))

    with open("texto_criptografado.txt", "w", encoding="utf-8") as f:
        f.write(texto_cifrado)
    
main()
