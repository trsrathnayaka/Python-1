from flask import Flask

app= Flask(_name_)

@app.route('/')
@app.route('/home')

def home():

return "welcome home python lovers!"

if _name_ == '_main_':
        app.run('localhost',5050)
