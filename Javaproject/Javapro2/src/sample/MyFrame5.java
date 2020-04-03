package sample;

import java.awt.Font;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class MyFrame5 extends Frame {
	MyClass myClass;
	int x, y;// 마우스로 폼 바닥을 찍었을 때의 해당 지점 좌표
	String str[] = { "김치국", "공기밥", "김밥", "주먹밥", "집밥" };

	public MyFrame5() {
		// super("내부 클래스 사용");
		setTitle("내부 클래스 사용");

		setSize(400, 300);
		setLocation(200, 200);
		setVisible(true);

		myClass = new MyClass();
		addWindowListener(myClass);
		addMouseListener(new OurClass());


	}

	class OurClass extends MouseAdapter {
		@Override
		public void mouseClicked(MouseEvent e) {
//			int m = e.getX();
//			int n = e.getY();
			x = e.getX();
			y = e.getY();
//			System.out.println("m : " + m + " n : " + n);
//			setTitle("m : " + m + " n : " + n);
			paint(getGraphics()); // refresh X
			repaint(); // refresh
		}
		
	}
	
	@Override
	public void paint(Graphics g) {
		int ar = (int)(Math.random() * 5);
		g.setFont(new Font("굴림", Font.BOLD, ar*50 +8));
		
		g.drawString(str[ar], x, y);
	}
	
	class MyClass extends WindowAdapter {
		public void windowClosing(WindowEvent e) {// 내부 클래스
			System.exit(0);
		}
	}
	
	public static void main(String[] args) {
		new MyFrame5();
	}
}
