package pack1;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
//import java.awt.event.WindowAdapter;
//import java.awt.event.WindowEvent;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class SwingTest extends JFrame implements ActionListener {
	JLabel lblShow;
	int count = 0;

	public SwingTest() {
		setTitle("스윙 연습");

		JPanel panel = new JPanel();
		panel.setLayout(new GridLayout(2, 1));
		panel.setBorder(BorderFactory.createEmptyBorder(30, 30, 10, 30));

		JButton btn = new JButton("클릭");
		btn.addActionListener(this);
		panel.add(btn);

		lblShow = new JLabel("버튼 클릭 수 : ");
		panel.add(lblShow);

//		add("Center", panel); 밑줄과 같음
		add(panel, BorderLayout.CENTER);

		setBounds(300, 300, 400, 400);
		setVisible(true);

		/*
		 * addWindowListener(new WindowAdapter() {
		 * 
		 * @Override public void windowClosing(WindowEvent e) { System.exit(0); } });
		 */
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		count++;
		lblShow.setText("버튼 클릭 수 : " + count);

	}

	public static void main(String[] args) {
		new SwingTest();

	}
}
