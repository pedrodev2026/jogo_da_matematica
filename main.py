#!/usr/bin/env python3
# Gerado por IA
import appdirs
import os
import pathlib
import random


def carregar_recorde(caminho_save):
    if caminho_save.exists():
        with open(caminho_save) as arquivo:
            return int(arquivo.read())
    caminho_save.touch()
    return 0


def salvar_recorde(caminho_save, recorde):
    with open(caminho_save, "w") as arquivo:
        arquivo.write(str(recorde))


def atualizar_recorde(pontos, recorde):
    if pontos > recorde:
        return pontos
    return recorde


def mostrar_menu():
    print("=== JOGO DA MATEMÁTICA ===")
    print("1. Jogar")
    print("2. Sair")
    print("==========================")
    
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                return True
            elif opcao == 2:
                return False
            else:
                print("Opção inválida! Escolha 1 ou 2.")
        except ValueError:
            print("Digite um número válido!")


def obter_pergunta(pontos):
    if pontos < 10:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return a, b, a + b, f"Quanto é {a} + {b}? "
    elif pontos >= 10 and pontos < 20:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return a, b, a - b, f"Quanto é {a} - {b}? "
    elif pontos >= 20 and pontos < 30:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return a, b, a * b, f"Quanto é {a} * {b}? "
    elif pontos >= 30:
        b = random.randint(2, 10)
        q = random.randint(1, 10)
        a = b * q
        return a, b, a / b, f"Quanto é {a} / {b}? "


def jogar():
    pontos = 0
    user_data_dir = appdirs.user_data_dir()
    jogo_da_matematica_data_dir = f"{user_data_dir}/jogo_da_matematica"
    os.makedirs(jogo_da_matematica_data_dir, exist_ok=True)
    save = pathlib.Path(f"{jogo_da_matematica_data_dir}/save.txt")
    recorde = carregar_recorde(save)
    print("Olá, Vamos Treinar Matemática?")
    try:
        while True:
            a, b, resposta_correta, pergunta = obter_pergunta(pontos)
            resposta = int(input(pergunta))
            if resposta == resposta_correta:
                print("Você Acertou!")
                pontos += 1
                recorde = atualizar_recorde(pontos, recorde)
            else:
                if pontos < 10:
                    print(f"Você Errou! A resposta era: {resposta_correta}")
                else:
                    print(f"Você Errou! A resposta era {resposta_correta}")
            print(f"Pontos: {pontos}")
            print(f"Recorde: {recorde}")
    except KeyboardInterrupt:
        salvar_recorde(save, recorde)


if __name__ == "__main__":
    if mostrar_menu():
        jogar()
    else:
        print("Obrigado por jogar!")
