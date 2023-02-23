import java.awt.*;
import java.awt.event.*;
import javax.swing.*; 

public class GUI 
{
    //Définition des différents éléments graphiques

    // Les différents labels pour le rendu visuel
    protected JLabel Electric;
    protected JLabel Famine;
    protected JLabel Money;
    protected JLabel NbOfLampeturnedOn;
    protected Maison maison;
    protected JLabel Level;

    protected JLabel locationBed;
    protected JLabel locationBath;
    protected JLabel locationKit;
    protected JLabel locationLiving;
    protected JLabel LaverieLevel;
    protected JLabel TVLevel;
    protected JLabel FactureTemps;

    // Les images de fond des différentes pièces
    protected ImagePanel BathPanel;
    protected ImagePanel LivingPanel;
    protected ImagePanel KitchenPanel;
    protected ImagePanel BedroomPanel;

    // Les buttons d'interfaces
    protected JButton buttonBath;
    protected JButton buttonLiv;
    protected JButton buttonKit;
    protected JButton buttonBed;

    //Gestion du déplacement de l'habitant dans les pièces de la maison
    public void setlocation(String roomName)
    {
        //Départ d'une pièce
        locationBath.setIcon(null);
        locationBed.setIcon(null);
        locationKit.setIcon(null);
        locationLiving.setIcon(null);

        //Arrivée dans une autre des pièces
        if (roomName=="Bathroom")
        {
            ImageIcon imgThisImg = new ImageIcon("images/stickLiving.png");
            locationBath.setIcon(imgThisImg);
        }
        if (roomName=="Bedroom")
        {
            ImageIcon imgThisImg = new ImageIcon("images/stickSleeping.png");
            locationBed.setIcon(imgThisImg);
        }
        if (roomName=="Kitchen")
        {
            ImageIcon imgThisImg = new ImageIcon("images/eating6.png");
            locationKit.setIcon(imgThisImg);
        }
        if (roomName=="LivingRoom")
        {
            ImageIcon imgThisImg = new ImageIcon("images/stickLiving.png");
            locationLiving.setIcon(imgThisImg);
        }
    }

    //Mise à jour des statistiques du jeu
    public void setTextlectriclabel(int electricityBill)
    {
        Electric.setText("Electricity : "+Integer.toString(electricityBill) + "%");
    }

    public void setTextFaminelabel(int famine)
    {
        Famine.setText("Niveau de Famine : "+Integer.toString(famine) + "%");
    }

    public void setTextMoneyLabel(int money)
    {
        Money.setText("Argent : "+Integer.toString(money) + " Euros");
    }

    public void setTextLevel(int level)
    {
        Level.setText("Niveau : "+Integer.toString(level));
    }
    public void setLaverieLevel(int level)
    {
        LaverieLevel.setText("Niveau laverie : "+Integer.toString(level));
    }
    public void setTVLevel(int level)
    {
        TVLevel.setText("Niveau TV : " + Integer.toString(level));
    }
    public void setTextLampesOn(int number)
    {
        NbOfLampeturnedOn.setText("Lampes allumees : "+Integer.toString(number));
    }
    public void setTempsFacture(int temps)
    {
        FactureTemps.setText("echeance Facture : " +Integer.toString(temps));
    }
    public void setMaison(Maison maison){this.maison=maison;}


