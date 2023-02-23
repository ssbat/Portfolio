public class LivingRoom extends Room
{
    public Objet TV;
    public Objet baignoire;
    public GUI gui;
    
    LivingRoom(GUI gui)
    {
        nameOfRoom="Salle de séjour";
        TV=new Television();
        this.gui=gui;
    }
    @Override
    public void switchLight(Boolean onoff) 
    {
        super.switchLight(onoff);
        // super.switchLight(onoff);
        if (onoff==true) 
        {   
            gui.LivingPanel.setImage("images/LivingRoom.jpg");
        }
        else
        {
            gui.LivingPanel.setImage("images/LivingNoLight.jpg");   
        }
    }


}