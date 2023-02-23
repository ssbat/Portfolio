public class Maison    
{

    protected Kitchen kit;
    protected Bedroom bed;
    protected Bathroom bath;
    protected LivingRoom living;
    protected GUI gui;
    protected Habitant habitant;
    Player player;

    //Initialisation de la maison
    public Maison(Player player,GUI gui)
    {
        kit=new Kitchen(gui);
        bed=new Bedroom(gui);
        bath=new Bathroom(gui);
        living=new LivingRoom(gui);
        this.gui=gui;
        this.player=player;
    }

    //Initialisation de l'habitant
    public void setHabitant(Habitant habitant)
    {
        this.habitant=habitant;
    }

    //Mise à jour de tous les paramètres de la maison
    public void update()
    {
        gui.setTextlectriclabel(habitant.electricity);
        gui.setTextFaminelabel(habitant.famine);
        gui.setTextMoneyLabel(player.money);
        gui.setTextLampesOn(Room.nbOfturnedOnLights);
        gui.setTextLevel(player.Level);
        gui.setTVLevel(living.TV.level);
        gui.setLaverieLevel(bath.laverie.level);
        gui.setTempsFacture(player.Facturefrequence);
    }



}
