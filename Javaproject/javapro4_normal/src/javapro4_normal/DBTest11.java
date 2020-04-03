package javapro4_normal;

import java.awt.GridLayout;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextArea;
import javax.swing.table.DefaultTableModel;

public class DBTest11 extends JFrame {
	Connection conn;
	PreparedStatement pstmt1, pstmt2, pstmt3;
	ResultSet rs1, rs2, rs3;
	
	String datas[][] = new String[0][4];
	String[] title = {"부서번호", "부서명", "부서전화", "부서위치"};
	String sql;
	String buserName;
	DefaultTableModel model;
	JTextArea txtResult;
	JTable table;
	
	public DBTest11() {
		super("부서별 직원정보");
		
		layInit();
		
		setBounds(300, 300, 400, 400);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	
		accDb();
		showData();
	
		table.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				table = (JTable)e.getComponent();
				model = (DefaultTableModel)table.getModel();
//				System.out.println("행/열번호 : " +
//						table.getSelectedRow() + " / " + table.getSelectedColumn());
//				System.out.println("열이름 : " + table.getColumnName(table.getSelectedColumn()));
//				System.out.println("값 : " + model.getValueAt(table.getSelectedRow(), table.getSelectedColumn()));
				System.out.println("값 : " + model.getValueAt(table.getSelectedRow(),	 1));
			
				buserName = (String)model.getValueAt(table.getSelectedRow(), 1);
				
				showResult();
				
			}
		});
	}
	
	public void layInit() {
		setLayout(new GridLayout(2,1));
		model = new DefaultTableModel(datas, title);
		table = new JTable(model);
		JScrollPane pane = new JScrollPane(table);
		
		txtResult = new JTextArea();
		JScrollPane pane2 = new JScrollPane(txtResult);
		
		add("North", pane);
		add("South", pane2);
		
	}
	
	public void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception accErr) {
			System.out.println("accessDb err : " + accErr);
			return;
		}

	}
	
	public void showData() {
		sql = "select * from buser";
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			pstmt1 = conn.prepareStatement(sql);
			rs1 = pstmt1.executeQuery();
			while(rs1.next()) {
				String[] data = 
					{rs1.getString(1), rs1.getString(2), rs1.getString(3), rs1.getString(4)};
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
	
	public void showResult() {
		txtResult.setText("");
		
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			String sql2 = "select jikwon_no, jikwon_name, jikwon_jik from"
					+ " jikwon right outer join buser"
					+ " on buser_num = buser_no where buser_name=?";
			pstmt2 = conn.prepareStatement(sql2);
			pstmt2.setString(1, buserName);
			rs2 = pstmt2.executeQuery();
			
			while(rs2.next()) {
				String ss = rs2.getString(1) + "\t" 
						+ rs2.getString(2) + "\t" 
						+ rs2.getString(3) + "\n";
				txtResult.append(ss);
			}
			
			
		} catch (Exception shResultErr) {
			System.out.println("결과출력 에러 : " + shResultErr);
		}finally {
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
	
	public static void main(String[] args) {
		new DBTest11();
	}
	
}
