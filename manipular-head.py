import os
from bs4 import BeautifulSoup

# Caminho da pasta contendo os arquivos .html
folder_path = os.path.dirname(os.path.abspath(__file__))

# Lista dos arquivos específicos que você deseja editar
files_to_edit = [
    'carregador-turbo-iphone.html',
    'acessorios-para-iphone.html',
    'carregador-para-iphone.html',
    'carregador-turbo-iphone.html',
    'como-proteger-o-iphone-de-roubo-confira-as-dicas.html',
    'dicas-de-seguranca-iphone-confira.html',
    'economizar-bateria-do-iphone.html',
    'edifier-w800bt-plus-review.html',
    'e-sports-games.html',
    'fone-in-ear.html',
    'iphone-de-vitrine.html',
    'iphone-vs-android.html',
    'jbl-original.html',
    'jogos-para-notebook-confira-5-opcoes.html',
    'melhores-fones-de-ouvido-bluetooth.html',
    'mulheres-gamer.html',
    'o-que-e-um-streamer.html',
    'pelicula-de-privacidade-para-iphone.html',
    'pelicula-para-camera-de-iphone.html',
    'peliculas-para-iphone-13.html',
    'pelicula-x-one-garantia.html',
    'perifericos-gamer.html',
    'poltrona-gamer-x-cadeira-game.html',
    'porque-o-iphone-esquenta-entenda.html',
    'por-que-o-iphone-e-tao-bom.html',
    'quais-sao-os-melhores-fones-de-ouvido-sem-fio.html',
    'setup-gamer-aprenda-como-escolher-e-montar.html',
    'setup-gamer-rosa-dicas-para-montar-o-seu.html',
    'teclado-mecanico-branco-modelos.html',
    'teclado-rgb.html',
    'telegram.html',
    'top-5-melhores-acessorios-para-iphone-em-2022.html',
    'trocar-seu-antigo-celular-pelo-iphone.html'
    
]

# Elemento que você deseja adicionar ao <head>
new_element = '<meta content="Narcipe Viana" name="author"/><meta name="robots" content="index, follow"><script type="text/javascript" async="" src="https://www.googletagmanager.com/gtag/js?id=G-M3QB3YBK2Y&amp;l=dataLayer&amp;cx=c"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script>'


def add_element_to_head(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    
    # Verifica se a tag <head> existe
    head = soup.head
    if head:
        # Adiciona o novo elemento
        new_soup_element = BeautifulSoup(new_element, 'lxml')
        head.append(new_soup_element)
        
        # Salva o arquivo com as alterações
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup.prettify(formatter=None)))
    else:
        print(f"Tag <head> não encontrada em {file_path}")

# Processar apenas os arquivos específicos
for file_name in files_to_edit:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        add_element_to_head(file_path)
        print(f"Elemento adicionado ao <head> de {file_name}")
    else:
        print(f"Arquivo não encontrado: {file_name}")

print("Processo concluído.")
