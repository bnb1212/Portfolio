package sample;

import java.awt.Frame;

public class MyFrame1 {
	
	private Frame fr;
	
	public MyFrame1() { // 클래스의 포함 연습
		// TODO Auto-generated constructor stub
		fr = new Frame("포함 연습용");
	
		displayWindow();
	}
	
	public void displayWindow() {
		fr.setSize(500, 300);
		fr.setLocation(200, 150);
		fr.setVisible(true);
	}
	
	public static void main(String[] args) {
//		Myframe1 frame1 = new Myframe1();
//		frame1.displayWindow();
		
		new MyFrame1();
	}
}
