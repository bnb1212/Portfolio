<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib prefix ="sform" uri="http://www.springframework.org/tags/form" %>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2> 자료 입력  </h2>
<sform:form modelAttribute="command">
i d : <sform:input path="userid"/><br>
pwd : <sform:input path="passwd"/><br>
<br>
<input type="submit" value="전송">
</sform:form>
</body>
</html>