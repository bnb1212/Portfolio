package javapro4_normal;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class GreatUpdate extends JDialog implements ActionListener {
	
	JTextField txtNo = new JTextField("", 3);
	JTextField txtName = new JTextField("", 5);
	JTextArea txtInfo = new JTextArea();
	JTextField txtBirth = new JTextField("", 10);
	JTextField txtJik = new JTextField("", 6);
	ButtonGroup group = new ButtonGroup();
	JRadioButton rBtnMale = new JRadioButton("남");
	JRadioButton rBtnFemale = new JRadioButton("여");
	private String greatName = ""; 
	JButton btnOk = new JButton("수정");
	JButton btnReset = new JButton("모두 지움");

	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;

	// ===
	public GreatUpdate(JFrame frame, String greatName) {
		super(frame, "인물 수정", true);
		this.greatName = greatName;
		// ==== 추가 폼 레이아웃 ====
		layInit();

		setBounds(310, 310, 650, 300);
		setVisible(true);
		setResizable(false);

		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				dispose();
			}
		});

	}

	private void layInit() {
		// 상단
		JPanel NorPanel = new JPanel();
		NorPanel.add(new JLabel("위인 번호 : "));
		NorPanel.add(txtNo);		
		NorPanel.add(new JLabel("이름 : "));
		NorPanel.add(txtName);
		NorPanel.add(new JLabel("출생일 : "));
		NorPanel.add(txtBirth);
		NorPanel.add(new JLabel("성별"));

		group.add(rBtnMale);
		group.add(rBtnFemale);

		NorPanel.add(rBtnMale);
		NorPanel.add(rBtnFemale);
		NorPanel.add(new JLabel("직업 : "));
		NorPanel.add(txtJik);

		// 중단
		JPanel SouPanel = new JPanel();
		JLabel info = new JLabel("설명 ");
		JScrollPane scrollPane = new JScrollPane(txtInfo);

		// 하단 버튼
		JPanel btnPanel = new JPanel();
		btnPanel.add(btnOk);
		btnPanel.add(btnReset);
		SouPanel.add("North", info);
		SouPanel.add("South", btnPanel);
		btnOk.addActionListener(this);
		btnReset.addActionListener(this);
		// 프레임에 패널 추가
		add("North", NorPanel);
		add("West", info);
		add("Center", scrollPane);
		add("South", SouPanel);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == btnOk) { // 위인 추가
			// 입력자료 검사
			if (txtName.getText().equals("")) {
				JOptionPane.showMessageDialog(this, "이름 입력");
				txtName.requestFocus();
				return;
			}

			if (txtBirth.getText().equals("")) {
				JOptionPane.showMessageDialog(this, "출생일 입력");
				txtBirth.requestFocus();
				return;
			}

			if (txtJik.getText().equals("")) {
				JOptionPane.showMessageDialog(this, "직업 입력");
				txtJik.requestFocus();
				return;
			}

			// 수정 가능한 상태
			try {
				conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
				String sql = "";

				sql = "update greatpeople"
						+ " set great_no = ?, great_name = ?, great_info = ?,"
						+ " great_birth = ?, great_gen = ?, great_jik = ?"
						+ " where great_name = ?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setInt(1, Integer.parseInt(txtNo.getText()));
				pstmt.setString(2, txtName.getText());
				pstmt.setString(3, txtInfo.getText());
				pstmt.setString(4, txtBirth.getText());
				if (rBtnMale.isSelected())
					pstmt.setString(5, "남");
				else
					pstmt.setString(5, "여");
				pstmt.setString(6, txtJik.getText());
				pstmt.setString(7, greatName);

				if (pstmt.executeUpdate() > 0) { // executeUpdate는 insert delete update문이 성공적으로 수행되면 수행된 개수만큼 int값
													// 반환. 0이면 실패
					JOptionPane.showMessageDialog(this, "수정 성공");
					dispose();
				} else {
					JOptionPane.showMessageDialog(this, "수정 실패");
				}

			} catch (Exception e6) {
				System.out.println(e6);
				JOptionPane.showMessageDialog(this, "위인번호 중복");
			}
		} else if (e.getSource() == btnReset) { // 입력자료 초기화
			txtName.setText("");
			txtInfo.setText(null);
			txtBirth.setText(null);
			txtName.setText(null);
			rBtnMale.getSelectedObjects();
			txtName.requestFocus();
		}
	}
}
