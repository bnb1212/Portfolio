package javapro4_normal;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.WindowConstants;

public class DBTest8Login extends JFrame implements ActionListener {

	JTextField txtNo, txtName;
	JButton btnLogin;
	JTextArea txtResult;

	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;

	public DBTest8Login() {
		setTitle("Login");

		layInit();
		accDb();
		setBounds(300, 300, 400, 300);
		setVisible(true);

		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				// ...
				System.exit(0);
			}
		});
	}

	private void layInit() {
		JPanel panel = new JPanel();
		txtResult = new JTextArea();
		JScrollPane spane = new JScrollPane(txtResult);
		txtNo = new JTextField("", 5);
		txtName = new JTextField("", 10);
		btnLogin = new JButton("로그인");

		panel.add(new JLabel("사번 : "));
		panel.add(txtNo);
		panel.add(new JLabel("직원명 : "));
		panel.add(txtName);
		panel.add(btnLogin);

		add("North", panel);
		add("Center", spane);
		
		btnLogin.addActionListener(this);

	}

	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
				} catch (Exception e) {
			System.out.println("accDb err : " + e);
		}
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (txtNo.getText().equals("") || txtName.getText().equals("")) {
			JOptionPane.showMessageDialog(this, "로그인 자료 입력");
			return;
		}

		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			String sql = "select * from jikwon where jikwon_no = ? and jikwon_name=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, txtNo.getText());
			pstmt.setString(2, txtName.getText());
			rs = pstmt.executeQuery();

			if (rs.next()) {
//				txtResult.setText("로그인");
				sql = "select jikwon_no, jikwon_name, jikwon_pay, jikwon_jik from jikwon";
				pstmt = conn.prepareStatement(sql);
				rs = pstmt.executeQuery();
				txtResult.setText("사번\t직원명\t연봉\t직급\n");

				while (rs.next()) {
					String bun = rs.getString(1);
					String irum = rs.getString(2);
					String pay = rs.getString(3);
					String jik = rs.getString(4);
					txtResult.append(bun + "\t" + irum + "\t" + pay + "\t" + jik + "\n");
				}
			} else {
				txtResult.setText("로그인 실패");
			}

		} catch (

		Exception e2) {
			System.out.println("actionPerformed err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e3) {
				// TODO: handle exception
			}
		}
	}

	public static void main(String[] args) {
		new DBTest8Login();
	}
}
