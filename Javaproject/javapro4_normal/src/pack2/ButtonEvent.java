package pack2;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;

public class ButtonEvent extends JFrame{
	
	public ButtonEvent() {
		super("람다");
		setBounds(300,300,300,300);
		setVisible(true);
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		setLayout(null); // 기본 레이아웃을 없앰(null로 설정)
		JButton btn = new JButton("버튼 클릭");
		btn.setBounds(10, 50,  100,  50);
		add(btn);
		
		btn.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				setTitle("첫번째 버튼 선택");
			}
		});
		
		JButton btn2 = new JButton("버튼 눌러");
		btn2.setBounds(10, 150, 100, 50);
		add(btn2);
		
		btn2.addActionListener(e -> setTitle("두번쨰 버튼 누르기")); // 람다 사용
	}
	
	public static void main(String[] args) {
		new ButtonEvent();
	}
}
