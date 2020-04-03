package pack1;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

@SuppressWarnings("serial")
public class CalculatorMain extends JFrame implements ActionListener {
	// ==== MEMBER ====
	JTextField number1, number2;
	JButton btnCal, btnReset, btnEnd;
	ButtonGroup btnGroup = new ButtonGroup();
	JRadioButton btnPlus, btnMinus, btnMul, btnSub;
	JLabel lblResult;

	// ==== CONSTRUCTOR ====
	public CalculatorMain() {
		super("미니 계산기");
		layoutInit();

		setBounds(300, 300, 300, 400);
		setVisible(true);

		setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
	}

	// ==== METHOD ====

	private void layoutInit() { // 레이아웃 설정(초기화)
		setLayout(new GridLayout(4, 1));

		// 숫자 입력받기
		JLabel noLabel1 = new JLabel("숫자1 :");
		number1 = new JTextField("", 20);

		JLabel noLabel2 = new JLabel("숫자2 :");
		number2 = new JTextField("", 20);
		JPanel pn1 = new JPanel();
		pn1.add(noLabel1);
		pn1.add(number1);
		pn1.add(noLabel2);
		pn1.add(number2);
		add(pn1);

		// 연산 버튼들
		operatorBtnInit();

		// 결과값
		lblResult = new JLabel("결과 : \n", JLabel.CENTER);
		add(lblResult);

		// 버튼들
		btnLayoutInit();
	}

	private void operatorBtnInit() { // 연산버튼 레이아웃
		JLabel selectBtn = new JLabel("연산 선택 : ");
		btnPlus = new JRadioButton("+", true);
		btnMinus = new JRadioButton("-", false);
		btnMul = new JRadioButton("*", false);
		btnSub = new JRadioButton("/", false);

		btnGroup.add(btnPlus);
		btnGroup.add(btnMinus);
		btnGroup.add(btnMul);
		btnGroup.add(btnSub);
		JPanel pn3 = new JPanel();

		pn3.add(selectBtn);
		pn3.add(btnPlus);
		pn3.add(btnMinus);
		pn3.add(btnMul);
		pn3.add(btnSub);
		add(pn3);
	}

	private void btnLayoutInit() { // 처리버튼 레이아웃

		btnCal = new JButton("계산");
		btnReset = new JButton("초기화");
		btnEnd = new JButton("종료");
		
		btnCal.addActionListener(this);
		btnReset.addActionListener(this);
		btnEnd.addActionListener(this);

		JPanel pn4 = new JPanel();
		pn4.add(btnCal);
		pn4.add(btnReset);
		pn4.add(btnEnd);

		add("South", pn4);
	}

	private void calBtnProcess() { // 계산 처리

		
		if (number1.getText().equals("")) {
			lblResult.setText("숫자1을 입력하세요");
			number1.requestFocus();
			return;
		}

		if (number2.getText().equals("")) {
			lblResult.setText("숫자2를 입력하세요");
			number2.requestFocus();
			return;
		}

		double no1 = 0;
		double no2 = 0;

		try {
			no1 = Double.parseDouble(number1.getText());
			no2 = Double.parseDouble(number2.getText());
		} catch (Exception e2) {
			lblResult.setText("숫자만 허용");
			System.out.println(e2);
			number1.requestFocus();
			return;
		}

		String result = "";
		if (btnPlus.isSelected()) {
			result = "결과 : \n" + (no1 + no2);
			lblResult.setText(result);
		} else if (btnMinus.isSelected()) {
			result = "결과 : \n" + (no1 - no2);
			lblResult.setText(result);
		} else if (btnMul.isSelected()) {
			result = "결과 : \n" + (no1 * no2);
			lblResult.setText(result);
		} else if (btnSub.isSelected()) {
			if (no2 == 0.0) {
				lblResult.setText("0으로 나눌수 없습니다.");
			} else {
				result = "결과 : \n" + (no1 / no2);
				lblResult.setText(result);
			}
		}

	}

	private void resetBtnProcess() { // 초기화 처리
		number1.setText(null);
		number2.setText(null);
		btnPlus.setSelected(true);
		lblResult.setText("결과 : \n");
	}

	private void exitBtnProcess() { // 종료버튼
		int re = JOptionPane.showConfirmDialog(this, "종료할까요?", "종료", JOptionPane.OK_CANCEL_OPTION);
		switch (re) {
		case JOptionPane.OK_OPTION:
			System.exit(0);
			break;
		case JOptionPane.NO_OPTION:
			break;
		}
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if (e.getSource() == btnCal)
			calBtnProcess();
		else if (e.getSource() == btnReset)
			resetBtnProcess();
		else if (e.getSource() == btnEnd)
			exitBtnProcess();
	}

	// ==== Main ====
	public static void main(String[] args) {
		new CalculatorMain();
	}

}
