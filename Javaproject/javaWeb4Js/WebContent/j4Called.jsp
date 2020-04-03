<%@page import="org.apache.catalina.filters.SetCharacterEncodingFilter"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
서블릿에 의해 호출된 jsp 파일
<br>
<%
request.setCharacterEncoding("utf-8");

// redirect 방식일때
//String data = request.getParameter("data");
//out.print("자료: " + data);


//forward 방식일때
String data = (String)request.getAttribute("key");
out.print("자료: " + data);

%>
</body>
</html>