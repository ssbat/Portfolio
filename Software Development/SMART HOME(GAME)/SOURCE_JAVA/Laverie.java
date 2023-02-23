public class Laverie extends Objet 
{
    public Laverie()
    {
        level=0;
        Name="Machine Laver";
        priceToUpgrade=10;
        electricityUse=15;
    }    

    @Override
    public void upgrade() 
    {
        if (level!=4)
        {
            level+=1;
            electricityUse=electricityUse-2;
        }        
    }
}
