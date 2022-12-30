from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib
# Create your views here.


def commerce(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))
   

def predire(request):
    if request.method=='POST':
        
        nbre_bijoux=int(request.POST['nbre_bijoux'])
        nbre_soulier=int(request.POST['nbre_soulier'])
        nbre_pantalon=int(request.POST['nbre_pantalon'])
        nbre_montre=int(request.POST['nbre_montre'])
        nbre_chapeau=int(request.POST['nbre_chapeau'])
        nbre_chemise=int(request.POST['nbre_chemise'])
        nbre_lacoste=int(request.POST['nbre_lacoste'])
        nbre_robe=int(request.POST['nbre_robe'])
        nbre_chainette=int(request.POST['nbre_chainette'])
        
        #chargement du tableau de 2dimensions 
        tableau=[[nbre_bijoux,nbre_soulier,nbre_pantalon,nbre_montre,nbre_chapeau,nbre_chemise,nbre_lacoste,nbre_robe,nbre_chainette]]
        
        
        #chargement du modele
        regression=joblib.load('ml/model1.pkl')
        resultat=regression.predict(tableau)
        print(tableau)
        print(resultat)
        
        
       
        
        return HttpResponse(regression.predict(tableau))
        
     
       
   
    