import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# Template HTML
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta name="description" content="{description}" />
    <meta name="author" content="" />
    <title>{title}</title>
    <link rel="icon" type="image/x-icon" href="img/icon-Lojas-kalfen-Logo-32x32.png" />
    <link href="css/styles.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
    <script type="application/ld+json">
        {{
          "@context": "https://schema.org",
          "@type": "BlogPosting",
          "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "https://blog-lojaskalfen.com.br/{nome_arquivo}"
          }},
          "headline": "{title}",
          "image": "", 
          "author": {{
            "@type": "Person",
            "name": "Narcipe Viana"
          }},
          "publisher": {{
            "@type": "Organization",
            "name": "Lokas kalfen",
            "logo": {{
              "@type": "ImageObject",
              "url": "https://blog-lojaskalfen.com.br/{imagem_campo}"
            }}
          }},
          "datePublished": "{date_published}",
          "dateModified": "{date_published}",
          "description": "{meta_description}",
          "articleBody": "{article_body}"
        }}
    </script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark cor-do-menu">
        <div class="container">
            <a class="navbar-brand" href="#!"><img src="img/Logo-lojas-Kalfen.png" alt="Logo-lojas-Kalfen"></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="/sobre">Sobre</a></li>
                    <li class="nav-item"><a class="nav-link" href="/contato">Contato</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-5">
        <div class="row">
            <div class="col-lg-8">
                <article>
                    <header class="mb-4">
                        <h1 class="fw-bolder mb-1">{titulo_post}</h1>
                        <div class="text-muted fst-italic mb-2"> Publicado em {meta_info}</div>
                        <a class="badge bg-secondary text-decoration-none link-light" href="#!">SEO</a>
                    </header>
                    <figure class="mb-4"><img class="img-fluid rounded" src="{imagem_post}" alt="SEO, ou Search Engine Optimization" /></figure>
                    <div>
                        {conteudo}
                    </div>
                </article>
            </div>
            <div class="col-lg-4">
                <div class="card mb-4">
                    <div class="card-header">Pesquise</div>
                    <div class="card-body">
                        <div class="input-group">
                            <input class="form-control" type="text" placeholder="digite o que deseja..." aria-label="Enter search term..." aria-describedby="button-search" />
                            <button class="btn btn-primary" id="button-search" type="button">Go!</button>
                        </div>
                    </div>
                </div>
                <div class="card mb-4">
                    <div class="card-header">Categories</div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-6">
                                <ul class="list-unstyled mb-0">
                                    <li><a href="#!">Web Design</a></li>
                                    <li><a href="#!">HTML</a></li>
                                    <li><a href="#!">Freebies</a></li>
                                </ul>
                            </div>
                            <div class="col-sm-6">
                                <ul class="list-unstyled mb-0">
                                    <li><a href="#!">JavaScript</a></li>
                                    <li><a href="#!">CSS</a></li>
                                    <li><a href="#!">Tutorials</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card mb-4">
                    <div class="card-header">Leia também</div>
                    <div class="card-body">
                        <p> <a href="/dicas-de-seguranca-iphone-confira">Dicas de segurança para iphone</a></p>
                    </div>
                </div>
                <div class="card mb-4">
                    <div class="card-header">Compartilhe</div>
                    <div class="card-body">
                        <div class="sharethis-inline-share-buttons"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <footer class="py-5 cor-do-menu">
        <div class="container">
            <p class="m-0 text-center text-white">Todos os direitos reservados Lojas Kalfen</p>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/scripts.js"></script>
</body>
</html>
"""

data = {}

def save_data(description, title, nome_arquivo, meta_description, imagem_campo, date, titulo_post, imagem_post, conteudo):
    global data
    date_published = datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
    meta_info = date
    data = {
        "description": description,
        "title": title,
        "nome_arquivo": nome_arquivo,
        "meta_description": meta_description,
        "imagem_campo": imagem_campo,
        "date_published": date_published,
        "titulo_post": titulo_post,
        "meta_info": meta_info,
        "imagem_post": imagem_post,
        "conteudo": conteudo
    }
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

def generate_html():
    global data
    article_body = f"<article>{data['conteudo']}</article>"
    html_content = html_template.format(
        description=data['description'],
        title=data['title'],
        nome_arquivo=data['nome_arquivo'],
        meta_description=data['meta_description'],
        imagem_campo=data['imagem_campo'],
        date_published=data['date_published'],
        article_body=article_body,
        titulo_post=data['titulo_post'],
        meta_info=data['meta_info'],
        imagem_post=data['imagem_post'],
        conteudo=data['conteudo']
    )
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        messagebox.showinfo("Sucesso", "Arquivo HTML gerado com sucesso!")

def create_interface():
    root = tk.Tk()
    root.title("Gerador de HTML")
    root.geometry("600x600")

    labels = ["Descrição", "Título", "Nome do Arquivo", "Meta Descrição", "Imagem Campo", "Data de Publicação (DD-MM-YYYY)", "Título do Post", "Imagem do Post", "Conteúdo"]
    entries = []

    for label in labels:
        frame = tk.Frame(root)
        frame.pack(fill='x', pady=5)
        lbl = tk.Label(frame, text=label, width=25)
        lbl.pack(side='left', padx=5)
        entry = tk.Entry(frame)
        entry.pack(fill='x', expand=True, padx=5)
        entries.append(entry)
    
    save_data_button = tk.Button(root, text="Salvar Dados", command=lambda: save_data(
        entries[0].get(),  # description
        entries[1].get(),  # title
        entries[2].get(),  # nome_arquivo
        entries[3].get(),  # meta_description
        entries[4].get(),  # imagem_campo
        entries[5].get(),  # date
        entries[6].get(),  # titulo_post
        entries[7].get(),  # imagem_post
        entries[8].get()   # conteudo
    ))
    save_data_button.pack(pady=10)

    generate_html_button = tk.Button(root, text="Gerar HTML", command=generate_html)
    generate_html_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_interface()
