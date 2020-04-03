package javapro4_normal;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class DbQuiz extends JFrame implements ActionListener {

	JButton searchBtn = new JButton("확인");
	ButtonGroup group = new ButtonGroup();
	JRadioButton asc = new JRadioButton("오름");
	JRadioButton desc = new JRadioButton("내림");
	JTextArea txtResult = new JTextArea();
	JLabel jikCount, payAvg;
	JTextField searchBox;
	String sqlSave = "";
	
	Connection conn;
	Statement stmt;
	ResultSet rs;

	public DbQuiz() {
		super("직급 정보");
		setLayout();
		accessDb();
		setBounds(300, 300, 400, 400);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

	public void setLayout() {
		JPanel panel = new JPanel();
		JLabel jik = new JLabel("직급 : ");
		searchBox = new JTextField("", 10);
		group.add(asc);
		group.add(desc);

		panel.add(jik);
		panel.add(searchBox);
		panel.add(searchBtn);
		panel.add(asc);
		panel.add(desc);

		txtResult.setEditable(false);
		JScrollPane panel2 = new JScrollPane(txtResult);

		JPanel panel3 = new JPanel();
		jikCount = new JLabel("인원수 : 0명\t");
		payAvg = new JLabel("연봉평균 : 0");

		panel3.add(jikCount);
		panel3.add(payAvg);

		add("North", panel);
		add("Center", panel2);
		add("South", panel3);

		asc.setSelected(true);

		searchBtn.addActionListener(this);
		asc.addActionListener(this);
		desc.addActionListener(this);
	}

	private void accessDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("accessDb err : " + e);
		}

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			stmt = conn.createStatement();

			String sql = "select jikwon_no, jikwon_name, jikwon_jik, jikwon_gen, buser_name from jikwon left outer join buser on buser_num = buser_no";
			
			
			int payAvgInt = 0;

			// 확인 버튼
			if (e.getSource() == searchBtn) {
				String searchTxt = searchBox.getText();

				if (searchTxt.equals("") == false)
					sql += " where jikwon_jik = " + "\'" + searchTxt + "\'";
					sqlSave = sql;
					
				if (desc.isSelected())
					sql += " order by jikwon_no desc";
					sqlSave = sql;
					
				rs = stmt.executeQuery(sql);
				System.out.println(sql);
				int count = 0;

				txtResult.setText("사번\t직원명\t직급\t성별\t부서명\n");
				while (rs.next()) {
					String ss = rs.getString("jikwon_no") + "\t" + rs.getString("jikwon_name") + "\t"
							+ rs.getString("jikwon_jik") + "\t" + rs.getString("jikwon_gen") + "\t"
							+ rs.getString("buser_name") + "\n";

					txtResult.append(ss);
					count++;
				}

				if (searchTxt.equals("") == false) {
					sql = "select avg(jikwon_pay) from jikwon where jikwon_jik = \'" + searchTxt + "\'";
					rs = stmt.executeQuery(sql);
					rs.next();
					payAvgInt = (int) rs.getDouble("avg(jikwon_pay)");
				} else {
					sql = "select avg(jikwon_pay) from jikwon";
					rs = stmt.executeQuery(sql);
					rs.next();
					payAvgInt = (int) rs.getDouble("avg(jikwon_pay)");
				}
				jikCount.setText("인원수 : " + count + "명\t");
				payAvg.setText("연봉평균 : " + payAvgInt);

			}

		} catch (Exception err) {
			System.out.println(err);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (stmt != null)
					stmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e3) {
				// TODO: handle exception
			}
		}

	}

	public static void main(String[] args) {
		new DbQuiz();
	}
}
