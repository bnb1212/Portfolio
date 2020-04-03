package pack1;

import java.awt.Color;
import java.awt.FileDialog;
import java.awt.event.*;
import java.io.*;

import javax.swing.*;

public class MemoJang extends JFrame implements ActionListener {
	// ==== MEMBER ====
	private JButton btnCopy = new JButton("Copy");
	private JButton btnPaste = new JButton("Paste");
	private JButton btnCut = new JButton("Cut");
	private JButton btnDel = new JButton("Delete");
	private JPanel pn = new JPanel();
	private JTextArea txtMemo = new JTextArea("", 10, 30);

	// 메뉴

	private JMenuItem mnuNew, mnuSave, mnuOpen, mnuExit;
	private JMenuItem mnuCopy, mnuPaste, mnuCut, mnuDel;
	private JMenuItem mnuAbout, mnuEtc1, mnuEtc2;

	// POP-UP 메뉴
	JPopupMenu popup;
	JMenuItem m_white, m_blue, m_yellow;
	private String copyText;

	public MemoJang() {
		super("간단 메모장 by Java");
		initLayout();
		menuLayout();

		setBounds(300, 300, 500, 400);
		setVisible(true);

		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				int re = JOptionPane.showConfirmDialog(MemoJang.this, "정말 종료할까요?", "종료", JOptionPane.YES_NO_OPTION);
				if (re == JOptionPane.YES_OPTION) {
					setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

				} else {
					setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
				}
			}
		});
	}

	private void menuLayout() {
		JMenuBar menuBar = new JMenuBar();

		JMenu mnuFile = new JMenu("파일");
		mnuNew = new JMenuItem("새문서");
		mnuOpen = new JMenuItem("열기...");
		mnuSave = new JMenuItem("저장...");
		mnuExit = new JMenuItem("끝내기");

		mnuFile.add(mnuNew);
		mnuFile.add(mnuOpen);
		mnuFile.add(mnuSave);
		mnuFile.addSeparator();
		mnuFile.add(mnuExit);
		mnuFile.addSeparator();

		JMenu mnuEdit = new JMenu("편집");
		mnuCopy = new JMenuItem("복사");
		mnuPaste = new JMenuItem("붙여넣기");
		mnuCut = new JMenuItem("잘라내기");
		mnuDel = new JMenuItem("삭제");
		mnuEdit.add(mnuCopy);
		mnuEdit.add(mnuPaste);
		mnuEdit.add(mnuCut);
		mnuEdit.add(mnuDel);

		JMenu mnuHelp = new JMenu("도움멀");

		mnuHelp = new JMenu("도움말");
		mnuAbout = new JMenuItem("메모장이란...");
		JMenu mnuEtc = new JMenu("기타");
		mnuEtc1 = new JMenuItem("계산기");
		mnuEtc2 = new JMenuItem("프리셀");

		mnuEtc.add(mnuEtc1);
		mnuEtc.add(mnuEtc2);
		mnuHelp.add(mnuAbout);
		mnuHelp.add(mnuEtc);

		menuBar.add(mnuFile);
		menuBar.add(mnuEdit);
		menuBar.add(mnuHelp);
		setJMenuBar(menuBar);

		mnuNew.addActionListener(this);
		mnuSave.addActionListener(this);
		mnuOpen.addActionListener(this);
		mnuExit.addActionListener(this);

		mnuCopy.addActionListener(this);
		mnuPaste.addActionListener(this);
		mnuCut.addActionListener(this);
		mnuDel.addActionListener(this);

		mnuAbout.addActionListener(this);
		mnuEtc1.addActionListener(this);
		mnuEtc2.addActionListener(this);

		popup = new JPopupMenu();
		JMenu m_color = new JMenu("배경색 선택");
		m_white = new JMenuItem("하양");
		m_blue = new JMenuItem("파랑");
		m_yellow = new JMenuItem("노랑");
		m_color.add(m_white);
		m_color.add(m_blue);
		m_color.add(m_yellow);
		popup.add(m_color);
		txtMemo.add(popup);

		m_white.addActionListener(this);
		m_blue.addActionListener(this);
		m_yellow.addActionListener(this);

		txtMemo.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				if (e.getModifiersEx() == MouseEvent.getMaskForButton(3))
					popup.show(txtMemo, e.getX(), e.getY());
			}

		});
	}

	private void initLayout() {
		pn.add(btnCopy);
		pn.add(btnPaste);
		pn.add(btnCut);
		pn.add(btnDel);
		add("South", pn);
		JScrollPane scrollPane = new JScrollPane(txtMemo);
		add("Center", scrollPane);

		btnCopy.addActionListener(this);
		btnPaste.addActionListener(this);
		btnCut.addActionListener(this);
		btnDel.addActionListener(this);

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if (e.getSource() == btnCopy || e.getSource() == mnuCopy) {
//			copyText = txtMemo.getText();
			copyText = txtMemo.getSelectedText();
			System.out.println(copyText);

		} else if (e.getSource() == btnPaste || e.getSource() == mnuPaste) {
//			txtMemo.setText(copyText);
			int position = txtMemo.getCaretPosition();
			System.out.println(position);
			txtMemo.insert(copyText, position);

		} else if (e.getSource() == btnCut || e.getSource() == mnuCut) {
			copyText = txtMemo.getSelectedText();
			int start = txtMemo.getSelectionStart();
			int end = txtMemo.getSelectionEnd();
			txtMemo.replaceRange("", start, end);

		} else if (e.getSource() == btnDel || e.getSource() == mnuDel) {
			int start = txtMemo.getSelectionStart();
			int end = txtMemo.getSelectionEnd();
			txtMemo.replaceRange("", start, end);
		} else if (e.getSource() == mnuNew) {
			txtMemo.setText("");
			setTitle("제목 없음");

		} else if (e.getSource() == mnuOpen) {
			FileDialog dialog = new FileDialog(this, "열기", FileDialog.LOAD);
			dialog.setDirectory(".");
			dialog.setVisible(true);
			if (dialog.getFile() == null)
				return;
			String dfName = dialog.getDirectory() + dialog.getFile();
//			System.out.println(dfName);
			try {
				BufferedReader reader = new BufferedReader(new FileReader(dfName));
				txtMemo.setText("");
				String line;
				while ((line = reader.readLine()) != null) {
					txtMemo.append(line + "\n");
				}
				reader.close();
				this.setTitle(dialog.getFile());
			} catch (Exception e2) {

				// TODO: handle exception
			}
		} else if (e.getSource() == mnuSave) {
			// 저장을 위한 경로명 및 파일명 등을 얻기 위한 운영체제의 대화상자 호출
			FileDialog dialog = new FileDialog(this, "저장", FileDialog.SAVE);
			dialog.setDirectory(".");
			dialog.setVisible(true);
			if (dialog.getFile() == null)
				return;
			String dfName = dialog.getDirectory() + dialog.getFile();
//			System.out.println(dfName);
			try {
				BufferedWriter writer = new BufferedWriter(new FileWriter(dfName));
				writer.write(txtMemo.getText());
				writer.close();

				this.setTitle(dialog.getFile());
			} catch (Exception e2) {
				System.out.println("save err : " + e2);
			}
		} else if (e.getSource() == mnuExit) {
			// ...
			System.exit(0);
			

		} else if (e.getSource() == mnuAbout) { 			//도움말
			new MemoAbout(this);
			System.out.println("대화상자 호출 후 ------------");
		} else if (e.getSource() == mnuEtc1) {
			try {
				Runtime.getRuntime().exec("calc.exe");
			} catch (Exception e2) {
				System.out.println("프리셀이 설치되지 않았습니다");
			}
		} else if (e.getSource() == mnuEtc2) {

		} else if (e.getSource().equals(m_white)) {
			txtMemo.setBackground(Color.white);
		} else if (e.getSource().equals(m_blue)) {
			txtMemo.setBackground(new Color(0, 0, 255));
		} else if (e.getSource().equals(m_yellow)) {
			txtMemo.setBackground(new Color(255, 255, 0));
		}
		txtMemo.requestFocus();
	}

	public static void main(String[] args) {
		new MemoJang();
		/*
		String ss = "1 2 3 4 5";
		String numlist[] = ss.split(" ");
		for (int i = 0; i < numlist.length; i++) {
			System.out.println(numlist[i]);
		}
		*/
	}
}
