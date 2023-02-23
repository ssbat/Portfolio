import java.util.Random;
public class Habitant
{
    protected String Name;
    protected int famine;
    protected int sante;
    protected Room location;
    protected int level;
    protected Boolean isAlive;
    protected int electricity;
    protected GUI gui;



    Habitant(String Name,int famine,Room location,int level)
    {
        this.Name=Name;
        this.famine=famine;
        this.level=level;
        this.location=location;
        this.electricity=100;
        this.isAlive=true;
    }


    public void setGUI(GUI gui)
    {this.gui=gui;}
    
    public void allumerTelevision(Maison maison)
    {
        if (electricity<=maison.living.TV.electricityUse){;MainPlay.Gameover();}
        else
        {
            this.electricity=this.electricity-maison.living.TV.electricityUse;
            maison.update();

            for (int i=0;i<3;i++)
            {
                try{Thread.sleep(1000);}catch(Exception e){System.out.println(e);}
            }

        }
    };
    public void faireLaLessive(Maison maison)
    {
        if (electricity<=maison.bath.laverie.electricityUse){MainPlay.Gameover();}
        else
        {
            this.electricity=this.electricity-maison.bath.laverie.electricityUse;
            maison.update();
            for (int i=0;i<3;i++)
            {
                try{java.lang.Thread.sleep(1000);}catch(Exception e){System.out.println(e);}
            }
        }
    };

    public void seNourrir(Maison maison)
    {
        //Evites les valeurs négatives de la stat famine
        if (this.famine<10) 
            this.famine=0;
        else{this.famine-=10;}

        maison.update();
                
        try 
        {
            java.lang.Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    public void faireUneSieste()
    {
        
        Random rand = new Random();
        int reponse2=rand.nextInt(6);

        for (int cptH=reponse2;cptH!=0;cptH--)//Paramétrage du sommeil chez l'habitant
        {
            try 
            {
                java.lang.Thread.sleep(2000);

            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            this.famine++;
            if(this.famine>100){MainPlay.Gameover();}

        }
    };

    //Gestion du déplacement de l'habitant dans la maison
    public void doDeplacement(Maison maison,int reponse)
    {
            if (reponse==0) // Chambre à coucher
            {
                try 
                {
                    java.lang.Thread.sleep(2000);

                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                
                this.location=maison.bed;
                gui.setlocation("Bedroom");
                gui.buttonBed.setEnabled(false);
            }
            else if(reponse==1) //Cuisine
            {   
                try 
                {
                    java.lang.Thread.sleep(2000);

                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                this.location=maison.kit;
                gui.setlocation("Kitchen");
                gui.buttonKit.setEnabled(false);

            }
            else if(reponse==2)//Salle de bain
            {
                try 
                {
                    java.lang.Thread.sleep(2000);

                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                this.location=maison.bath;
                gui.setlocation("Bathroom");
                gui.buttonBath.setEnabled(false);


            }
            else if(reponse==3)//Salle de séjour
            {
                try 
                {
                    java.lang.Thread.sleep(2000);

                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                this.location=maison.living;
                gui.setlocation("LivingRoom");
                gui.buttonLiv.setEnabled(false);
            }
    }
}