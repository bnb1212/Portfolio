package javapro4_normal;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;



public class GukgaLogin extends JDialog implements ActionListener{
	
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	
	JLabel lblNo, lblName;
	JTextField txtNo, txtName;
	JButton btnLogin;
	
	int count =0;
	
	
	public GukgaLogin() {
		
		setModal(true); // 모달형 다이얼로그 생성
		setTitle("Login");
		Layinit_Login();
		accDB_Login();
		setBounds(300, 300, 300, 180);

		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {

				System.exit(0);
			}
		});
		
	}
	
	
	private void Layinit_Login() {
		JPanel pn0 = new JPanel();
		pn0.setLayout(new BorderLayout());
		JPanel pn1 = new JPanel();
		JLabel lbllogin = new JLabel("로그인");
		pn1.add(lbllogin);
		add("North", pn1);
		JPanel pn2 = new JPanel();
		txtNo = new JTextField("", 5);
		txtName = new JTextField("", 10);
		btnLogin = new JButton("로그인");
		pn2.add(new JLabel("회원번호: "));
		pn2.add(txtNo);

		JPanel pn3 = new JPanel();
		pn3.add(new JLabel("회원이름: "));
		pn3.add(txtName);

		pn0.add("North", pn2);
		pn0.add("South", pn3);
		add("Center", pn0);

		JPanel pn4 = new JPanel();
		pn4.add(btnLogin);
		btnLogin.addActionListener(this);

		add("South", pn4);
	}

	private void accDB_Login() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");

		} catch (Exception e) {
			System.out.println("acc db 에러" + e.getMessage());
			// TODO: handle exception
		}
	}
	

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == btnLogin) {
			if (txtNo.getText().equals("") || txtName.getText().equals("")) {
				JOptionPane.showMessageDialog(this, "정확히 정보를 입력하세요");
				return;
			}

			try {
				conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
				String sql = "select * from loginpeople where login_No=? and login_Name=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1, txtNo.getText());
				pstmt.setString(2, txtName.getText());
				rs = pstmt.executeQuery();
				if (rs.next()) { // sql문이 실행되면 로그인 허용으로 간주
					dispose();
				} else {

					if (count <= 1) {
						JOptionPane.showMessageDialog(this, "다시입력해주세요");
						++count; // 억지로 세번 맞추기....
					} else {
						System.exit(0); // 3번 틀리면 exit
					}
				}

			}

			catch (Exception e2) {
				System.out.println("Action performed 에러");
			}

			finally {
				try {
					if (rs != null)
						rs.close();
					if (pstmt != null)
						pstmt.close();
					if (conn != null)
						conn.close();
				}

				catch (Exception e2) {
				}
			}

		}
	
		
	}

}
