<%@ page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/plain; charset=UTF-8"
	pageEncoding="UTF-8" import="java.sql.*"%>

<%
	Connection conn = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;

	try {
		Class.forName("org.mariadb.jdbc.Driver");
	} catch (Exception e) {
		System.out.println("loading err : " + e);
		return;
	}

	try {
		request.setCharacterEncoding("utf-8");
		String keyword = request.getParameter("keyword");
		System.out.println(keyword);

		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
		pstmt = conn.prepareStatement("select jikwon_name from jikwon where jikwon_name like ?");
		pstmt.setString(1, keyword + "%");
		rs = pstmt.executeQuery();

		ArrayList<String> list = new ArrayList();
		while (rs.next()) {
			list.add(rs.getString(1));
			System.out.println(rs.getString(1));
		}
		out.print(list.size());
		out.print("|");
		for(int i = 0; i < list.size(); i++){
			String data = list.get(i);
			out.print(data);
			if(i <list.size() -1){
				out.print(",");
			}
		}

		rs.close();
		pstmt.close();
		conn.close();
	} catch (Exception e) {
		System.out.println("err : " + e);
		return;
	}
%>
