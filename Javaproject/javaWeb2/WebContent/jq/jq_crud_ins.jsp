
<%@ page language="java" contentType="text/plain; charset=UTF-8"
	pageEncoding="UTF-8" import="java.sql.*"%>

<%
	request.setCharacterEncoding("utf-8");
	String code = request.getParameter("code");
	String sang = request.getParameter("sang");
	String su = request.getParameter("su");
	String dan = request.getParameter("dan");
	
	// System.out.println(code + " " + sang + " " + su + " " + dan);
	
	Connection conn = null;
	PreparedStatement pstmt = null;
	
	try{
		Class.forName("org.mariadb.jdbc.Driver");
		
		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
		pstmt = conn.prepareStatement("insert into sangdata values(?,?,?,?)");
		pstmt.setString(1, code);
		pstmt.setString(2, sang);
		pstmt.setString(3, su);
		pstmt.setString(4, dan);
		int re = pstmt.executeUpdate();
		
		if(re == 1)
			out.print("t");
		else
			out.print("f");
			
		
	} catch(Exception e){
		System.out.print("err : " +e);
	}finally{
		pstmt.close();
		conn.close();
	}
%>
