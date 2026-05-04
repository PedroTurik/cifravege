import sys

def calcular_ic(texto: str) -> float:
    n = len(texto)
    if n <= 1:
        return 0.0
    freq = {}
    for c in texto:
        freq[c] = freq.get(c, 0) + 1
    soma = sum(f * (f - 1) for f in freq.values())
    return soma / (n * (n - 1))


def ic_medio_para_tamanho(texto: str, tamanho_chave: int) -> float:
    subtextos = [""] * tamanho_chave
    for i, c in enumerate(texto):
        subtextos[i % tamanho_chave] += c

    ics = [calcular_ic(s) for s in subtextos]
    return sum(ics) / len(ics)


def main():
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        texto = f.read().strip()

    print(f"Tamanho do texto cifrado: {len(texto)} caracteres\n")
    print(f"{'Tam. chave':>12} | {'IC médio':>10} | Observação")
    print("-" * 50)

    IC_PORTUGUES = 0.072

    melhor_tam = 1
    melhor_ic = 0.0

    for k in range(1, 21):
        ic = ic_medio_para_tamanho(texto, k)
        obs = ""
        if abs(ic - IC_PORTUGUES) < 0.008:
            obs = "<-- próximo do português"
        if ic > melhor_ic:
            melhor_ic = ic
            melhor_tam = k
        print(f"{k:>12} | {ic:>10.6f} | {obs}")

    print(f"\n>>> Tamanho de chave mais provável: {melhor_tam} (IC = {melhor_ic:.6f})")


if __name__ == "__main__":
    main()