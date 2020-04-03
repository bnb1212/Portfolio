package sample;

import java.awt.Color;
import java.awt.Event;
import java.awt.Frame;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class MyFrame3 extends Frame implements WindowListener, MouseListener {

	int aa = 0;

	// ===== CONSTRUCTOR ======================
	public MyFrame3() {
		super("인터페이쓰 사용");
		setSize(300, 200);
		setLocation(200, 200);
		setVisible(true);

		addWindowListener(this);
		addMouseListener(this);
	}
	// ===== METHOD ===========================

	@Override
	public void mouseClicked(MouseEvent e) {
//		aa++;
//		System.out.println("aa : " + aa);
//		setBackground(new Color(85, 94,227));
		System.out.println((int)(Math.random()*255));
		int r = (int)(Math.random()*255);
		int g = (int)(Math.random()*255);
		int b = (int)(Math.random()*255);
		setBackground(new Color(r, g, b));
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public boolean mouseExit(Event evt, int x, int y) {
		// TODO Auto-generated method stub
		return super.mouseExit(evt, x, y);
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void windowActivated(WindowEvent e) {
	}

	@Override
	public void windowDeactivated(WindowEvent e) {
	}

	@Override
	public void windowIconified(WindowEvent e) {
		System.out.println("자바만세~!");
	}

	@Override
	public void windowDeiconified(WindowEvent e) {
		System.out.println("오늘 불금 만쉐~");
	}

	@Override
	public void windowOpened(WindowEvent e) {
	}

	@Override
	public void windowClosing(WindowEvent e) {
//		this.setTitle("뿌슝빠슝");
		System.exit(0);
	}

	@Override
	public void windowClosed(WindowEvent e) {
	}

	public static void main(String[] args) {
		new MyFrame3();

	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

}
