from flask import Flask, render_template, request, redirect,url_for


app = Flask(__name__)
##TESTE DE EDIÇÂO
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

 #Adicionamos a rota de create
@app.route('/cadastrar')
def criar():
    return render_template("cadastrar.html")

#Método para criar galaxias
@app.route('/criar', methods=['GET', 'POST'])
def criarGalaxia():
    if request.method == 'POST':
        nova_galaxia = {}
        nova_galaxia['nome'] = request.form['nome']
        nova_galaxia['estrelaPrincipal'] = request.form['estrela']
        nova_galaxia['distancia'] = request.form['distancia']
        nova_galaxia['imagem'] = request.form['imagem']
        
        id = gerar_id()
        galaxias[id] = nova_galaxia  # Adiciona a nova galaxia ao dicionario galaxias

        return redirect(url_for('home'))  # Redireciona para a rota 'index'

    else:
        return render_template('cadastrar.html')

#EXCLUSÃO
##Jéssica
@app.route('/deletar/<int:id>', methods=['POST'])  # Captura o ID na URL
def deletarGalaxia(id):
    if id in galaxias:
        del galaxias[id]

    return redirect(url_for('home'))

#ATUALIZAÇÃO DE DADOS
@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    galaxia = galaxias.get(id)
    if galaxia:
        return render_template('editar.html', id=id, galaxia=galaxia)
    return redirect(url_for('home'))

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    if request.method == 'POST' and id in galaxias:
        galaxias[id]['nome'] = request.form['nome']
        galaxias[id]['estrelaPrincipal'] = request.form['estrela']
        galaxias[id]['distancia'] = request.form['distancia']
        galaxias[id]['imagem'] = request.form['imagem']
        return redirect(url_for('home'))
    return 'Galáxia não encontrada!', 404


def listar_galaxias():
    return galaxias


#Como não sabemos o posicionamento, geramos um ID para a nova galaxia quando chamado o método
def gerar_id():
    id = len(galaxias) +1
    return id


if __name__ == '__main__':
    app.run(debug = True)
    


    
#print(listar_galaxias())

#create_galaxy("Hubble","Jupiter","1 milhão","")

#print(listar_galaxias())
