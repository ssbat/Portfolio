public class Kitchen extends Room
{
    protected Objet four;
    protected GUI gui;
    
    Kitchen(GUI gui)
    {
        nameOfRoom="Cuisine";
        this.gui=gui;
    }

    @Override
    public void switchLight(Boolean onoff) {
        super.switchLight(onoff);
        if (onoff==true) 
        {  
            gui.KitchenPanel.setImage("images/Kitchen.jpeg");
        }
        else
        {
            gui.KitchenPanel.setImage("images/KitchenNoLight.jpg");   
        }
    }
}