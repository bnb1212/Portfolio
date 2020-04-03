package javapro4_normal;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.*;

public class GreatInsert extends JDialog implements ActionListener {
	JTextField txtName = new JTextField("", 5);
	JTextArea txtInfo = new JTextArea();
	JTextField txtBirth = new JTextField("", 10);
	JTextField txtJik = new JTextField("", 6);
	ButtonGroup group = new ButtonGroup();
	JRadioButton rBtnMale = new JRadioButton("남");
	JRadioButton rBtnFemale = new JRadioButton("여");
	private int gukgaNum;
	JButton btnOk = new JButton("등록");
	JButton btnReset = new JButton("모두 지움");

	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;

	public GreatInsert(JFrame frame, int gukgaNum) {
		super(frame, "인물 추가", true);
		this.gukgaNum = gukgaNum;
		// ==== 추가 폼 레이아웃 ====
		layInit();
		
		setBounds(310, 310, 550, 200);
		setVisible(true);
		setResizable(false);

		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				dispose();
			}
		});

	}

	public void layInit() {
		// 상단
		JPanel NorPanel = new JPanel();
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

			// 등록 가능한 상태
			try {
				conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
				int new_code = 0;

				String sql = "select max(great_no) from greatpeople";
				pstmt = conn.prepareStatement(sql);
				rs = pstmt.executeQuery();
				if (rs.next()) {
					new_code = rs.getInt(1);

				}

				sql = "insert into greatpeople values(?,?,?,?,?,?,?)";
				pstmt = conn.prepareStatement(sql);
				pstmt.setInt(1, (new_code + 1));
				pstmt.setString(2, txtName.getText());
				pstmt.setString(3, txtInfo.getText());
				pstmt.setString(4, txtBirth.getText());
				if (rBtnMale.isSelected())
					pstmt.setString(5, "남");
				else
					pstmt.setString(5, "여");
				pstmt.setInt(6, gukgaNum);
				pstmt.setString(7, txtJik.getText());
				
				if (pstmt.executeUpdate() > 0) { // executeUpdate는 insert delete update문이 성공적으로 수행되면 수행된 개수만큼 int값
													// 반환. 0이면 실패
					JOptionPane.showMessageDialog(this, "등록성공");
					dispose();
				} else {
					JOptionPane.showMessageDialog(this, "등록 실패. 위인번호는 한글만 가능합니다.");
				}

			} catch (Exception e6) {
				System.out.println("국가 추가 에러 : " + e6);
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