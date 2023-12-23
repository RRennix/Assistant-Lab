import os
import winapps
import yaml
def encontrar_caminho(nome):
    aplicativos = list(winapps.search_installed(nome))
    if len(aplicativos) > 0:
        return aplicativos[0].install_location
    else:
        return None

def encontrar_executavel(caminho):
    for raiz, diretorios, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo.endswith('.exe'):
                return os.path.join(raiz, arquivo)
    return None

def adicionar_aplicativo(nome, caminho):
    data = yaml.safe_load(open('path.yml','r',encoding='utf-8').read())
    novo_aplicativo = {'Aplicativo': None, 'Caminho': caminho, 'Nome': nome}
    data['Aplicativos'].append(novo_aplicativo)
    with open('path.yml', 'w') as f:
        yaml.safe_dump(data, f, default_flow_style=False)
def adicionar():
    caminho = encontrar_caminho(input('Pesquisar por:'))
    if caminho is not None:
        print('Aplicativo encontrado com sucesso!')
        nome = input('Adicione o nome:')
        executavel = encontrar_executavel(caminho)
        adicionar_aplicativo(nome, executavel)
        print('Adicionado com sucesso com o nome de '+nome)
    else:
        print('Aplicativo não encontrado, adicione manualmente')
        x = input('Nome:')
        y = input('Caminho:')
        adicionar_aplicativo(x, y)
        print('Adicionado com sucesso com o nome de '+x)