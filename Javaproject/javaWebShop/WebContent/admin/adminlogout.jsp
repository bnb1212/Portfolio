<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>로그아웃</title>
</head>
<body>
<%
session.removeAttribute("adminKey");
%>
로그아웃 성공
<br><Br>
<a href="../guest/guest_index.jsp">홈페이지</a>
</body>
</html>