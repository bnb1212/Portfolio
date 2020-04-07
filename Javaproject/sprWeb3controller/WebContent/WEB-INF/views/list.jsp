<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
Controller 처리후 결과 : <br>
<% 
String ss = (String)request.getAttribute("key");
out.println(ss);

%>
<br>
${key}
</body>
</html>