"""
Etapa 3 — Decifrar o texto com a chave descoberta

Aplica o inverso da cifra de Vigenère: subtrai o deslocamento da chave
em vez de somar.
"""

import sys


def decifrar_vigenere(texto: str, chave: str) -> str:
    resultado = []
    for i, c in enumerate(texto):
        deslocamento = ord(chave[i % len(chave)]) - ord('a')
        original = chr((ord(c) - ord('a') - deslocamento) % 26 + ord('a'))
        resultado.append(original)
    return "".join(resultado)


def main():
    if len(sys.argv) < 3:
        print("Uso: python 03_decifrar.py <texto_cifrado.txt> <chave>")
        print("  A chave pode ser a descoberta pelo script 02 ou digitada manualmente.")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        texto = f.read().strip()

    chave = sys.argv[2].lower()

    texto_decifrado = decifrar_vigenere(texto, chave)

    arquivo_saida = "texto_decifrado.txt"
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(texto_decifrado)

    # Mostrar preview
    preview = texto_decifrado[:500]
    print(f"Chave utilizada: {chave}")
    print(f"Texto decifrado salvo em '{arquivo_saida}'\n")
    print(f"--- Preview (500 primeiros caracteres) ---")
    print(preview)


if __name__ == "__main__":
    main()