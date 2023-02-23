class SchedulerThread extends Thread
{
    Habitant habitant;
    Maison maison;
    // Gestion du temps restant pour payer la facture;
    SchedulerThread(Habitant habitant,Maison maison)
    {
        this.habitant=habitant;
        this.maison=maison;
    }
    //Gestion de l'avancement des paramètres du jeu
    public void run()
    {
        int i=0;
        int NextLevel=7;
        //Gestion de l'évolution des paramètres en fonction des actions du joueur
        while(habitant.isAlive)
        {
            try
            {
                sleep(2000);

            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            i++;
            maison.player.Facturefrequence--;
            habitant.famine++;
            //La facture d'electricité sera proportionnelle à chaque instant au nombre d'ampoule allumés
            habitant.electricity=habitant.electricity-1-(Room.nbOfturnedOnLights)*3;
            if (i==NextLevel)
            {
                //Evolution du niveau de difficulté du jeu
                maison.player.Level+=1;
                i=0;
                NextLevel+=2;
                maison.player.money+=50;
                if(maison.habitant.electricity+60>100){maison.habitant.electricity=100;}
                else maison.habitant.electricity+=60;
            }

            //Gestion des cas possibles pour un GameOver
            if (habitant.famine>100){habitant.isAlive=false;MainPlay.Gameover();}
            if (habitant.electricity<0){habitant.isAlive=false;MainPlay.Gameover();}
            if(maison.player.Facturefrequence==0){habitant.isAlive=false;MainPlay.Gameover();}
            maison.update();
        }
    }
}
