public abstract class Room 
{
    //Squelette classique de la pièce dont hérite les autres classes ( Cuisine, chambre,...)
    public boolean lightState=false;
    public String  nameOfRoom;
    public static int nbOfturnedOnLights=0;

    public void switchLight(Boolean onoff)
    {
        if (onoff==true)
        {
            this.lightState=true;
            nbOfturnedOnLights++;
        }
        else
        {
            this.lightState=false;
            nbOfturnedOnLights--;
        }
    }
}
