from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask(__name__)

lembretes = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/criar-lembrete', methods=['POST'])
def criar_lembrete():
    nome = request.form.get('nome')
    data = request.form.get('data')

    if nome and data:
        try:
            data_formatada = datetime.strptime(data, '%Y-%m-%d')
            if data_formatada > datetime.now():
                lembrete = {'nome': nome, 'data': data}
                lembretes.append(lembrete)
                return redirect('/?sucesso=true')
            else:
                return redirect('/?erro=data_invalida')
        except ValueError:
            return redirect('/?erro=data_invalida')

    return redirect('/')

@app.route('/meus-lembretes')
def meus_lembretes():
    lembretes_ordenados = sorted(lembretes, key=lambda x: datetime.strptime(x['data'], '%Y-%m-%d'))
    return render_template('meus_lembretes.html', lembretes=lembretes_ordenados)

@app.route('/editar-lembrete/<int:index>', methods=['GET', 'POST'])
def editar_lembrete(index):
    if request.method == 'POST':
        nome = request.form.get('nome')
        data = request.form.get('data')

        if nome and data:
            try:
                data_formatada = datetime.strptime(data, '%Y-%m-%d')
                if data_formatada > datetime.now():
                    lembretes[index] = {'nome': nome, 'data': data}
            except ValueError:
                pass

        return redirect('/meus-lembretes')
    else:
        lembrete = lembretes[index]
        return render_template('editar_lembrete.html', lembrete=lembrete, index=index)

@app.route('/deletar-lembrete/<int:index>')
def deletar_lembrete(index):
    del lembretes[index]
    return redirect('/meus-lembretes')

if __name__ == '__main__':
    app.run(debug=True)
