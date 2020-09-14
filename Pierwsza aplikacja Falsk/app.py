from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# Konfiguracja połączenia do bazy danych MySQL
app.config['MYSQL_DATABASE_USER'] = '07438848_python'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = '07438848_python'
app.config['MYSQL_DATABASE_HOST'] = 'sql.fxsystems.com.pl'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showHome')
def showHome():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        # Uruchomiliśmy właściwe działanie - przechodzimy do obsługi MySQL
        conn = mysql.connect()
        cursor = conn.cursor()

        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # Sprawdzanie, czy są wszystkie wymagane dane
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'Nowy użytkownik poprawnie dodany!'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Proszę wprowadzić wymagane informacje</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

if __name__ == "__main__":
    app.run(port=5002)
