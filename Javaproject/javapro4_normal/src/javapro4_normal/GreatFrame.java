package javapro4_normal;

import java.awt.event.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javapro4_normal.GreatInsert;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class GreatFrame extends JFrame implements ActionListener {

	Connection conn;
	PreparedStatement pstmt1, pstmt2, pstmt3;
	ResultSet rs1, rs2, rs3;

	private String sql;
	private String selGreatName = "";

	// 레이아웃 관련 변수
	private JLabel lblGukga;
	private JTextField txtGukga;
	private JButton btnIns, btnMod, btnDel;

	// Table 관련 멤버변수
	String datas[][] = new String[0][4];
	String[] title = { "위인번호", "이름", "성별", "직업" };
	DefaultTableModel model = new DefaultTableModel(datas, title) { 
		public boolean isCellEditable(int row, int column) { // 셀 수정 불가
			return false;
		}
	};
	JTable table = new JTable(model);

	private int gukgaNum;

	// ===== CONSTRUCTOR ====
	public GreatFrame(int gukgaNum) {
		super("해당 국가 위인");
		this.gukgaNum = gukgaNum;
		layInit(gukgaNum);

		setBounds(300, 300, 400, 400);
		setVisible(true);

		accDb();
		showData();

		this.addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				dispose();
			}
		});

		table.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				table = (JTable) e.getComponent();
				model = (DefaultTableModel) table.getModel();
				selGreatName = (String) model.getValueAt(table.getSelectedRow(), 1);

				showInfo();
			}
		});
	}

	// ==== LAYOUT INIT ====
	private void layInit(int gukgaNum) {
		// 상단
		JPanel norPanel = new JPanel();
		lblGukga = new JLabel("국가 : ");
		txtGukga = new JTextField(GukgaMain.gukgaName, 10);
		txtGukga.setEditable(false);
		norPanel.add(lblGukga);
		norPanel.add(txtGukga);

		// 중단 테이블
		table.getColumnModel().getColumn(0).setPreferredWidth(10);
		table.getColumnModel().getColumn(1).setPreferredWidth(100);
		table.getColumnModel().getColumn(2).setPreferredWidth(20);
		JScrollPane cenPanel = new JScrollPane(table);

		// 하단 버튼 레이아웃 패널
		JPanel souPanel = new JPanel();
		btnIns = new JButton("등록");
		btnDel = new JButton("삭제");
		btnMod = new JButton("수정");
		souPanel.add(btnIns);
		souPanel.add(btnMod);
		souPanel.add(btnDel);

		btnIns.addActionListener(this);
		btnMod.addActionListener(this);
		btnDel.addActionListener(this);

		// 프레임에 추가
		add("North", norPanel);
		add("Center", cenPanel);
		add("South", souPanel);
	}

	// ==== accDB ====
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception accErr) {
			System.out.println("accessDb err : " + accErr);
			return;
		}
	}

	// ==== SHOW DATA ==== // 화면에 데이터 출력
	private void showData() {

		model.setNumRows(0);
		sql = "select * from greatpeople where great_country = ?";
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");

			pstmt1 = conn.prepareStatement(sql);
			pstmt1.setInt(1, gukgaNum);
			rs1 = pstmt1.executeQuery();
			while (rs1.next()) {
				String[] data = { rs1.getString(1), rs1.getString(2), rs1.getString(5), rs1.getString(7) };
				model.addRow(data);
			}

		} catch (Exception showErr) {
			System.out.println("showData err : " + showErr);
		} finally {
			try {
				if (rs1 != null)
					rs1.close();
				if (rs2 != null)
					rs2.close();
				if (rs3 != null)
					rs3.close();
				if (pstmt1 != null)
					pstmt1.close();
				if (pstmt2 != null)
					pstmt2.close();
				if (pstmt3 != null)
					pstmt3.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}

	// ==== SHOW INFO ====
	private void showInfo() { // 클릭한 인물의 정보와 출생일을 다이얼로그로 보여줌
		try {
			String ss = "";
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			String sql2 = "select great_name, great_birth, great_info from" + " greatpeople" + " where great_name=?";
			pstmt2 = conn.prepareStatement(sql2);
			pstmt2.setString(1, selGreatName);
			rs2 = pstmt2.executeQuery();

			while (rs2.next()) {
				ss = "이름 : " + rs2.getString("great_name") + "\n" + "출생일 : " + rs2.getString("great_birth") + "\n"
						+ "정보 : " + rs2.getString("great_info") + "\n";
			}
			JOptionPane.showMessageDialog(this, ss, "인물정보", JOptionPane.PLAIN_MESSAGE);

		} catch (Exception shResultErr) {
			System.out.println("결과출력 에러 : " + shResultErr);
		} finally {
			try {
				if (rs1 != null)
					rs1.close();
				if (rs2 != null)
					rs2.close();
				if (rs3 != null)
					rs3.close();
				if (pstmt1 != null)
					pstmt1.close();
				if (pstmt2 != null)
					pstmt2.close();
				if (pstmt3 != null)
					pstmt3.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {
				// TODO: handle exception
			}
		}
	}

	// ==== ACTION PERFROMED ====
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
		if (e.getSource() == btnIns) { // 인물 추가
			GreatInsert greatInsert = new GreatInsert(this, gukgaNum);

			showData(); // 추가후 자료보-기
			selGreatName = ""; // 선택 해제
		}

		if (e.getSource() == btnMod) { // 인물 추가
			if (selGreatName.equals("")) {
				JOptionPane.showMessageDialog(this, "수정할 행 선택");
				return;
			}
			GreatUpdate greatUpdate = new GreatUpdate(this, selGreatName);

			
			showData(); // 추가후 자료보-기
			selGreatName = "";
		}

		if (e.getSource() == btnDel) { // 인물 삭제
			try {
				if (selGreatName.equals("")) {
					JOptionPane.showMessageDialog(this, "삭제할 행 선택");
					return;
				}
				conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
				String sql = "delete from greatpeople where great_name=?";
				pstmt3 = conn.prepareStatement(sql);
				pstmt3.setString(1, selGreatName);
				if (pstmt3.executeUpdate() == 0) {
					JOptionPane.showMessageDialog(this, "삭제 실패");
					return;
				}
				selGreatName = "";

			} catch (Exception e8) {
				System.out.println("삭제 실패 " + e8);
			} finally {
				try {
					if (rs3 != null)
						rs3.close();
					if (pstmt3 != null)
						pstmt3.close();
					if (conn != null)
						conn.close();
				} catch (Exception e9) {
					System.out.println("연결 에러");
				}

				showData(); // 추가후 자료보-기
			}
			
		}

	}
	
	public static void main(String[] args) {
//		new GreatFrame(1);
	}
}
