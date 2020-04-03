package javapro4_normal;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.math.BigDecimal;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.text.DecimalFormat;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

public class DBTest9Ex extends JFrame implements ActionListener {
	private JButton btnOut, btnExit;
	private String[][] datas = new String[0][6];
	private String[] title = { "사번", "이름", "성별", "연봉", "세금", "실수령액" };
	private DefaultTableModel model;
	private JTable table;

	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;

	// ==== CONSTRUCTOR ====
	public DBTest9Ex() {
		super("세금 계산기");
		
		new DBTest9ExLogin(this);
		layInit();
		accDb();

		setBounds(300, 300, 500, 300);
		setVisible(true);
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				try {
					if (rs != null)
						rs.close();
					if (pstmt != null)
						pstmt.close();
					if (conn != null)
						conn.close();
				} catch (Exception e3) {
				}
				System.exit(0);
			}
		});
	}

	// ==== Layout init ====
	private void layInit() {
		JPanel panel = new JPanel();
		btnOut = new JButton("출력");
		btnExit = new JButton("종료");

		btnOut.addActionListener(this);
		btnExit.addActionListener(this);

		panel.add(btnOut);
		panel.add(btnExit);
		add("North", panel);

		model = new DefaultTableModel(datas, title);
		table = new JTable(model);
		JScrollPane scrollPane = new JScrollPane(table);

		add("Center", scrollPane);
	}

	// ==== Access Db ====
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("accDb err : " + e);
		}
	}

	// ========= 기능 구현 ( ACTION LISTENER ) =======
	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == btnOut) {
			try {
				model.setRowCount(0);
				
				conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
				pstmt = conn.prepareStatement("select * from jikwon");
				rs = pstmt.executeQuery();

				while (rs.next()) {
					String jikNo = rs.getString("jikwon_no");
					String jikName = rs.getString("jikwon_name");
					String jikGen = rs.getString("jikwon_gen");
					Double jikPay = rs.getDouble("jikwon_pay") * 10000;
					Double jikTax;
					if (jikPay >= 50000000)
						jikTax = jikPay * 0.03;
					else
						jikTax = jikPay * 0.02;
					
					BigDecimal bigJikPay = new BigDecimal(jikPay);
					BigDecimal realMoney = new BigDecimal(jikPay-jikTax);
					DecimalFormat Comma = new DecimalFormat("###,###");
					
					String[] imsi = { jikNo, jikName, jikGen, bigJikPay.toString(), Double.toString(jikTax),
							Comma.format(realMoney) };
					model.addRow(imsi);
				}
			} catch (Exception e2) {
				System.out.println(e2);
			}
		}
		if (e.getSource() == btnExit) {
			System.exit(0);
		}

	}

	public static void main(String[] args) {
		new DBTest9Ex();
	}
}
