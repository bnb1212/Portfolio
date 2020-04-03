package javapro4_normal;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DBTest1 {

	private Connection conn; // DB연결
	private Statement stmt; // SQL 실행
	private ResultSet rs; // select 결과 접근

	public DBTest1() {
		// Drivate Loading 방법 1.
		// Driver File을 구해서 프로젝트에 build path
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("드라이버 로딩 실패 : " + e);
		}

		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
		} catch (Exception e) {
			System.out.println("연결 실패 : " + e);
		}

		try {
			stmt = conn.createStatement();

			/*
			 * rs = stmt.executeQuery("select * from sangdata"); rs.next();
			 * System.out.println(rs.getString("code") + " " + rs.getString("sang") + " " +
			 * rs.getInt("su") + " " + rs.getInt("dan"));
			 */

			/*
			 * rs = stmt.
			 * executeQuery("select code as 코드, sang as 품명, su as 수량, dan as 단가  from sangdata;"
			 * ); rs.next(); System.out.println(rs.getString("코드") + " " +
			 * rs.getString("sang") + " " + rs.getInt("su") + " " + rs.getInt("dan"));
			 */

			rs = stmt.executeQuery("select code, sang, su, dan from sangdata");
			while (rs.next()) {
				String code = rs.getString("code");
				String sangpum = rs.getString(2);
				int su = rs.getInt("su");
				String danga = rs.getString("dan");
				System.out.println(code + " " + sangpum + " " + su + " " + danga);

			}

			String sql = "select count(*) from sangdata";
			rs = stmt.executeQuery(sql);
			if (rs.next()) {
				System.out.println("건수 : " + rs.getInt(1));
			}

		} catch (Exception e) {
			System.out.println("처리실패: " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (stmt != null)
					stmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {
				// TODO: handle exception
			}
		}

	}

	public static void main(String[] args) {
		new DBTest1();
	}
}
