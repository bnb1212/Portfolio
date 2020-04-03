package sample;

import java.awt.Frame;
public class MyFrame2 extends Frame{

	
	public MyFrame2() {
		super("상속연습");
		
		dispWindow();
	}
	
	void dispWindow() {
//		super.setSize(500, 300); 오해를 살수 있음
//		this.setSize(500, 300); setSize가 이 클래스에도 있고 부모클래스에도 있구나 오해할수 있음
		setSize(500, 300);
		setLocation(200, 150);
		setVisible(true);
		
	}
	public static void main(String[] args) {
		new MyFrame2();
		
	}
}
