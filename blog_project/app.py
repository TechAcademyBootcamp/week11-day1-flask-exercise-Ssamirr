from blog import app

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'key'
    app.config['WTF_CSRF_SECRET_KEY'] = 'a random string'
    app.run(debug = True,port = 5000)