<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="sform" uri="http://www.springframework.org/tags/form"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>자료 입력</h2>
	<sform:form commandName="command">
i d : <sform:input path="userid" />
		<sform:errors path="userid" />
		<br>
pwd : <sform:input path="passwd" />
		<sform:errors path="passwd" />
		<br>
		<br>
		<input type="submit" value="전송">
	</sform:form>

	<hr>
	<form id="command" action="/cc/login" method="post">
		i d : <input id="userid" name="userid" type="text" value="" /><br>
		pwd : <input id="passwd" name="passwd" type="text" value="" /><br>
		<br> <input type="submit" value="전송">
</body>
</html>