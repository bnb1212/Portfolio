<%@ page language="java" contentType="text/plain; charset=UTF-8"
	pageEncoding="UTF-8" import="java.sql.*"%>

<%
	request.setCharacterEncoding("utf-8");
	String dcode = request.getParameter("dcode");
	
	// System.out.println(code + " " + sang + " " + su + " " + dan);
	
	Connection conn = null;
	PreparedStatement pstmt = null;
	
	try{
		Class.forName("org.mariadb.jdbc.Driver");
		
		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
		pstmt = conn.prepareStatement("delete from sangdata where code=?");
		pstmt.setString(1, dcode);;
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
