<%@page import="pack.SangpumDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="connBean" class="pack.ConnBean" scope="page" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>*상품자료 출력(Beans 사용)*</h2>
	<table border='1'>
		<tr>
			<th>code</th>
			<th>sang</th>
			<th>su</th>
			<th>dan</th>
		</tr>
		<%
		ArrayList<SangpumDto> list = connBean.getDataAll();
		for(SangpumDto s:list) {
			%>
		<tr>
			<td><%= s.getCode() %></td>
			<td><%= s.getSang() %></td>
			<td><%= s.getSu() %></td>
			<td><%= s.getDan() %></td>
		</tr>
		<%
		}
		%>

	</table>
</body>
</html>