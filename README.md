# Jogo Da Matemática
O Jogo Da Matemática é um jogo de matemática usando as 4 operações básicas (soma, subtração, multiplicação e divisão) escrito na linguagem de programação Python.
Ele contém um sistema de save onde quando se encerra o programa (dando Ctrl+C) ele salva automaticamente o recorde.
Ele também contém um sistema que aumenta a dificuldade conforme mais pontos tiver:  
0-9 Pontos: Soma  
10-19 Pontos: Subtração  
20-29 Pontos: Multiplicação  
\>=30 Pontos: Divisão  
## Dependências
Este projeto depende do Python e da lib appdirs que pode ser instalada utilizando este comando (se estiver utilizando Arch Linux ou derivados):
```bash
sudo pacman -S python-appdirs
```
ou utilizando este comando (qualquer Linux):
```bash
mkdir venv
python -m venv venv
source venv/bin/activate
pip install -r requeriments.txt
```
## Instalação
Você pode instalar utilizando este comando:
```bash
sudo cp main.py /usr/local/bin/jogo_da_matematica # Copia o codigo para um arquivo em /usr/local/bin
sudo chmod +x /usr/local/bin/jogo_da_matematica # Dá permissão de execução ao arquivo
```
mas se você quiser apenas executar sem instalar você pode utilizar esse comando:
```bash
python main.py
```
## Objetivo Do Projeto
A ideia desse projeto não é ser um projeto completo ou robusto, mas sim ser um projeto simples e educacional
