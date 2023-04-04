from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# import json
# from flask_mail import Mail

# with open("flask_project/templates/config.json",'r') as c:
#     params=json.load(c)["params"]

# local_server=True
app=Flask(__name__)
# app.config.update(
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT='465',
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME=params["user_mail"],
#     MAIL_PASSWORD=params["user_pass"]
# )

# if local_server:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


# # mail=Mail(app)
# db = SQLAlchemy(app)
# class Contact(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(20), nullable=False)
#     msg = db.Column(db.String(120), nullable=False)

@app.route("/")
def home():
    return render_template('index.html' )
@app.route("/gallery")
def gallery():
    return render_template('gallery.html')
@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    # if (request.method=='POST'):
    #     '''Add entry to the database'''
    #     name = request.form.get('name')
    #     email = request.form.get('email')
    #     message = request.form.get('message')
    #     entry = Contact(name=name, msg = message,email = email )
    #     db.session.add(entry)
    #     db.session.commit()
    #     mail.send_message(
    #         'Message from School Website by ' + name,
    #         sender=email,
    #         recipients=params['user_mail'].split(),
    #         body= message + '\n' + email
    #     )
    return render_template('contact.html')
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
