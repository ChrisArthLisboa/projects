package easier_said;

import javax.swing.*;

public class face{

    face() {
        JFrame screen = new JFrame("Teste", null);

        JButton button = new JButton("Click", null);
        button.setBounds(100, 100, 100, 40);

        screen.add(button);

        screen.setSize(500, 500);
        screen.setLayout(null);
        screen.setVisible(true);

        button.addActionListener(null);
    }

    public static void main(String[] args) {
        face cara = new face();
    }
    

}
