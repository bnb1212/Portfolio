<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@taglib prefix="sform" uri="http://www.springframework.org/tags/form"  %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
** 자료 추가 **<br>
<sform:form modelAttribute="command">
아이디 : <sform:input path="id"/><br>
패스워드 : <sform:input path="passwd"/><br>
이름 : <sform:input path="name"/><br>
<br>
<input type="submit" value="추가">
</sform:form>
</body>
</html>