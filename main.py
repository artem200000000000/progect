#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)

def result_calculate(volume):
    #Переменные для энергозатратности приборов
    MNOGITEL = 0.432
    return  volume * MNOGITEL 

#Форма карты
#@app.route('/form_create', methods=['GET','POST'])
#def form_create():
#    if request.method == 'POST':
#        title =  request.form['title']
#        subtitle =  request.form['subtitle']
#        text =  request.form['text']

        #Создание объкта для передачи в дб

#        card = Card(title=title, subtitle=subtitle, text=text)
#
#        db.session.add(card)
#        db.session.commit()
#        return redirect('/')
#    else:
#        return render_template('create_cart.html')

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def info_raschet_perexod():
    return render_template('raschet.html',
#                            volume=volume
                           )

#@app.route('/3')
#def index():
#    return render_template('end.html')
#                            result=result_calculate(int(volume),
#                                                    int(fertility), 
#                                                    int(weight)
#                                                    )


    
# @app.route('/<size>')
# def lights(size):
#     return render_template(
#                             'info rogozl' 
                            
#                            )
# @app.route('/<size>/<lights>')
# def electronics(size, lights):
#     return render_template(
#                             'info kamish.html'                                                     
#                            )

# #Расчет
# @app.route('/<size>/<lights>/<device>')
# def end(size, lights, device):
#     return render_template('end.html', 
#                             result=result_calculate(int(size),
#                                                     int(lights), 
#                                                     int(device)
#                                                     )
#                         )
# #Форма
# @app.route('/form')
# def form():
#     return render_template('form.html')

# #Результаты формы
# @app.route('/submit', methods=['GET','POST'])
# def submit_form():
#     name = request.form['name']
#     email = request.form['email']
#     address = request.form['address']
#     date = request.form['date']
# 		# здесь вы можете сохранить данные или отправить их по электронной почте
#     return render_template('form_result.html', name=name, email=email, date = date, address = address)

app.run(debug=True)