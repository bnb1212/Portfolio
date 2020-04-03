package pack1;

import javax.swing.JFrame;
import javax.swing.JMenu;

public class SwingTest2 {
	
	
	
	public static void main(String[] args) {
		JFrame frame = new JFrame("대화상자 연습");
		
		Swing2Part part = new Swing2Part();
		// ...
		frame.getContentPane().add(part, "Center");
//		frame.getContentPane().add(part, "South");
		
		frame.setJMenuBar(part.mBar);
		frame.setBounds(300, 300 ,400, 300);
		frame.setVisible(true);
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
	}
	
}
