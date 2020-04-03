package javapro4_normal;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

public class DBTest2 {

	private Connection conn;
	private Statement stmt;
	private ResultSet rs;
	private Properties properties = new Properties();
	
	public DBTest2() { // Secure coding - 연결 정보를 별도 파일로 작성 후 읽기
		String sql = "";
		
		try {
			properties.load(new FileInputStream("C:\\work\\jsou\\javapro4_normal\\src\\javapro4_normal\\userpass.properties"));
			//System.out.println(properties.getProperty("driver"));
			
			Class.forName(properties.getProperty("driver"));
			conn = DriverManager.getConnection(properties.getProperty("url"),
					properties.getProperty("user"),
					properties.getProperty("passwd"));
			
			stmt = conn.createStatement();
			
			// 자료 추가 -- auto commit
//			sql = "inset into sangdata values(5, '새우깡', 5, '1000')";
//			stmt.executeUpdate(sql);
			
//			-----transaction -----------------------
			/*
			conn.setAutoCommit(false);
			sql = "insert into sangdata values(6, '감자깡', 15, '1200')";
			stmt.executeUpdate(sql);
			// ...
//			conn.rollback();
			conn.commit();
			conn.setAutoCommit(true);
			*/
			// --------------------------
			// 자료 수정
			sql = "update sangdata set sang='가죽점퍼', dan=1300 where code=4";
			int re = stmt.executeUpdate(sql);
			if(re>0)
				System.out.println("수정 성공");
			else
				System.out.println("수정실패");
			
			// 자료 삭제
			sql = "delete from sangdata where code=6";
			int re2 = stmt.executeUpdate(sql);
			if(re2>0)
				System.out.println("삭제 성공");
			else
				System.out.println("삭제 실패");
			
			// 모든 자료 읽기
			sql = "select * from sangdata order by code";
			
			int cou = 0;
			rs = stmt.executeQuery(sql);
			while(rs.next()) {
				System.out.println(rs.getString("code") + " " +
									rs.getString("sang")+" " +
									rs.getString("su") + " " +
									rs.getString("dan"));
			}
			
		} catch (Exception e) {
			System.out.println("err : " + e);
		}
	}
	public static void main(String[] args) {
		new DBTest2();
	}
}
