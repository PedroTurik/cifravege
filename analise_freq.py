"""
Etapa 2 — Análise de Frequência

Sabendo o tamanho da chave, dividimos o texto em subtextos (um por posição).
Cada subtexto é uma cifra de César simples. Para cada um, testamos os 26
deslocamentos possíveis e escolhemos o que produz uma distribuição de
frequência mais próxima do português (via correlação / chi-quadrado).
"""

import sys

# Frequência esperada das letras em português (fonte: norma linguística)
FREQ_PT = {
    'a': 0.1463, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499,
    'e': 0.1257, 'f': 0.0102, 'g': 0.0130, 'h': 0.0078,
    'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278,
    'm': 0.0474, 'n': 0.0505, 'o': 0.1073, 'p': 0.0252,
    'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434,
    'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021,
    'y': 0.0001, 'z': 0.0047,
}


def frequencias(texto: str) -> dict:
    """Retorna a frequência relativa de cada letra no texto."""
    n = len(texto)
    if n == 0:
        return {c: 0.0 for c in "abcdefghijklmnopqrstuvwxyz"}
    cont = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
    for c in texto:
        cont[c] += 1
    return {c: cont[c] / n for c in cont}


def correlacao(freq_obs: dict, deslocamento: int) -> float:
    """
    Calcula a correlação (soma dos produtos) entre a frequência observada
    deslocada e a frequência esperada do português.
    Quanto maior, melhor o encaixe.
    """
    soma = 0.0
    for c in "abcdefghijklmnopqrstuvwxyz":
        # Letra original antes da cifra: (c - deslocamento) mod 26
        idx_original = (ord(c) - ord('a') - deslocamento) % 26
        letra_original = chr(idx_original + ord('a'))
        soma += freq_obs[c] * FREQ_PT[letra_original]
    return soma


def descobrir_deslocamento(subtexto: str) -> tuple:
    """Testa os 26 deslocamentos e retorna o melhor (deslocamento, letra, score)."""
    freq = frequencias(subtexto)
    melhor = (0, 'a', 0.0)
    for d in range(26):
        score = correlacao(freq, d)
        if score > melhor[2]:
            melhor = (d, chr(d + ord('a')), score)
    return melhor


def main():
    if len(sys.argv) < 3:
        print("Uso: python 02_analise_frequencia.py <texto_cifrado.txt> <tamanho_chave>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        texto = f.read().strip()

    tam_chave = int(sys.argv[2])

    # Dividir em subtextos
    subtextos = [""] * tam_chave
    for i, c in enumerate(texto):
        subtextos[i % tam_chave] += c

    print(f"Tamanho da chave: {tam_chave}")
    print(f"Tamanho do texto: {len(texto)} caracteres\n")

    chave = []
    print(f"{'Posição':>8} | {'Desloc.':>8} | {'Letra':>6} | {'Score':>8}")
    print("-" * 45)

    for i, sub in enumerate(subtextos):
        desloc, letra, score = descobrir_deslocamento(sub)
        chave.append(letra)
        print(f"{i:>8} | {desloc:>8} | {letra:>6} | {score:>8.6f}")

    chave_str = "".join(chave)
    print(f"\n>>> Chave descoberta: {chave_str}")

    # Mostrar top-3 candidatos para cada posição (para análise manual)
    print("\n--- Top 3 candidatos por posição ---")
    for i, sub in enumerate(subtextos):
        freq = frequencias(sub)
        candidatos = []
        for d in range(26):
            score = correlacao(freq, d)
            candidatos.append((d, chr(d + ord('a')), score))
        candidatos.sort(key=lambda x: -x[2])
        top3 = ", ".join(f"{c[1]}({c[2]:.4f})" for c in candidatos[:3])
        print(f"  Posição {i}: {top3}")


if __name__ == "__main__":
    main()