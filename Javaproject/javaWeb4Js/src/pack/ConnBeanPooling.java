package pack;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class ConnBeanPooling {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	private DataSource ds;

	public ConnBeanPooling() {
		try {
			Context context = new InitialContext(); // DBCP지원
			ds = (DataSource) context.lookup("java:comp/env/jdbc_maria");

		} catch (Exception e) {
			System.out.println("DB connect Failed : " + e);
		}

	}

	public ArrayList<SangpumDto> getDataAll() {
		ArrayList<SangpumDto> list = new ArrayList<SangpumDto>();
		try {
			String sql = "select * from sangdata";

			conn = ds.getConnection();
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

	public boolean insertData(SangpumBean bean) {
		boolean b = false;
		try {
			// 새상품 구하기
			String sql = "select max(code) as max from sangdata";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			int newCode = 0;
			if (rs.next()) {
				newCode = rs.getInt("max");
				;
			}
			newCode++;

			pstmt.close();
			sql = "insert into sangdata values(?, ?, ? ,?)";
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, newCode);
			pstmt.setString(2, bean.getSang());
			pstmt.setString(3, bean.getSu());
			pstmt.setString(4, bean.getDan());
			int re = pstmt.executeUpdate();
			if (re == 1)
				b = true;

		} catch (Exception e) {
			System.out.println("insertData err  " + e);
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
		return b;
	}

	public SangpumDto updateList(String code) {
		SangpumDto dto = null;
		try {
			String sql = "select * from sangdata where code=?";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, code);
			rs = pstmt.executeQuery();
			if (rs.next()) {
				dto = new SangpumDto();
				dto.setCode(rs.getString(1));
				dto.setSang(rs.getString(2));
				dto.setSu(rs.getString(3));
				dto.setDan(rs.getString(4));
			}
			System.out.println(dto.getCode());
		} catch (Exception e) {
			System.out.println("updateData err  " + e);
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
		return dto;
	}
	
	public boolean updateData(SangpumBean bean) {
		boolean b = false;
		try {
			conn = ds.getConnection();
			String sql = "update sangdata set sang=?, su=?, dan=? where code=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, bean.getSang());
			pstmt.setString(2, bean.getSu());
			pstmt.setString(3, bean.getDan());
			pstmt.setString(4, bean.getCode());
			if(pstmt.executeUpdate() > 0)
				b = true;
			
			
		} catch (Exception e) {
			System.out.println("updateData err  " + e);
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
		return b;
	}
	
	public boolean deleteData(String code) {
		boolean b = false;
		try {
			conn = ds.getConnection();
			String sql = "delete from sangdata where code=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, code);
			if(pstmt.executeUpdate() > 0)
				b = true;
			
			
		} catch (Exception e) {
			System.out.println("updateData err  " + e);
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
		return b;
	}
}
