<%@page import="java.sql.*" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	Connection conn = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;

	try {
		Class.forName("org.mariadb.jdbc.Driver");
		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
		pstmt = conn.prepareStatement("select * from sangdata");

		
	} catch (Exception e) {
		System.out.println("init err : " + e);
	}
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>* 상품자료 (jsp:Beans X)</h2>
	<h3>바로 회사 짤리는 각 ( ._. )</h3>
	<table border="1">
		<tr>
			<th>code</th>
			<th>sang</th>
			<th>su</th>
			<th>dan</th>
		</tr>
		<%
			try {
				rs = pstmt.executeQuery();
				while (rs.next()) {
		%>
		<tr>
			<td>
				<%
					out.println(rs.getString("code"));
				%>
			</td>
			<td><%=rs.getString("sang") %></td>
			<td><%=rs.getString("su") %></td>
			<td><%=rs.getString("dan") %></td>
		</tr>
		<%
			}
				
			} catch (Exception e) {
				out.println("실행 에러: " + e);
			} finally{
				
			}
		%>
	</table>
</body>
</html>