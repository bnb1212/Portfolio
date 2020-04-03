package pack2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DbEx {
	private Connection conn = null;
	private PreparedStatement pstmt = null;
	private ResultSet rs = null;

	public DbEx() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");

			conn = DriverManager.getConnection("jdbc:mariadb://192.168.0.77:3306/test", "root", "123");
			pstmt = conn.prepareStatement("select * from aa");
			rs = pstmt.executeQuery();
			
			/*
			 * rs.next(); System.out.println(rs.getInt("bun") + " " + rs.getString("irum") +
			 * " " + rs.getString("juso"));
			 */
			
			while (rs.next()) {
				System.out.println(rs.getInt("bun") + " " + rs.getString("irum") + " " + rs.getString("juso"));
			}
		} catch (Exception e) {
			System.out.println("err" + e);

		} finally {
			try {
				rs.close();
				pstmt.close();
				conn.close();
			} catch (Exception e) {

			}

		}
	}

	public static void main(String[] args) {
		new DbEx();
	}
}
