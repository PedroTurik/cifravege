import sys

def decifrar_vigenere(texto: str, chave: str) -> str:
    resultado = []
    for i, c in enumerate(texto):
        deslocamento = ord(chave[i % len(chave)]) - ord('a')
        original = chr((ord(c) - ord('a') - deslocamento) % 26 + ord('a'))
        resultado.append(original)
    return "".join(resultado)

def main():

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        texto = f.read().strip()

    chave = sys.argv[2].lower()
    texto_decifrado = decifrar_vigenere(texto, chave)
    
    arquivo_saida = "texto_decifrado.txt"
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(texto_decifrado)

    print(f"Chave utilizada: {chave}")
    print(f"Texto decifrado salvo em '{arquivo_saida}'\n")

if __name__ == "__main__":
    main()