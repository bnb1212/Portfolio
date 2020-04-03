package pack;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

public class ConnBean {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;

	public ConnBean() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("DB connect Failed : " + e);
		}

	}

	public ArrayList<SangpumDto> getDataAll() {
		ArrayList<SangpumDto> list = new ArrayList<SangpumDto>();
		try {
			String sql = "select * from sangdata";
			
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
			pstmt = conn.prepareStatement(sql);

			rs = pstmt.executeQuery();
			while (rs.next()) {
				SangpumDto dto = new SangpumDto();
				dto.setCode(rs.getString(1));
				dto.setSang(rs.getString(2));
				dto.setSu(rs.getString(3));
				dto.setDan(rs.getString(4));
				list.add(dto);
			}

		} catch (Exception e) {
			System.out.println("getDataAll err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e2) {

			}
		}
		return list;

	}
}