    //Mise à disposition de la fenêtre graphique
    protected  void createAndShowGUI()
    {
        JFrame frame = new JFrame("SmartHome");
        frame.repaint();
        JPanel InfoPanel=new JPanel();
        InfoPanel.setBounds(0, 0,1000,100);        
        InfoPanel.setBackground(new java.awt.Color(25,25, 25));    
        
        //Configuration de l'interface Salle de séjour
        ImagePanel LivingPanel=new  ImagePanel(new ImageIcon("images/LivingNoLight.jpg").getImage());
        this.LivingPanel=LivingPanel;
        LivingPanel.setBounds(0,100,400,300);
        LivingPanel.setBackground(new java.awt.Color(50,50,50));
        JButton buttonLiv=new JButton("Off");

        this.buttonLiv=buttonLiv;
        buttonLiv.setBounds(340,0,60,30);
        buttonLiv.setBackground(Color.ORANGE);
        buttonLiv.setForeground(Color.WHITE);
        buttonLiv.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                if(maison.living.lightState==true)
                { 
                    maison.living.switchLight(false);
                    maison.update();
                }
            }
        });
        JLabel Livingname=new JLabel("Living room");
        Livingname.setForeground(new java.awt.Color(255,255,255));
        Livingname.setFont(new Font("Franklin Gothic Demi Cond", Font.BOLD, 14));
        Livingname.setBounds(10, 0, 100, 20);
        
        //Configuration de l'interface de la cuisine
        ImagePanel KitchenPanel=new  ImagePanel(
            new ImageIcon("images/Kitchen.jpeg").getImage());
        this.KitchenPanel=KitchenPanel;
        KitchenPanel.setBounds(400,100,400,300);
        JButton buttonKit=new JButton("Off");
        this.buttonKit=buttonKit;
        buttonKit.setEnabled(false);
        buttonKit.setBounds(340,0,60,30);
        buttonKit.setBackground(Color.ORANGE);
        buttonKit.setForeground(Color.WHITE);
        buttonKit.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                if(maison.kit.lightState==true)
                { 
                    maison.kit.switchLight(false);
                    maison.update();
                }
            }
        });
        JLabel Kitchenname=new JLabel("Dinning room");
        Kitchenname.setForeground(new java.awt.Color(0,0,0));
        Kitchenname.setFont(new Font("Franklin Gothic Demi Cond", Font.BOLD, 14));
        Kitchenname.setBounds(10, 0, 100, 20);

        //Configuration de la salle de bain
        ImagePanel BathPanel=new  ImagePanel(
            new ImageIcon("images/Bathroomnolight.jpg").getImage());  
        this.BathPanel=BathPanel;
        BathPanel.setBounds(0,400,400,300);
        JButton buttonBath=new JButton("Off");
        this.buttonBath=buttonBath;
        buttonBath.setBackground(Color.ORANGE);
        buttonBath.setForeground(Color.WHITE);
        buttonBath.setBounds(340,0,60,30);
        buttonBath.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                if(maison.bath.lightState==true)
                {
                    maison.bath.switchLight(false);
                    maison.update();
                }
            }
        });
        JLabel Bathroomname=new JLabel("Bathroom");
        Bathroomname.setForeground(new java.awt.Color(0,0,0));
        Bathroomname.setFont(new Font("Franklin Gothic Demi Cond", Font.BOLD, 14));
        Bathroomname.setBounds(10, 0, 100, 20);
        Bathroomname.setBackground(new java.awt.Color(0,222,0));

        //Configuration de la chambre à coucher
        ImagePanel BedroomPanel=new  ImagePanel(
            new ImageIcon("images/BedroomNoLight.jpg").getImage());  
        this.BedroomPanel=BedroomPanel;
        BedroomPanel.setBounds(400,400,400,300);
        BedroomPanel.setBackground(new java.awt.Color(46,120,80));
        JButton buttonBed=new JButton("Off");
        this.buttonBed=buttonBed;
        buttonBed.setBackground(Color.ORANGE);
        buttonBed.setForeground(Color.WHITE);
        buttonBed.setBounds(340,0,60,30);
        buttonBed.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                if(maison.bed.lightState==true)
                { 
                    maison.bed.switchLight(false);
                    maison.update();
                }
            }
        });
        JLabel Bedroomname=new JLabel("Bedroom");
        Bedroomname.setFont(new Font("Franklin Gothic Demi Cond", Font.BOLD, 14));
        Bedroomname.setForeground(new java.awt.Color(255,255,255));
        Bedroomname.setBounds(10, 0, 200, 20);


        // Affichage des statistiques du jeu
        JLabel electricLabel=new JLabel();
        electricLabel.setBounds(20,0,200,20);
        electricLabel.setForeground(new java.awt.Color(255,255,255));
        this.Electric=electricLabel;

        JLabel Famine=new JLabel();
        Famine.setBounds(20,25,200,20);
        Famine.setForeground(new java.awt.Color(255,255,255));
        this.Famine=Famine;
        
        JLabel Money=new JLabel();
        Money.setBounds(20,50,200,20);
        Money.setForeground(new java.awt.Color(255,255,255));
        this.Money=Money;

        JLabel NbOfLampeturnedOn=new JLabel();
        NbOfLampeturnedOn.setBounds(20,75,200,20);
        NbOfLampeturnedOn.setForeground(new java.awt.Color(255,255,255));
        this.NbOfLampeturnedOn=NbOfLampeturnedOn;

        JLabel Level=new JLabel();
        Level.setBounds(220,0,200,20);
        Level.setForeground(new java.awt.Color(255,255,255));
        this.Level=Level;

        JLabel LaverieLevel=new JLabel();
        LaverieLevel.setBounds(220,25 ,200,20);
        LaverieLevel.setForeground(new java.awt.Color(255,255,255));
        this.LaverieLevel=LaverieLevel;

        JLabel TVLevel=new JLabel();
        TVLevel.setBounds(220,50 ,200,20);
        TVLevel.setForeground(new java.awt.Color(255,255,255));
        this.TVLevel=TVLevel;

        JLabel FactureTemps=new JLabel();
        FactureTemps.setBounds(220,75 ,200,20);
        FactureTemps.setForeground(new java.awt.Color(255,255,255));
        this.FactureTemps=FactureTemps;
        
        //Configuration des buttons d'actions
        JButton buttonFacture=new JButton("Payer la Facture");
        buttonFacture.setBounds(640,0,150,30);
        buttonFacture.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                maison.player.payerFacture();
            }
        });
        JButton UpdateLaverie=new JButton("Ugrade Laverie");
        UpdateLaverie.setBounds(640,30,150,30);
        UpdateLaverie.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                maison.player.upgrade(maison.bath.laverie);
            }
        });
        JButton UpdateTv=new JButton("Ugrade TV");
        UpdateTv.setBounds(640,60,150,30);
        UpdateTv.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                maison.player.upgrade(maison.living.TV);
            }
        });

        //label location
        JLabel locationbed=new JLabel();
        locationbed.setBounds(100, 15, 400, 300);
        this.locationBed=locationbed;
        locationbed.setForeground(new java.awt.Color(255,0,0));

        JLabel locationKit=new JLabel();
        ImageIcon imgThisImg = new ImageIcon("images/eating6.png");
        locationKit.setBounds(170, 30, 400, 300);
        locationKit.setIcon(imgThisImg);
        this.locationKit=locationKit;
        locationKit.setForeground(new java.awt.Color(255,0,0));

        JLabel locationBath=new JLabel();
        locationBath.setBounds(80, 30, 400, 300);
        this.locationBath=locationBath;
        locationBath.setForeground(new java.awt.Color(255,0,0));

        JLabel locationLiving=new JLabel();
        locationLiving.setBounds(170, 30, 400, 300);
        this.locationLiving=locationLiving;
        locationLiving.setForeground(new java.awt.Color(255,0,0));

        // Ajout des composants à la fenêtre graphique
        InfoPanel.add(electricLabel);
        InfoPanel.add(Famine);
        InfoPanel.add(Money);
        InfoPanel.add(NbOfLampeturnedOn);
        InfoPanel.add(Level);
        InfoPanel.add(LaverieLevel);
        InfoPanel.add(TVLevel);
        InfoPanel.add(FactureTemps);
        InfoPanel.add(buttonFacture);
        InfoPanel.add(UpdateLaverie);
        InfoPanel.add(UpdateTv);
        KitchenPanel.add(buttonKit);
        BedroomPanel.add(buttonBed);
        BathPanel.add(buttonBath);
        LivingPanel.add(buttonLiv);
        BedroomPanel.add(Bedroomname);
        LivingPanel.add(Livingname);
        KitchenPanel.add(Kitchenname);
        BathPanel.add(Bathroomname);
        BathPanel.add(locationBath);
        KitchenPanel.add(locationKit);
        LivingPanel.add(locationLiving);
        BedroomPanel.add(locationBed);
        InfoPanel.setLayout(null);
        BathPanel.setLayout(null);
        BedroomPanel.setLayout(null);
        LivingPanel.setLayout(null);
        KitchenPanel.setLayout(null);
        frame.add(InfoPanel);
        frame.add(LivingPanel);
        frame.add(KitchenPanel);
        frame.add(BathPanel);
        frame.add(BedroomPanel);

        //Définition des caractéristiques de la fenêtre
        frame.setSize(815,715);
        frame.setLocationRelativeTo(null);
        frame.setLayout(null);
        frame.setResizable(false);
        frame.setVisible(true);
    }
}

class ImagePanel extends JPanel {
    protected Image img;
  
    public ImagePanel(String img) {
      this(new ImageIcon(img).getImage());
    }
  
    public ImagePanel(Image img) {
      this.img = img;
      Dimension size = new Dimension(img.getWidth(null), img.getHeight(null));
      setPreferredSize(size);
      setMinimumSize(size);
      setMaximumSize(size);
      setSize(size);
      setLayout(null);
    }
  
    public void setImage(String img)
    {
        this.img=new ImageIcon(img).getImage();
        Dimension size = new Dimension(this.img.getWidth(null), this.img.getHeight(null));

        //Définition des caractéristiques de l'image
        setPreferredSize(size);
        setMinimumSize(size);
        setMaximumSize(size);
        setSize(size);

        this.repaint();
        setLayout(null);
    }

    public void paintComponent(Graphics g) {
      super.paintComponent(g);
      g.drawImage(img, 0, 0, null);
    }
}