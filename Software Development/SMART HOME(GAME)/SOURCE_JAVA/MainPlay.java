import java.awt.Color;
import java.util.Random;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.UIManager;
import javax.swing.plaf.nimbus.NimbusLookAndFeel;

class MainPlay {
    
    static int oldChoixDeplacement = 1; //Cette varaible sauvegarde la position précedente de l'habitant dans la maison
    static Maison maison;

    static void doDeplacement(Maison maison, Habitant habitant) 
    {
        /*  Les déplacements de l'habitant étant aléatoire, il faut donc éviter que celui ci ne se déplace d'un endroit vers 
        le même endroit*/
        Random rand = new Random();
        int choixDeplacement = rand.nextInt(4);
        while (choixDeplacement == oldChoixDeplacement) {
            choixDeplacement = rand.nextInt(4);
        }

        oldChoixDeplacement = choixDeplacement; //sauvegarde de l'action choisi aléatoirement

        /* Si l'habitant risque de mourir, alors le programme l'envoi de force à la cuisine */
        if(habitant.famine>=80){choixDeplacement=1;}
        
        habitant.doDeplacement(maison, choixDeplacement);
    }

    static void doList(Habitant habitant, Player player) {
        try {
            java.lang.Thread.sleep(1500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } // cadencement des actions

        //Choix de l'action à exécuter en fonction de la position de l'habitant dans la maison
        if (habitant.location instanceof Kitchen) {
            kitchenDoList(habitant, player);
        } else if (habitant.location instanceof Bedroom) {
            bedroomDoList(habitant);
        } else if (habitant.location instanceof Bathroom) {
            bathroomDoList(habitant);
        } else if (habitant.location instanceof LivingRoom) {
            livingDoList(habitant);
        }
    }

    static void kitchenDoList(Habitant habitant, Player player) {
        //Entrée de l'habitant dans une pièce
        if (maison.kit.lightState == false) {
            maison.kit.switchLight(true);
        }
        maison.update();

        //Action à exécuter
        if (player.money <= 10) {
            habitant.isAlive = false;
            MainPlay.Gameover();
        } else {
            player.money -= 10;
            habitant.seNourrir(maison);
            doDeplacement(maison, habitant);
            // L'habitant donne ainsi la possibilité d'éteindre la lumière une fois qu'il quitte la pièce
            maison.gui.buttonKit.setEnabled(true); 
        }
    }

    static void bedroomDoList(Habitant habitant) {
        //Entrée de l'habitant dans une pièce
        if (maison.bed.lightState == false) {
            maison.bed.switchLight(true);
        }

        maison.update();

        habitant.faireUneSieste();
        doDeplacement(maison, habitant);
        // L'habitant donne ainsi la possibilité d'éteindre la lumière une fois qu'il quitte la pièce
        maison.gui.buttonBed.setEnabled(true);
    }

    static void bathroomDoList(Habitant habitant) {
        //Entrée de l'habitant dans une pièce
        if (maison.bath.lightState == false) {
            maison.bath.switchLight(true);
        }

        maison.update();

        habitant.faireLaLessive(maison);
        doDeplacement(maison, habitant);
        // L'habitant donne ainsi la possibilité d'éteindre la lumière une fois qu'il quitte la pièce
        maison.gui.buttonBath.setEnabled(true);
    }

    static void livingDoList(Habitant habitant) {
        //Entrée de l'habitant dans une pièce
        if (maison.living.lightState == false) {
            maison.living.switchLight(true);
        }
        maison.update();
        habitant.allumerTelevision(maison);
        doDeplacement(maison, habitant);
        // L'habitant donne ainsi la possibilité d'éteindre la lumière une fois qu'il quitte la pièce
        maison.gui.buttonLiv.setEnabled(true);
    }

    static JFrame gameOver2()
    {
        JFrame gameOver = new JFrame("Smart Home GAME OVER");
        
		gameOver.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gameOver.setSize(815,715);
        gameOver.setLocationRelativeTo(null);
        gameOver.setVisible(true);

        JPanel back = new JPanel();
        back.setBackground(Color.BLACK);
        back.setSize(815,715);
        gameOver.add(back);

        return gameOver;
    }

    static void Gameover()
    {
        //Générer une interface qui va se charger de l'affichage du GameOver
        gameOver2();
        JOptionPane.showMessageDialog(null, "You must pay more attention to your stats", "too slow", JOptionPane.INFORMATION_MESSAGE);
        //Fermeture complet de tout le Jeu
        System.exit(0);
    }

    //Lancement du jeu
    static public void Gameinit() {
        //Initialisation des paramètres du jeu
        Player player = new Player(0, 200);

        GUI gui = new GUI();
        gui.createAndShowGUI();
        player.setGui(gui);

        Habitant habitant;
        maison = new Maison(player, gui);
        gui.setMaison(maison);
        habitant = new Habitant("Saad", 65, maison.kit, 0);
        habitant.setGUI(gui);
        maison.setHabitant(habitant);
        maison.update();

        //Définition des threads pour le cadençage du programme
        SchedulerThread threadSched = new SchedulerThread(habitant, maison);

        
        //Lancement des différents threads
        threadSched.start();


        while (habitant.isAlive) {
            doList(habitant, player);
        }
    }

    // //point d'entrée du programme
    public static void main(String[] args) throws Exception 
    {
        UIManager.setLookAndFeel(new NimbusLookAndFeel());
        GuiStartGame.createAndShowGUI();
    }
}
