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

#Método salvar o Id da galaxia
@app.route('/galaxy_update/<int:id>')
def update_galaxia(id):
        galaxia = retornar_galaxia(id)
        galaxia['id'] = id
        return render_template('update.html', **galaxia)

#Função para devolver uma única galaxia para atualização
def retornar_galaxia(id:int):
    if id in galaxias.keys():
        return galaxias[id]
    else:
        return {}
    
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
