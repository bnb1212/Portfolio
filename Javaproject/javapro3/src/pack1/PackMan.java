package pack1;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.JFrame;

public class PackMan extends JFrame implements KeyListener {
	Image image;
	int x, y, sel = 1;

	public PackMan() {
		super("상하좌우 화살표를 사용하세요");

		setIconImage(Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack1.jpg"));

		setLayout(null);
		setBackground(Color.white);
		setResizable(false);
		setBounds(300, 300, 400, 400);
		setVisible(true);

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		addKeyListener(this);

		x = (int) getWidth() / 2;
		y = (int) getHeight() / 2;
	}

	@Override
	public void paint(Graphics g) {
		switch (sel) {
		case 1:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack1.jpg");
			break;

		case 2:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack2.jpg");
			break;

		case 3:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack3.jpg");
			break;
		case 4:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack4.jpg");
			break;
		case 5:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack5.jpg");
			break;
		case 6:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack6.jpg");
			break;
		case 7:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack7.jpg");
			break;
		case 8:
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack8.jpg");
			break;
		}
		g.clearRect(0, 0, getWidth(), getHeight());
		g.drawImage(image, x - image.getWidth(this) / 2, y - image.getHeight(this) / 2, this);
	}

	@Override
	public void keyPressed(KeyEvent e) {
		int key = e.getKeyCode();
//		System.out.println(key);
		if (key == KeyEvent.VK_NUMPAD6 || key == KeyEvent.VK_RIGHT) {
//			System.out.println("오른쪽");
//			if (sel == 1) sel = 2; else sel = 1;
			sel = (sel == 1) ? 2 : 1;
			x = (x < getWidth()) ? x + 10 : -image.getWidth(this);
			System.out.println(x);
		}
		if (key == KeyEvent.VK_NUMPAD4 || key == KeyEvent.VK_LEFT) {
			sel = (sel == 3) ? 4 : 3;
			x = (x + image.getWidth(this) > 0) ? x - 10 : getWidth() + image.getWidth(this);
			System.out.println(x);
		}
		if (key == KeyEvent.VK_NUMPAD5 || key == KeyEvent.VK_DOWN) {
			sel = (sel == 5) ? 6 : 5;
			y = (y < getHeight()) ? y + 10 : -image.getHeight(this);
			System.out.println(y);
		}
		if (key == KeyEvent.VK_NUMPAD8 || key == KeyEvent.VK_UP) {
			sel = (sel == 7) ? 8 : 7;
			y = (y  + image.getHeight(this)  > 0) ? y - 10 : getHeight() + image.getHeight(this);
			System.out.println(y);
		}

		repaint();
	}

	public void keyReleased(KeyEvent e) {
	};

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub

	}

	public static void main(String[] args) {
		new PackMan();
	}

}
