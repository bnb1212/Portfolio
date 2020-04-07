<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
품번 사용함<br>
${data}
<hr>
참고 :
<br>
${sangpumBean.sang}
<br>
별명으로 접근 : ${my.sang}
<br>
<%
	ArrayList<String> list = (ArrayList)request.getAttribute("hongList");
	for(String h:list){
		out.println(h + "&nbsp;&nbsp;");
	}
%>
<br>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:forEach var="s" items="${hongList}">
	${s}&nbsp;&nbsp;
</c:forEach>
</body>
</html>