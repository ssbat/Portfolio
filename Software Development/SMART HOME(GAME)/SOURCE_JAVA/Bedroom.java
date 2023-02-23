public class Bedroom extends Room
{
    protected Objet lit;
    protected GUI gui;

    Bedroom(GUI gui)
    {
        nameOfRoom="Chambre";
        this.gui=gui;
    }

    @Override
    public void switchLight(Boolean onoff) 
    {
        // Définition de l'affichage en fonction de l'etat de la chambre
        super.switchLight(onoff);
        if (onoff==true) 
        {   
            gui.BedroomPanel.setImage("images/Bedroom.jpg");
        }
        else
        {
            gui.BedroomPanel.setImage("images/BedroomNoLight.jpg");   
        }
    }
}