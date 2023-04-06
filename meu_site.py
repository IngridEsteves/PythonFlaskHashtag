from flask import Flask, render_template

app = Flask(__name__)

# Criar a 1ª página do site
# route -> Qual link vai ficar a página -> O que vem depois do domínio blablabla.com/route
# Função -> O que quer exibir naquela página
# template -> HTML das páginas

@app.route("/") # Definindo a home page como route - Decorator - objetivo de atribuir uma nova funcionalidade para a função que vem logo abaixo
def homepage(): # Função
    return render_template("homepage.html")

# Criando outra página
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

# Criando uma página dinâmica para usuários
@app.route("/usuarios/<nome_usuario>") # <variável>
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Colocar o site no ar
if __name__ == "__main__": # Se esse arquivo for importado por outro arquivo não executa - importante para o deploy
    app.run(debug=True) #Ativando o debugar do site - Todas as edições feitas no código são automaticamente processadas

# Servidor do heroku
# 1º Garanta que o if __name__ = "__main__" existe no seu site
#requirements.txt

