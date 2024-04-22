import os
import sys
import json

with open('data.json', 'r') as f:
    data = json.load(f)

id_exercicio=0

if sys.argv[1]=="criar":
    
    def criar_pasta(caminho):
        if not os.path.exists(caminho):
            os.makedirs(caminho)
            print(f"Criada a pasta: {caminho}")
        else:
            print(f"A pasta já existe: {caminho}")

    def criar_arquivo(caminho, conteudo):
        if not os.path.exists(caminho):
            with open(caminho, 'w') as arquivo:
                arquivo.write(conteudo)
            print(f"Criado o arquivo: {caminho}")
        else:
            print(f"O arquivo já existe: {caminho}")

    def criar_exercicio(competicao, modalidade, fase, nome_exercicio, id_exercicio):
        global caminho_exercicio
        competicao="".join(competicao.split(" ")).upper()
        primeiro_nome=nome_exercicio.split(" ")[0].lower();
        caminho_competicao = f"../{competicao}/"
        caminho_modalidade = f"../{competicao}/{modalidade}/"
        caminho_fase = f"../{competicao}/{modalidade}/{fase}/"
        caminho_exercicio = f"../{competicao}/{modalidade}/{fase}/{primeiro_nome}/"
        # Criar pasta da competição se não existir
        criar_pasta(caminho_competicao)

        # Criar pasta da modalidade se não existir
        criar_pasta(caminho_modalidade)

        # Criar pasta da fase se não existir
        criar_pasta(caminho_fase)

        # Criar pasta do exercício se não existir
        criar_pasta(caminho_exercicio)

        # Criar arquivo readme.txt
        conteudo_readme = f"{nome_exercicio}\n{id_exercicio}\n"
        readme_path = f"{caminho_exercicio}readme.txt"
        criar_arquivo(readme_path, conteudo_readme)

        # Criar arquivo .cpp
        conteudo_cpp = f"// Codigo para o exercicio {nome_exercicio} (ID: {id_exercicio})\n"
        cpp_path = f"{caminho_exercicio}{primeiro_nome}.cpp"
        criar_arquivo(cpp_path, conteudo_cpp)

        # Criar arquivo start.bat
        conteudo_bat = f'g++ {primeiro_nome}.cpp -o {primeiro_nome}\n{primeiro_nome}'
        bat_path = f"{caminho_exercicio}start.bat"
        criar_arquivo(bat_path, conteudo_bat)

        # Criar arquivo input.txt
        input_txt = ""
        bat_path = f"{caminho_exercicio}input.txt"
        criar_arquivo(bat_path, input_txt)

    # Exemplo de uso
    competicao = input("Digite o nome da competição: ")
    modalidade = input("Digite a modalidade: ")
    fase = input("Digite a fase: ")
    nome_exercicio = input("Digite o nome do exercício: ")
    id_exercicio = input("Digite o ID do exercício: ")

    criar_exercicio(competicao, modalidade, fase, nome_exercicio, id_exercicio)
        
    data[id_exercicio]=caminho_exercicio

    with open("ir.bat", 'w') as arquivo:
        arquivo.write("cd "+data[id_exercicio])
    
    with open("data.json", 'w') as arquivo:
        json.dump(data, arquivo, indent=4)

else: 
    if(data[sys.argv[2]]):
        with open("ir.bat", 'w') as arquivo:
            arquivo.write("cd "+data[sys.argv[2]])
    else:
        print('ainda nao existe pasta para exercício '+sys.argv[2])