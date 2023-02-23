public class Television  extends Objet
{
    public Television()
    {
        level=0;
        Name="Machine Laver";
        priceToUpgrade=10;
        electricityUse=10;
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
