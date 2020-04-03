<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
		if (request.getParameter("name") == null) {
	%>
	<jsp:forward page="el.html"></jsp:forward> <!-- 포워딩으로 부름 -->

	<%
		}
	%>
	
	표현식 사용 : <%=request.getParameter("name") %>
	<br>
	스크립트렛 사용
	<%
	out.println(request.getParameter("name"));
	%>
	<br>
	EL 사용 : ${param.name}
</body>
</html>