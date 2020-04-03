package pack9;

import java.awt.Button;
import java.awt.Font;
import java.awt.Frame;
import java.awt.Label;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Calendar;

public class ThreadTestClock extends Frame implements ActionListener, Runnable {

	private Label lblMessage;
	private Boolean flag = false;
	private Thread thread;

	public ThreadTestClock() {
		lblMessage = new Label("Epic7 is God-Game.\nTry, try.", Label.CENTER);
		add("Center", lblMessage);
		lblMessage.setFont(new Font("궁서", Font.BOLD, 18));

		Button button = new Button("Click");
		add("South", button);
		button.addActionListener(this);

		setTitle("스레드 연습");
//		setSize(300, 300);
//		setLocation(300, 400);
//		이거 두개는 한줄로 쓸수 있음
		setBounds(300, 400, 300, 300);

		setVisible(true);

		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				flag = true;
				System.exit(0);

			}
		});

		thread = new Thread(this);
	}

	@Override
	public void run() {
		while (true) {
			if (flag == true)
				break;
			
			calShow();
			
			try {
				Thread.sleep(1000);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}

	}

	@Override
	public void actionPerformed(ActionEvent e) {
//		System.out.println("당장 설치해");
//		calShow();
		if (thread.isAlive())
			return;

		thread.start();

	}

	private void calShow() {
		Calendar calendar = Calendar.getInstance();
		int y = calendar.get(Calendar.YEAR);
		int m = calendar.get(Calendar.MONTH) + 1; // 달은 0부터 시작하므로 +1
		int d = calendar.get(Calendar.DATE);
		int h = calendar.get(Calendar.HOUR);
		int mi = calendar.get(Calendar.MINUTE);
		int s = calendar.get(Calendar.SECOND);

		lblMessage.setText(y + " - " + m + " - " + d + "      " + h + ":" + mi + ":" + s);
	}

	public static void main(String[] args) {
		new ThreadTestClock();

	}
}
