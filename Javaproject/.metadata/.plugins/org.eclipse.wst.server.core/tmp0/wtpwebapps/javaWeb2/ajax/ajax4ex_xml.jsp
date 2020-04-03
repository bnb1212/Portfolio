<?xml version="1.0" encoding="UTF-8"?>

<%@ page language="java" contentType="text/xml; charset=UTF-8"
	pageEncoding="UTF-8" import="java.sql.*"%>
  
<jikwons> <%
	Connection conn = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;

	request.setCharacterEncoding("utf-8");
	String gender = request.getParameter("gen");
	System.out.println(gender);
	
 	try {
 		Class.forName("org.mariadb.jdbc.Driver");
 	} catch (Exception e) {
 		System.out.println("loading err : " + e);
 		return;
 	}

 	try {
 		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");		
 		String sql = "select * from jikwon";
 		
 		if (gender.equals("all")){
 		pstmt = conn.prepareStatement(sql);
 		} else if(gender.equals("male")){
 			sql += " where jikwon_gen = \"남\"";
 			pstmt = conn.prepareStatement(sql);
 		} else if(gender.equals("female")){
 			sql += " where jikwon_gen = \"여\"";
 			pstmt = conn.prepareStatement(sql);
 		}
 		
 		pstmt = conn.prepareStatement(sql);
 		rs = pstmt.executeQuery();

 		while (rs.next()) {
%>
 		<jikwon>
 			 <jiknum><%out.print(rs.getString("jikwon_no"));%></jiknum>
 			 <jikname><%=rs.getString("jikwon_name") %></jikname>
 			 <jikjik><%=rs.getString("jikwon_jik") %></jikjik>
 			 <jikgen><%=rs.getString("jikwon_gen") %></jikgen>
	    </jikwon>
<%
 	}
 	} catch (Exception e) {
 		System.out.println("err2 : " + e);
 		return;
 	}
%> 
</jikwons>