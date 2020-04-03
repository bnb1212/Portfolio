package pack.order;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

import pack.product.ProductDto;

public class OrderMgr {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	private DataSource ds;

	public OrderMgr() {
		try {
			Context context = new InitialContext();
			ds = (DataSource) context.lookup("java:comp/env/jdbc_maria");
		} catch (Exception e) {
			System.out.println("OrderMgr Constructor err : " + e);
		}
	}

	public void insertOrder(OrderBean order) {
		try {
			conn = ds.getConnection();
			String sql = "insert into shop_order (product_no, quantity, sdate, state, id) values (?, ?, now(), ?, ?)";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, order.getProduct_no());
			pstmt.setString(2, order.getQuantity());
			pstmt.setString(3, "1");
			pstmt.setString(4, order.getId());
			pstmt.executeUpdate();

		} catch (Exception e) {
			System.out.println("insertOrder err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {

			}
		}

	}

	public ArrayList<OrderDto> getOrder(String id) {
		ArrayList<OrderDto> list = new ArrayList<OrderDto>();
		try {
			conn = ds.getConnection();
			String sql = "select * from shop_order where id=? order by no desc";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, id);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				OrderDto dto = new OrderDto();
				dto.setNo(rs.getString("no"));
				dto.setProduct_no(rs.getString("product_no"));
				dto.setQuantity(rs.getString("quantity"));
				dto.setSdate(rs.getString("sdate"));
				dto.setState(rs.getString("state"));
				dto.setId(rs.getString("id"));
				list.add(dto);

			}
		} catch (Exception e) {
			System.out.println("getOrder err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {

			}
		}
		return list;
	}

	public ArrayList<OrderDto> getOrderAll() {
		ArrayList<OrderDto> list = new ArrayList<OrderDto>();
		try {
			conn = ds.getConnection();
			String sql = "select * from shop_order order by no desc";

			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			while (rs.next()) {
				OrderDto dto = new OrderDto();
				dto.setNo(rs.getString("no"));
				dto.setProduct_no(rs.getString("product_no"));
				dto.setQuantity(rs.getString("quantity"));
				dto.setSdate(rs.getString("sdate"));
				dto.setState(rs.getString("state"));
				dto.setId(rs.getString("id"));
				list.add(dto);

			}
		} catch (Exception e) {
			System.out.println("getOrder errAll : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {

			}
		}
		return list;
	}

	public OrderDto getOrderDetail(String no) {
		OrderDto dto = null;
		try {
			conn = ds.getConnection();
			String sql = "select * from shop_order where no=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, no);
			rs = pstmt.executeQuery();
			if (rs.next()) {
				dto = new OrderDto();
				dto.setNo(rs.getString("no"));
				dto.setProduct_no(rs.getString("product_no"));
				dto.setQuantity(rs.getString("quantity"));
				dto.setSdate(rs.getString("sdate"));
				dto.setState(rs.getString("state"));
				dto.setId(rs.getString("id"));
			}
		} catch (

		Exception e) {
			System.out.println("getOrderDetail errAll : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {

			}
		}
		return dto;
	}

	public boolean updateOrder(String no, String state) {
		boolean b = false;
		try {
			conn = ds.getConnection();
			String sql = "update shop_order set state=? where no=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, state);
			pstmt.setString(2, no);
			if (pstmt.executeUpdate() > 0) {
				b = true;
			}
		} catch (Exception e) {
			System.out.println("updateOrder err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {

			}
		}
		return b;
	}

	public boolean deleteOrder(String no) {
		boolean b = false;
		try {
			conn = ds.getConnection();
			String sql = "delete from shop_order where no=?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, no);
			if (pstmt.executeUpdate() > 0) {
				b = true;
			}
		} catch (Exception e) {
			System.out.println("deleteOrder err : " + e);
		} finally {
			try {
				if (rs != null)
					rs.close();
				if (pstmt != null)
					pstmt.close();
				if (conn != null)
					conn.close();
			} catch (Exception e) {
				
			}
		}
		return b;
	}
}
