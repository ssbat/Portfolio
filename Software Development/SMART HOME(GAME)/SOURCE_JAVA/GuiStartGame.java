import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*; 

public class GuiStartGame 
{
    // private JFrame frame;
    public static void createAndShowGUI()
    {
      //Définition de l'interface graphique de la landing page
        JFrame frame=new JFrame();
        frame.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);

        ImagePanel2 panel = new ImagePanel2("images/landing.png");

        panel.setBounds(150,50,800,700);
        
        JButton start=new JButton("Lancer la partie");
        start.setBounds(200,550,150,30);
        start.addActionListener(new ActionListener()
        {
            public void actionPerformed(ActionEvent e)
            {
                frame.dispose();
                //On crée un autre thread pour lancer la deuxième interface ( le Jeu )
                new Thread(()->MainPlay.Gameinit()).start();
            }
        });
        panel.add(start);
        frame.add(panel);

        frame.setSize(800,700);
        frame.setLayout(null);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }    
    
}
class ImagePanel2 extends JPanel {

    private Image img;
  
    public ImagePanel2(String img) {
      this(new ImageIcon(img).getImage());
    }
  
    public ImagePanel2(Image img) {
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