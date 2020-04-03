package javapro4_normal;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class DBTest5Ex extends JFrame implements ActionListener {
	JButton btnFir, btnPre, btnNext, btnLast;
	JTextField txtNo, txtName, txtBuserName, txtBuserTel;
	JTextArea txtResult = new JTextArea();
	JLabel gogekCount = new JLabel("인원수 : 0명\t");
	
	Connection conn;
	Statement stmt;
	ResultSet rs,rs2;

	public DBTest5Ex() {
		layInit();
		accDb();

		setTitle("DB문제");

		setBounds(300, 300, 500, 500);
		setVisible(true);
//		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				try {
					if (rs != null)
						rs.close();
					if (stmt != null)
						stmt.close();
					if (conn != null)
						conn.close();
				} catch (Exception e2) {
					// TODO: handle exception
				}
				System.exit(0);
			}
		});
	}

	public void layInit() {
		// ===== 상단 =====
		JPanel panel = new JPanel();
		JLabel jikNo = new JLabel("사번 : ");
		JLabel jikName = new JLabel("이름 : ");
		JLabel BusName = new JLabel("부서명 : ");
		JLabel BusTel = new JLabel("부서전화 : ");

		txtNo = new JTextField("", 3);
		txtName = new JTextField("", 6);
		txtBuserName = new JTextField("", 5);
		txtBuserTel = new JTextField("", 10);

		// 버튼 패널
		JPanel btnPanel = new JPanel();
		btnFir = new JButton("|<<");
		btnPre = new JButton("<");
		btnNext = new JButton(">");
		btnLast = new JButton(">>|");

		btnPanel.add(btnFir);
		btnPanel.add(btnPre);
		btnPanel.add(btnNext);
		btnPanel.add(btnLast);

		// 버튼과 입력부를 패널 1에 추가

		panel.add(jikNo);
		panel.add(txtNo);
		panel.add(jikName);
		panel.add(txtName);
		panel.add(BusName);
		panel.add(txtBuserName);
		panel.add(BusTel);
		panel.add(txtBuserTel);
		panel.add(btnPanel);

		txtNo.setEditable(false);
		txtName.setEditable(false);
		txtBuserName.setEditable(false);
		txtBuserTel.setEditable(false);

		// ==== 고객 목록 TEXT AREA ====
		JScrollPane panelResult = new JScrollPane(txtResult);

		// ==== 하단 인원수 체크 ====
		JPanel panel4 = new JPanel();
		

		panel4.add(gogekCount);

		add("North", panel);
		add("Center", panelResult);
		add("South", btnPanel);
		add("West", gogekCount);
		
		btnFir.addActionListener(this);
		btnPre.addActionListener(this);
		btnNext.addActionListener(this);
		btnLast.addActionListener(this);
	}

	// ==== ACCESS DB 메소드 ====
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");

			stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY); // 레코드 포인터 이동 순
																										// / 역 방향 가능
			rs = stmt.executeQuery(
					"select jikwon_no, jikwon_name, buser_name, buser_tel from jikwon LEFT OUTER JOIN buser ON buser_num = buser_no");

			rs.next();

			displayData();

		} catch (Exception e) {
//			System.out.println("accDb err : " + e);
		}

	}

	private void displayData() {
		try {
			txtNo.setText(rs.getString("jikwon_no"));
			txtName.setText(rs.getString("jikwon_name"));
			txtBuserName.setText(rs.getString("buser_name"));
			txtBuserTel.setText(rs.getString("buser_tel"));
			
			String jikNum = txtNo.getText();
			String sql = "select gogek_no, gogek_name, gogek_tel from gogek join jikwon on gogek_damsano = jikwon_no "
						+ "where jikwon_no = '" + jikNum + "'";
			
			txtResult.setText("고객 번호\t고객이름\t고객전화번호\n");
			rs2 = stmt.executeQuery(sql);
			
			int count = 0;
			
			while (rs2.next()) {
				String ss = rs2.getString("gogek_no") + "\t" + rs2.getString("gogek_name") + "\t"
						+ rs2.getString("gogek_tel") + "\n";

				txtResult.append(ss);
				count++;
			}

			gogekCount.setText("인원수 : " + count + "명\t");
			
		} catch (Exception e2) {
			System.out.println("displayData err : " + e2);
			JOptionPane.showMessageDialog(this, "자료의 처음 또는 마지막");
		}

	}

	// ============= ACTION PERFORM 메소드 ==========
	@Override
	public void actionPerformed(ActionEvent e) {

		// ==== 버튼 기능 =====
		try {
			if (e.getSource() == btnFir)
				rs.first();

			else if (e.getSource() == btnPre) {
				rs.previous();
			}

			else if (e.getSource() == btnNext) {
				rs.next();

			} else if (e.getSource() == btnLast)
				rs.last();

			displayData();
		} catch (Exception e3) {
			// TODO: handle exception
		}

	}

	public static void main(String[] args) {
		new DBTest5Ex();

	}
}
