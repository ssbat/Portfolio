public class Bathroom extends Room
{
    protected Objet laverie;
    protected GUI gui;


    Bathroom(GUI gui)
    {
        nameOfRoom = "Salle de bain";
        laverie = new Laverie();
        this.gui = gui;
    }

    @Override
    public void switchLight(Boolean onoff) {
        super.switchLight(onoff);

        //Définition de l'image à afficher en fonction de l'état des lumières dans la salle de bain
        if (onoff==true) 
        {   
            gui.BathPanel.setImage("images/Bathroom.jpg");
        }
        else
        {
            gui.BathPanel.setImage("images/Bathroomnolight.jpg");   
        }
    }

}