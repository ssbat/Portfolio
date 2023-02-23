public  class Player 
{
    protected String Name;
    protected int Level;
    protected int money;
    protected int paiementFacture;
    protected int Facturefrequence;
    protected GUI gui;

    Player(int Level,int money)
    {
        this.Level=Level;
        this.money=money;
        this.paiementFacture=80;
        this.Facturefrequence=20;

    }
    void setGui(GUI gui)
    {
        this.gui=gui;
    }

    //Définition de la fonction de mise à jour
    void upgrade (Objet obj)
    {
        obj.upgrade();
        if(this.money-(10+obj.level*(10))<0)
        {
            MainPlay.Gameover();
        }
        else{this.money-=(10+obj.level*10);};
        gui.maison.update();
    }

    public void payerFacture()
    {
        if(this.money-paiementFacture <0){MainPlay.Gameover();}
        else
        {
            this.money-=paiementFacture;
            this.Facturefrequence=20;
            gui.setTempsFacture(this.Facturefrequence);
        }
    }
}
