package pack1;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

public class SwingTest3 extends JFrame implements ActionListener {
	JTextField txtName, txtAge;
	ButtonGroup group = new ButtonGroup();
	JRadioButton rdoM, rdoF;
	JLabel lblResult;

	public SwingTest3() {
		super("이벤트 연습");
		layoutInit();

		setBounds(300, 300, 300, 300);
		setVisible(true);

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	private void layoutInit() {
		setLayout(new GridLayout(5, 1));

		// 1행
		JLabel lbl1 = new JLabel("이름 :");
		txtName = new JTextField("", 20);
		JPanel pn1 = new JPanel();
		pn1.add(lbl1);
		pn1.add(txtName);
		add(pn1);

		// 2행
		JLabel lbl2 = new JLabel("나이 :");
		txtAge = new JTextField("", 20);
		JPanel pn2 = new JPanel();
		pn2.add(lbl2);
		pn2.add(txtAge);
		add(pn2);

		// 3행
		rdoM = new JRadioButton("남자", true);
		rdoF = new JRadioButton("여자", false);
		group.add(rdoM);
		group.add(rdoF);
		JPanel pn3 = new JPanel();
		pn3.add(rdoM);
		pn3.add(rdoF);
		add(pn3);

		// 4행
		JButton btnOk = new JButton("결과 확인");
		btnOk.addActionListener(this);
		JPanel pn4 = new JPanel();
		pn4.add(btnOk);
		add(pn4);
		// 5행
		lblResult = new JLabel("결과 : ", JLabel.CENTER);
		add(lblResult);
	}

	@Override
	public void actionPerformed(ActionEvent e) {

		if (txtName.getText().equals("")) {
			lblResult.setText("이름을 입력하시오");
			txtName.requestFocus();
			return;
		}

		if (txtAge.getText().equals("")) {
			lblResult.setText("나이를 입력하시오");
			txtName.requestFocus();
			return;
		}

		int nai = 0;
		try {
			nai = Integer.parseInt(txtAge.getText());
		} catch (Exception e2) {
			lblResult.setText("숫자만 허용");
			txtAge.setText(null);
			txtAge.requestFocus();
			return;
		}

//		System.out.println(rdoM.isSelected() + " " + rdoF.isSelected());
		String gender = "";
		if (rdoM.isSelected()) {
			gender = "남";
		} else {
			gender = "여";
		}

		String msg = "결과 : " + txtName.getText() + "님은 " 
		+ gender + "이고 " 
		+ nai + "살";
		lblResult.setText(msg);
	}

	public static void main(String[] args) {
		new SwingTest3();
	}
}
