from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

app = Flask(__name__) #to jest coś w rodzaju unitu/modułu

#####################################################################################
# Tu definiujemy obiekt bazy danych i elementy podłączenia do niego, oraz wymagane parametry
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#####################################################################################
# Tu definiujemy klasę odpowiedzialną za wymianę informacji z bazą danych
#####################################################################################
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name
    
#####################################################################################
# Tu definiujemy klasę do pobierania danych z formy
#####################################################################################
class UserForm(FlaskForm):
    name = StringField('Imię i nazwisko', validators=[InputRequired()])
    email = StringField('Adres e-mail', validators=[InputRequired()])
    
#####################################################################################
# Definicja komunikatu błędu
#####################################################################################
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Błąd w %s rekordzie - %s" % (getattr(form, field).label.text, error))
#####################################################################################    

#####################################################################################
# Tu jest obsługa wszystkich wywołań strony i podstron jako funkcje obsługujące dane wywołanie

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/oprojekcie.html')
def oprojekcie():
    return render_template('oprojekcie.html')

@app.route('/listauzytkownikow.html')
def listauzytkownikow():
    users = db.session.query(User).all()
    return render_template('listauzytkownikow.html', users=users)

@app.route('/dodajuzytkownika.html', methods=['POST', 'GET'])
def dodajuzytkownika():
    user_form = UserForm()

    if request.method == 'POST':
        if user_form.validate_on_submit():
            # Pobieranie danych z formy na stronie dodajuzytkownika.html
            name = user_form.name.data
            email = user_form.email.data

            # Zapisanie danych do bazy
            user = User(name, email)
            db.session.add(user)
            db.session.commit()

            flash('Użytkownik poprawnie dodany!')
            return redirect(url_for('listauzytkownikow'))

    flash_errors(user_form)
    return render_template('dodajuzytkownika.html', form=user_form)

#####################################################################################
# Tu uruchamiamy samą aplikację na określonych parametrach - np. na jakimś porcie
if __name__ == '__main__':
    app.run(port=5002)

