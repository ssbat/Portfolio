
from ast import Num
from re import L
from flask import Flask, redirect, render_template,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_required, login_user,current_user, logout_user
from flask_login import UserMixin
from requests import session
from sqlalchemy.sql import func
import numpy as np
import matplotlib.pyplot as plt

#chaque application sur flask est initialisé comme ca
app=Flask(__name__)
app.config['SECRET_KEY'] = "MyUsjProject"
data=SQLAlchemy(app)
database='database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database}'
data.init_app(app)
def create_database(app):#la7ata ma aemel databasejdide kel mara
    if not path.exists("usjbook+/" + database):
        data.create_all(app=app)

#hon kheles 


#la data base
class Etudiant(data.Model,UserMixin):
    
    id=data.Column(data.Integer,primary_key=True)
    matricule=data.Column(data.String(150),unique=True)
    nom=data.Column(data.String(150),unique=True)
    password=data.Column(data.String(150))
    date=data.Column(data.DateTime(timezone=True),default=func.now())
    position=data.Column(data.String())
    specialite=data.Column(data.String())
    questions=data.relationship('Question',backref='etudiant',passive_deletes=True)
    reponses=data.relationship('Reponse',backref='etudiant',passive_deletes=True)


class Question(data.Model):
    id=data.Column(data.Integer,primary_key=True)
    text=data.Column(data.Text,nullable=False)
    date=data.Column(data.DateTime(timezone=True),default=func.now())
    personnage=data.Column(data.Integer,data.ForeignKey('etudiant.id',ondelete='CASCADE'),nullable=False)
    reponses=data.relationship('Reponse',backref='question',passive_deletes=True)

class Reponse(data.Model):
    id=data.Column(data.Integer,primary_key=True)
    text=data.Column(data.Text,nullable=False)
    date=data.Column(data.DateTime(timezone=True),default=func.now())
    personnage=data.Column(data.Integer,data.ForeignKey('etudiant.id',ondelete='CASCADE'),nullable=False)
    question_id=data.Column(data.Integer,data.ForeignKey('question.id',ondelete='CASCADE'),nullable=False)

    



    #posts=data.relationship('Post',backref='etudiant',passive_deletes=True)
    #comments=data.relationship('Comment',backref='etudiant',passive_deletes=True)
    #likes=data.relationship('Like',backref='etudiant',passive_deletes=True)
##
create_database(app)
login_manager = LoginManager()
login_manager.login_view = "loginpage"
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):#ta tehfaz bel sessin enni signed in
        return Etudiant.query.get(int(id))

@app.route('/loginpage',methods=['GET','POST'])
def loginpage():
    if request.method=="POST":
      
        matricule=request.form.get("matricule")
        print(matricule)

        password=request.form.get("password")
        etudiant=Etudiant.query.filter_by(matricule=matricule).first()
        if etudiant:
            if etudiant.password==password:
                flash('lOGIN SUCCESFULLY!')
                login_user(etudiant,remember=True)
                return redirect(url_for('main'))
            else:
                flash("le pass est faux")
        else:
            flash("matricule n'existe pas")
    print(current_user,'433333333333')
    return render_template('authentification.html',etudiant=current_user)

@app.route('/')
@app.route('/main',methods=['POST','GET'])
@login_required
def main():
    ##
    import requests
    response = requests.get("https://newsapi.org/v2/top-headlines?country=fr&apiKey=438be8ecf7c04e8d97beb745139228c4")
    data=response.json()
    import json
    text = json.dumps(data, indent=4)
    print(type(text))
    text=json.loads(text)
    #print(text)
    listenews=[]
    for i in range(9):
        listenews.append([text['articles'][i]['title'],text['articles'][i]['source'],text['articles'][i]['url'],text['articles'][i]['publishedAt']])
    print(listenews)
        
    etudiants=Etudiant.query.all()
    questions=Question.query.all()
    
    return render_template('main.html',etudiant=current_user,etudiants=etudiants,questions=questions,listenews=listenews)





@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method=="POST":
            print(Etudiant)
            matricule=request.form.get('matricule')
            print(matricule,'ffewwwwwwwwwwwwwwwwwwwww')
            nom=request.form.get("nom")
            password=request.form.get("password")
            password2=request.form.get("password2")
            position=request.form.get("position")
            specialite=request.form.get("specialite")

            matricule_exist=Etudiant.query.filter_by(matricule=matricule).first()
            nom_exist=Etudiant.query.filter_by(nom=nom).first()
            test=matricule.isdigit()
            if not test:
                flash("le matricule doit étre un nombre")

            elif matricule_exist:
                flash("Ce matricule déja existe")
            elif nom_exist:
                flash("ce nom deja existe")
            elif password!=password2:
                flash("les 2 passwords sont différents")
                
            else:
                etudiant2=Etudiant(matricule=matricule,nom=nom,password=password,position=position,specialite=specialite)
                data.session.add(etudiant2)
                data.session.commit()
                login_user(etudiant2,remember=True)
                flash("Crée!")
                    
                return redirect(url_for("main"))
    
    return render_template("sign-up.html",etudiant=current_user)



@app.route('/logout')
@login_required
def logout():
    flash("LOGGED OUT!")
    logout_user()
    return redirect(url_for('main'))

@app.route('/creationdupost',methods=['GET','POST'])
@login_required
def createpost():
    if request.method=='POST':
        question=request.form.get("post")
        post=Question(text=question,personnage=current_user.id)
        data.session.add(post)
        data.session.commit()
        print(question)
        flash("POST CREE")
        return redirect(url_for('main'))
    return render_template('creationpost.html',etudiant=current_user)

@app.route('/reponse/<questionid>',methods=['POST','GET'])
@login_required
def creationreponse(questionid):
    if request.method =='POST':
        reponsetext=request.form.get('reponse')
        post=Question.query.filter_by(id=questionid).first()
        if post:
            reponse=Reponse(text=reponsetext,question_id=questionid,personnage=current_user.id)
            data.session.add(reponse)
            data.session.commit()
    return redirect(url_for('main'))


@app.route('/deletpost/<questionid>')
@login_required
def deletereponse(questionid):
    question=Question.query.filter_by(id=questionid).first()
    if question:
        reponses=Reponse.query.filter_by(question_id=questionid).all()
        for reponse in reponses:
            data.session.delete(reponse)
        data.session.delete(question)
        data.session.commit()    
    return redirect(url_for('main'))

@app.route('/etudiant/<etudiantid>')
@login_required
def etudiantpages(etudiantid):
    etudiant2=Etudiant.query.filter_by(id=etudiantid).first()
    questions=Question.query.filter_by(personnage=etudiantid).all()

    return render_template('etudiantpage.html',questions=questions,etudiant=current_user,etudiant2=etudiant2)
  

if __name__=="__main__": 
    app.run(debug=True)#every change byaemel run lal flask server

