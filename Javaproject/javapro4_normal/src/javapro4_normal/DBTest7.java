package javapro4_normal;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBTest7 {

	private Connection conn; // DB연결
	private PreparedStatement pstmt; // 선처리 방식으로 SQL 실행
	private ResultSet rs; // select 결과 접근

	public DBTest7() {
		// Drivate Loading 방법 1.
		// Driver File을 구해서 프로젝트에 build path
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("드라이버 로딩 실패 : " + e);
		}

		try {
			// 자료 추가
			
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
		} catch (Exception e) {
			System.out.println("연결 실패 : " + e);
		}

		try {
			// 자료 추가
//			String insSql = "insert into sangdata values(6,'aa',5, 1000)";
			
			/*
			String insSql = "insert into sangdata values(?,?,?,?)"; //prepareStatement의 강점. ?을 쓸 수 있음
			pstmt = conn.prepareStatement(insSql);
			pstmt.setString(1, "7");
			pstmt.setString(2, "아메리카노");
			pstmt.setInt(3, 10);
			pstmt.setInt(4, 5000);
			pstmt.executeUpdate();
			*/
			
			
			//자료 수정
			/*
			String upSql = "update sangdata set sang=?, su=? where code = ?";
			pstmt = conn.prepareStatement(upSql);
			pstmt.setString(1, "삼다수");
			pstmt.setString(2, "100");
			pstmt.setString(3, "6");
			*/
			
			//자료 삭제
			/*
			String delSql ="delete from sangdata where code = ?";
			pstmt = conn.prepareStatement(delSql);
			pstmt.setString(1, "7");
			*/
			
			int re = pstmt.executeUpdate();
			if (re == 1)
				System.out.println("추가 성공");
			else
				System.out.println("추가 실패");

			String sql = "select code, sang, su, dan from sangdata";
			pstmt = conn.prepareStatement(sql);

			rs = pstmt.executeQuery();
			while (rs.next()) {
				String code = rs.getString("code");
				String sangpum = rs.getString(2);
				int su = rs.getInt("su");
				String danga = rs.getString("dan");
				System.out.println(code + " " + sangpum + " " + su + " " + danga);

			}

			sql = "select count(*) from sangdata";
			rs = pstmt.executeQuery(sql);
			if (rs.next()) {
				System.out.println("건수 : " + rs.getInt(1));
			}

		} catch (Exception e) {
			System.out.println("처리실패: " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {
				// TODO: handle exception
			}
		}

	}

	public static void main(String[] args) {
		new DBTest7();
	}
}
