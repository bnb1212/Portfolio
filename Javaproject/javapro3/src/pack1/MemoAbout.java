package pack1;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class MemoAbout extends JDialog implements ActionListener{
	public MemoAbout(JFrame frame) {
		
		/*super(frame);
		setTitle("메모장 정보");
//		setModal(true);
		setModal(false); // true : Modal, flase : Modaless
		*/
		super(frame,"메모장 정보", true);// 세번쨰 인자는 modal인자
		
		JLabel label = new JLabel("미니 메모장 ver 0.9");
		JButton btn = new JButton("확인");
		btn.addActionListener(this);
		add("Center", label);
		add("South", btn);
		
		setBackground(Color.LIGHT_GRAY);
		setBounds(350,350,200,200);
		setVisible(true);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		dispose();
	}
	
}
