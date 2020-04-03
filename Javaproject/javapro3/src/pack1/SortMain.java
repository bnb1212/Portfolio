package pack1;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

@SuppressWarnings("serial")
public class SortMain extends JFrame implements ActionListener {
	// ==== MEMBER ====
	JTextField inputNumber, result;
	JButton btnSelection, btnBub, btnClr;

	// ==== CONSTRUCTOR ====
	public SortMain() {
		super("정렬 연습");
		layoutInit();

		setBounds(300, 300, 300, 200);
		setVisible(true);

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	// ==== METHOD ====
	private void layoutInit() {
		setLayout(new GridLayout(3, 1));

		// 숫자 입력받기
		JLabel noLabel1 = new JLabel("대상 :");
		inputNumber = new JTextField("", 20);

		JLabel noLabel2 = new JLabel("결과 : ");
		result = new JTextField("", 20);
		JPanel pn1 = new JPanel();
		pn1.add(noLabel1);
		pn1.add(inputNumber);
		pn1.add(noLabel2);
		pn1.add(result);
		add(pn1);

		// 연산 버튼들
		sortBtnInit();

	}

	private void sortBtnInit() {
		btnSelection = new JButton("Selection");
		btnBub = new JButton("Bubble");
		btnClr = new JButton("Clear");

		btnSelection.addActionListener(this);
		btnBub.addActionListener(this);
		btnClr.addActionListener(this);

		JPanel pn4 = new JPanel();
		pn4.add(btnSelection);
		pn4.add(btnBub);
		pn4.add(btnClr);

		add("South", pn4);
	}

	private void btnSelectionProcess() {
		// ==== NumCheck ====
		numCheck();

		// ==== Selection ====
		String[] sel = inputNumber.getText().split("");
		for (int i = 0; i < sel.length - 1; i++) {
			for (int j = i + 1; j < sel.length; j++) {
				if (Integer.parseInt(sel[i]) > Integer.parseInt(sel[j])) {
					String temp = sel[i];
					sel[i] = sel[j];
					sel[j] = temp;
				}
			}

		}
		String selresult = "";

		for (int k = 0; k < sel.length; k++) {
			selresult = selresult + sel[k];
		}

		result.setText(selresult);
	}

	private void btnBubProcess() {
		numCheck();
		
		String[] bub = inputNumber.getText().split("");
		for (int i = 0; i < bub.length - 1; i++) {
			for (int j = 0; j < bub.length - i - 1; j++) {
				if (Integer.parseInt(bub[j]) > Integer.parseInt(bub[j + 1])) {
					String temp = bub[j];
					bub[j] = bub[j + 1];
					bub[j + 1] = temp;
				}
			}

		}

		String bubResult = "";
		for (int k = 0; k < bub.length; k++) {
			bubResult = bubResult + bub[k];
		}

		result.setText(bubResult);
	}

	private void btnClrProcess() {

		inputNumber.setText(null);
		result.setText(null);

	}

	private void numCheck() {
		if (inputNumber.getText().equals("")) {
			result.setText("정렬숫자를 입력하세요");
			inputNumber.requestFocus();
			return;
		}
		int num = 0;
		try {
			num = Integer.parseInt(inputNumber.getText());
		} catch (Exception e2) {
			result.setText("숫자만 허용");
			System.out.println(e2);
			inputNumber.requestFocus();
			return;
		}
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if (e.getSource() == btnSelection)
			btnSelectionProcess();
		else if (e.getSource() == btnBub)
			btnBubProcess();
		else if (e.getSource() == btnClr)
			btnClrProcess();
	}

	public static void main(String[] args) {
		new SortMain();

	}
}
