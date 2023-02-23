import imp
import numpy as np
import matplotlib.pyplot as plt

from application import Etudiant,Question,Reponse





def statistique():
        etudiantliste=Etudiant.query.all()
        nb_groups=len(etudiantliste)
        liste1=[]
        liste2=[]
        liste3=[]
        for etudiant in etudiantliste:
            liste1.append(len(etudiant.questions))
            liste2.append(etudiant.nom)
            s=0
            for question in etudiant.questions:
                s=s+len(question.reponses)
            liste3.append(s)
        avg_reponses=tuple(liste3)

        avg_post=tuple(liste1)
        names=tuple(liste2)
        bar_width = 0.35
        opacity = 0.8
        index = np.arange(nb_groups)
        plt.xlabel('Person')
        
        plt.title('Statistique')
        plt.bar(index, avg_post, bar_width, alpha=opacity, color='g', label='POST')
        plt.bar(index + bar_width, avg_reponses, bar_width, alpha=opacity, color='r', label='Reponses')

        plt.xticks(index+ bar_width , names)

        plt.legend()
        plt.show()
statistique()