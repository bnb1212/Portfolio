package pack1;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class Swing2Part extends JPanel implements ActionListener {

	JButton btnR, btnG, btnB;
	JTextArea txtArea = new JTextArea("", 10, 50);
	JMenuBar mBar;
	JMenuItem mnuMes, mnuOk, mnuInput;

	public Swing2Part() {
		setLayout(new BorderLayout()); // Flow->Border

		btnR = new JButton("빨강");
		btnG = new JButton("초록");
		btnB = new JButton("파랑");
		btnR.addActionListener(this);
		btnG.addActionListener(this);
		btnB.addActionListener(this);

		JPanel panel = new JPanel();
		panel.add(btnR);
		panel.add(btnG);
		panel.add(btnB);

		add("South", panel);
		add("Center", txtArea);

		menuProcess();
	}

	private void menuProcess() {
		mBar = new JMenuBar();

		JMenu menu = new JMenu("대화상자");
		mnuMes = new JMenuItem("메시지");
		mnuOk = new JMenuItem("확인");
		mnuInput = new JMenuItem("입력");

		menu.add(mnuMes);
		menu.add(mnuOk);
		menu.add(mnuInput);

		mBar.add(menu);
		// 메뉴에 리스너 등록
		mnuMes.addActionListener(this);
		mnuOk.addActionListener(this);
		mnuInput.addActionListener(this);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
//		System.out.println(e.getSource());
		if (e.getSource() == btnR) {
			txtArea.setBackground(new Color(255, 0, 0));
		} else if (e.getSource() == btnG) {
			txtArea.setBackground(new Color(0, 255, 0));
		} else if (e.getSource() == btnB) {
			txtArea.setBackground(new Color(0, 0, 255));
		} else if (e.getSource() == mnuMes) { // 메뉴 아이템
			JOptionPane.showMessageDialog(this, "메시지", "알림", JOptionPane.INFORMATION_MESSAGE);
			System.out.println("Modal DialogBox가 닫히면 수행");
		} else if (e.getSource() == mnuOk) {
			int re = JOptionPane.showConfirmDialog(this, "버튼 선택", "골라", JOptionPane.YES_NO_CANCEL_OPTION);
			System.out.println(re);
			switch (re) {
//			case 0:
			case JOptionPane.YES_OPTION:
//				txtArea.setText("예 선택");
				txtArea.append("예 선택\n");
				break;
			case JOptionPane.NO_OPTION:
				txtArea.append("아니 선택\n");
				break;
			case JOptionPane.CANCEL_OPTION:
				txtArea.append("취소 선택\n");
				break;
			}
		} else if (e.getSource() == mnuInput) {
			String str = JOptionPane.showInputDialog(this, "자료입력");
			txtArea.append(str + "\n");
		}
	}

}
