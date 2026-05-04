# Criptoanálise da Cifra de Vigenère

## Objetivo

Recuperar o texto original a partir de um texto cifrado com a Cifra de Vigenère, **sem conhecer a senha**, assumindo que o idioma é português.

## Etapa 1 — Descoberta do Tamanho da Chave

**Ferramenta:** `ic.py`

O **Índice de Coincidência (IC)** mede a probabilidade de duas letras escolhidas aleatoriamente em um texto serem iguais.

- Texto em **português natural**: IC ≈ **0.072**

### Método

1. Para cada tamanho de chave candidato `k` (de 1 a 20), dividimos o texto cifrado em `k` subtextos: o subtexto `i` contém os caracteres nas posições `i, i+k, i+2k, ...`
2. Calculamos o IC de cada subtexto e tiramos a média.
3. Se `k` for o tamanho correto da chave, cada subtexto foi cifrado com um deslocamento fixo, preservando a distribuição do português. Logo, o IC médio será próximo de **0.072**.
4. O valor de `k` que produz o IC médio mais alto é o tamanho mais provável da chave.

### Fórmula do IC

```
IC = Σ fi(fi - 1) / n(n - 1)
```

Onde `fi` é a contagem da letra `i` e `n` é o total de letras no subtexto.

## Etapa 2 — Análise de Frequência

**Ferramenta:** `analise_freq.py`

Com o tamanho da chave definido, precisamos descobrir o deslocamento de cada posição.

### Método

1. Para cada subtexto, calculamos a frequência relativa de cada letra.
2. Para cada deslocamento `d` (0 a 25), calculamos a **correlação** entre a frequência observada (deslocada por `d`) e a frequência esperada do português.
3. O deslocamento com maior correlação é o mais provável. A letra correspondente (`a`=0, `b`=1, ...) é a letra da chave naquela posição.

### Fórmula da Correlação

```
C(d) = Σ freq_obs(c) × freq_pt( (c - d) mod 26 )
```

O `d` que maximiza `C(d)` é o deslocamento correto.

## Etapa 3 — Decifração

**Ferramenta:** `decifrar.py`

Com a chave completa descoberta, aplicamos o inverso da cifra de Vigenère:

```
letra_original = (letra_cifrada - letra_chave) mod 26
```

O texto resultante é o conteúdo original (higienizado: sem acentos, espaços ou pontuação).

## Resumo do Fluxo

```
texto_cifrado.txt
       │
       ▼
01_indice_coincidencia.py  →  tamanho da chave (ex: 5)
       │
       ▼
02_analise_frequencia.py   →  chave descoberta (ex: "senha")
       │
       ▼
03_decifrar.py             →  texto_decifrado.txt
```

## Como Executar

```bash
python cifra.py <texto para cifrar> <senha>
```

```bash
# 1. Descobrir tamanho da chave
python ic.py texto_criptografado.txt

# 2. Descobrir a chave
python analise_freq.py texto_criptografado.txt <tamanho da chave>

# 3. Decifrar
python decifrar.py texto_criptografado.txt <chave encontrada>
```