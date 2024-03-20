from flask import Flask, render_template, request, redirect,url_for


app = Flask(__name__)

# Dicionário para armazenar os dados temporariamente
galaxias= {
    1: {
        "nome": "Via Lactea",
        "estrelaPrincipal": "Sol",
        "distancia": "0",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/1/12/Artist%27s_impression_of_the_Milky_Way_%28updated_-_annotated%29.jpg"
    },
     2: {
        "nome": "Andrômeda",
        "estrelaPrincipal": "Alpheratz",
        "distancia": "2,5 milhões anos luz",
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/8/8e/The_Andromeda_Galaxy_old.jpg"

    }
}

@app.route('/')
def home():
    dicionario = listar_galaxias()
    return render_template('index.html', dados=dicionario)

@app.route('/about')
def about():
    return 'About page'

 #Adicionamos a rota de create
@app.route('/create')
def criar():
    return render_template("criar.html")

#Criamos o método para criar as galaxias
def create_galaxy(nome,estrela,distancia,imagem):
    galaxias[gerar_id()] = {"nome":nome, "estrelaPrincipal":estrela, "distancia":distancia,"imagem":imagem}
    return redirect(url_for('index'))

def listar_galaxias():
    return galaxias

#Como não sabemos o posicionamento, geramos um ID para a nova galaxia quando chamado o método
def gerar_id():
    id = len(galaxias) +1
    return id


if __name__ == '__main__':
    app.run(debug = True)
    





"""@app.route('/create')
def criarGalaxia():
    if request.method == 'POST':
        galaxias = {}
        galaxias['nome'] = request.form['nome']
        galaxias['estrelaPrincipal'] = request.form['estrela']
        galaxias['distancia']  = request.form['distancia']
        galaxias['imagem'] = request.form['imagem']
        return render_template('index.html')
    else:
        return render_template('criar.html', id = gerar_id())"""
    
#print(listar_galaxias())

#create_galaxy("Hubble","Jupiter","1 milhão","")

#print(listar_galaxias())