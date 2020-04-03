package javapro4_normal;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DBTest6Execute {

	private Connection conn;
	private Statement stmt;
	private ResultSet rs;

	public DBTest6Execute() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			process();

		} catch (Exception e) {
			System.out.println("드라이버 로딩 실패 : " + e);
		} finally {
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
		}
	}

	private void process() {
		try {
			stmt = conn.createStatement();

			boolean b = false;

			b = stmt.execute("update sangdata set sang='종이컵' where code=5");
			System.out.println("update 실행 후 b : " + b);
			int re = stmt.getUpdateCount(); // insert, update, delete 수행 후 결과 수를 반환
			
			if (re >= 1) {
				
			}
			
			stmt.execute("select * from sangdata");
			System.out.println("select 수행 후 b : " + b);
			if (b) {
				rs = stmt.getResultSet();

				while (rs.next()) {
					System.out.println(rs.getString(1) + " " + rs.getString(2));
				}
			}

		} catch (Exception e) {
			System.out.println("process err : " + e);
		}
	}

	public static void main(String[] args) {
		new DBTest6Execute();

	}
}
