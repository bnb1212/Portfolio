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
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class DBTest5RecMove extends JFrame implements ActionListener {

	JButton btnFir, btnPre, btnNext, btnLast;
	JTextField txtNo, txtName;
	JTextArea txtResult = new JTextArea();

	Connection conn;
	Statement stmt;
	ResultSet rs;

	public DBTest5RecMove() {
		layInit();
		accDb();

		setTitle("레코드 이동");

		setBounds(200, 200, 400, 300);
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

	private void layInit() {
		txtNo = new JTextField("", 5);
		txtName = new JTextField("", 10);

		JPanel panel1 = new JPanel();
		panel1.add(new JLabel("직원 자료 : "));
		panel1.add(txtNo);
		panel1.add(txtName);
		add("North", panel1);

		txtNo.setEditable(false);
		txtName.setEditable(false);

		btnFir = new JButton("|<<");
		btnPre = new JButton("<");
		btnNext = new JButton(">");
		btnLast = new JButton(">>|");

		JPanel panel2 = new JPanel();
		panel2.add(btnFir);
		panel2.add(btnPre);
		panel2.add(btnNext);
		panel2.add(btnLast);
		add("Center", panel2);

		btnFir.addActionListener(this);
		btnPre.addActionListener(this);
		btnNext.addActionListener(this);
		btnLast.addActionListener(this);
	}

	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");

			stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY); // 레코드 포인터 이동 순
																										// / 역 방향 가능

			rs = stmt.executeQuery("select jikwon_no, jikwon_name from jikwon");

			rs.next();

			displayData();
		} catch (Exception e) {
			System.out.println("accDb err : " + e);
		}
	}

	private void displayData() {
		try {
			txtNo.setText(rs.getString("jikwon_no"));
			txtName.setText(rs.getString("jikwon_name"));

		} catch (Exception e) {
//			System.out.println("displayData err : "  + e);
			JOptionPane.showMessageDialog(this, "자료의 처음 또는 마지막");
		}

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			String jikwonNo = txtNo.getText();
			
			if (e.getSource() == btnFir)
				rs.first();
			else if (e.getSource() == btnPre)
				rs.previous();
				
			else if (e.getSource() == btnNext)
				rs.next();
			else if (e.getSource() == btnLast)
				rs.last();

			displayData();
		} catch (Exception e3) {
			// TODO: handle exception
		}

	}
	
	
	public static void main(String[] args) {
		new DBTest5RecMove();
	}
}
