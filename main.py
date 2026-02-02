#!/usr/bin/env python3
import random, appdirs, os, pathlib
pontos = 0
user_data_dir = appdirs.user_data_dir()
jogo_da_matematica_data_dir = f"{user_data_dir}/jogo_da_matematica"
os.makedirs(jogo_da_matematica_data_dir, exist_ok=True)
save = pathlib.Path(f"{jogo_da_matematica_data_dir}/save.txt")
if save.exists():
    with open(f"{jogo_da_matematica_data_dir}/save.txt") as f:
        recorde = int(f.read())
else:
    save.touch()
    recorde = 0
print("Olá, Vamos Treinar Matemática?")
try:   
    while True:
        if pontos < 10:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            resposta_correta = a + b
            resposta = int(input(f"Quanto é {a} + {b}? "))
            if resposta == resposta_correta:
                print("Você Acertou!")
                pontos += 1
                if pontos > recorde:
                    recorde = pontos
            else:
                print(f"Você Errou! A resposta era: {resposta_correta}")
        elif pontos >= 10 and pontos < 20:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            resposta_correta = a - b
            resposta = int(input(f"Quanto é {a} - {b}? "))
            if resposta == resposta_correta:
                print("Você Acertou!")
                pontos += 1
                if pontos > recorde:
                    recorde = pontos
            else:
                print(f"Você Errou! A resposta era {resposta_correta}")
        elif pontos >= 20 and pontos < 30:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            resposta_correta = a * b
            resposta = int(input(f"Quanto é {a} * {b}? "))
            if resposta == resposta_correta:
                print("Você Acertou!")
                pontos += 1
                if pontos > recorde:
                    recorde = pontos
            else:
                print(f"Você Errou! A resposta era {resposta_correta}")
        elif pontos >= 30:
            b = random.randint(2, 10)
            q = random.randint(1, 10)
            a = b * q
            resposta_correta = a / b
            resposta = int(input(f"Quanto é {a} / {b}? "))
            if resposta == resposta_correta:
                print("Você Acertou!")
                pontos += 1
                if pontos > recorde:
                    recorde = pontos
            else:
                print(f"Você Errou! A resposta era {resposta_correta}")
        print(f"Pontos: {pontos}")        
        print(f"Recorde: {recorde}")
except KeyboardInterrupt:
    with open(f"{jogo_da_matematica_data_dir}/save.txt", "w") as f:
        f.write(str(recorde))