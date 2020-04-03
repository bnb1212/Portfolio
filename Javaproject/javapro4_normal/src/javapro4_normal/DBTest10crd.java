package javapro4_normal;

import java.awt.GridLayout;
import java.awt.event.*;
import java.sql.*;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class DBTest10crd extends JFrame implements ActionListener {

	JButton btnIns = new JButton("추가");
	JButton btnDel = new JButton("삭제");
	JButton btnExit = new JButton("종료");
	String[][] datas = new String[0][5];
	String[] title = { "코드", "상품명", "수량", "단가", "금액" };
	DefaultTableModel model = new DefaultTableModel(datas, title);
	JTable table = new JTable(model);
	JLabel lblCou = new JLabel("건수 : 0 ");

	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;

	public DBTest10crd() {

		layInit();
		accDb();

		setTitle("상품 처리");
		setResizable(false);
		setBounds(300, 300, 300, 300);
		setVisible(true);

		addWindowListener(new WindowAdapter() {
			public void windowClosing(java.awt.event.WindowEvent e) {
				int re = JOptionPane.showConfirmDialog(DBTest10crd.this, "정말 종료할까요?", "종료",
						JOptionPane.OK_CANCEL_OPTION);
				if (re == JOptionPane.OK_OPTION) {
					try {
						if (rs != null)
							rs.close();
						if (pstmt != null)
							pstmt.close();
						if (conn != null)
							conn.close();
					} catch (Exception e7) {
						// TODO: handle exception
					} finally {
						System.exit(0);
					}
				} else {
					setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
				}
			};
		});
	}

	private void layInit() {
		JPanel panel = new JPanel();
		panel.add(btnIns);
		panel.add(btnDel);
		panel.add(btnExit);
		add("North", panel);

		table.getColumnModel().getColumn(0).setPreferredWidth(30);
		JScrollPane scrollPane = new JScrollPane(table);
		add("Center", scrollPane);

		add("South", lblCou);

		// ==== Listener =====
		btnIns.addActionListener(this);
		btnDel.addActionListener(this);
		btnExit.addActionListener(this);
	}

	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("accessDb err : " + e);
			return;
		}

		dispData();
	}

	public void dispData() {
		model.setNumRows(0);
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			pstmt = conn.prepareStatement("select * from sangdata");
			rs = pstmt.executeQuery();

			int count = 0;
			while (rs.next()) {
				int keum = rs.getInt("su") * rs.getInt("dan");

				String[] imsi = { rs.getString("code"), rs.getString("sang"), rs.getString("su"), rs.getString("dan"),
						Integer.toString(keum) };
				model.addRow(imsi);
				count++;
			}

			lblCou.setText("건수 : " + count);
		} catch (Exception e3) {
			System.out.println(e3);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == btnIns) { // 상품 추가
			InsertForm insertForm = new InsertForm(this);

			dispData(); // 추가후 자료보-기

		} else if (e.getSource() == btnDel) { // 상품 삭제
			String delNo = JOptionPane.showInputDialog(this, "삭제할 코드 입력");
//			System.out.println(delNo);
			if (delNo == null)
				return;

			try {
				conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
				String sql = "delete from sangdata where code=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setInt(1, Integer.parseInt(delNo));
				if(pstmt.executeUpdate() == 0) {
					JOptionPane.showMessageDialog(this, delNo + "번은 등록된 코드가 아닙니다.");
					return;
				}
				
				dispData();
			} catch (Exception e8) {
				System.out.println("삭제 실패 " + e8);
			} finally {
				try {
					if (rs != null)
						rs.close();
					if (pstmt != null)
						pstmt.close();
					if (conn != null)
						conn.close();
				} catch (Exception e9) {
					System.out.println("연결 에러");
				}

				
			}
		} else if (e.getSource() == btnExit) { // 종료
			int re = JOptionPane.showConfirmDialog(DBTest10crd.this, "정말 종료할까요?", "종료", JOptionPane.OK_CANCEL_OPTION);
			if (re == JOptionPane.OK_OPTION) {
				try {
					if (rs != null)
						rs.close();
					if (pstmt != null)
						pstmt.close();
					if (conn != null)
						conn.close();
				} catch (Exception e2) {
					// TODO: handle exception
				} finally {
					System.exit(0);
				}
			} else {
				setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
			}
		}
	}

	// 추가를 위한 내부 클래스
	class InsertForm extends JDialog implements ActionListener {
		JTextField txtSang = new JTextField();
		JTextField txtSu = new JTextField();
		JTextField txtDan = new JTextField();

		JButton btnOk = new JButton("등록");
		JButton btnCancel = new JButton("지움");

		public InsertForm(JFrame frame) {
			super(frame, "상품 추가", true);

			JPanel pn1 = new JPanel(new GridLayout(4, 2));
			pn1.add(new JLabel("품명"));
			pn1.add(txtSang);
			pn1.add(new JLabel("수량"));
			pn1.add(txtSu);
			pn1.add(new JLabel("단가"));
			pn1.add(txtDan);

			pn1.add(btnOk);
			pn1.add(btnCancel);

			btnOk.addActionListener(this);
			btnCancel.addActionListener(this);

			add("North", new JLabel("상품자료 입력"));
			add("Center", pn1);

			setBounds(310, 310, 200, 150);
			setVisible(true);

			addWindowListener(new WindowAdapter() {
				@Override
				public void windowClosing(WindowEvent e) {
					dispose();
				}
			});

		}

		@Override
		public void actionPerformed(ActionEvent e) {
//			System.out.println("aa");
			if (e.getSource() == btnOk) { // 상품 추가
				// 입력자료 검사
				if (txtSang.getText().equals("")) {
					JOptionPane.showMessageDialog(this, "상품명 입력");
					txtSang.requestFocus();
					return;
				}

				if (txtSu.getText().equals("")) {
					JOptionPane.showMessageDialog(this, "수량 입력");
					txtSu.requestFocus();
					return;
				}

				if (txtDan.getText().equals("")) {
					JOptionPane.showMessageDialog(this, "단가 입력");
					txtDan.requestFocus();
					return;
				}

				int su = 0;
				try {
					su = Integer.parseInt(txtSu.getText().trim());
				} catch (Exception e4) {
					JOptionPane.showMessageDialog(this, "수량은 숫자만 허용");
					txtSu.requestFocus();
					return;
				}

				int dan = 0;
				try {
					dan = Integer.parseInt(txtDan.getText().trim());
				} catch (Exception e5) {
					JOptionPane.showMessageDialog(this, "단가는 숫자만 허용");
					txtDan.requestFocus();
					return;
				}

				// 등록 가능한 상태
				try {
					conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
					// 새 상품 코드 얻기
					int new_code = 0;

					String sql = "select max(code) from sangdata";
					pstmt = conn.prepareStatement(sql);
					rs = pstmt.executeQuery();
					if (rs.next()) {
						new_code = rs.getInt(1); // new_code = rs.getInt("max");

					}
//					System.out.println("새상품 코드 : " + (new_code + 1));

//					sql = "insert into sangdata values(" + new_code + "," + txtSang.getText() + ...)  // Statement에서는 이런식으로 밖에 못함
					sql = "insert into sangdata values(?,?,?,?)";
					pstmt = conn.prepareStatement(sql);

					pstmt.setInt(1, (new_code + 1));
					pstmt.setString(2, txtSang.getText());
					pstmt.setInt(3, su);
					pstmt.setInt(4, dan);
//					int re = pstmt.executeUpdate();
//					if(re>0){ }
					if (pstmt.executeUpdate() > 0) { // executeUpdate는 insert delete update문이 성공적으로 수행되면 수행된 개수만큼 int값
														// 반환. 0이면 실패
						JOptionPane.showMessageDialog(this, "등록성공");
					} else {
						JOptionPane.showMessageDialog(this, "등록실패");
					}

				} catch (Exception e6) {
					System.out.println("신상품 추가 에러 : " + e6);
				}
			} else if (e.getSource() == btnCancel) { // 입력자료 초기화
				txtSang.setText("");
				txtSu.setText(null);
				txtDan.setText(null);
				txtSang.requestFocus();
			}
		}
	}

	public static void main(String[] args) {
		new DBTest10crd();
	}
}
