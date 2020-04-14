<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="sform" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
** 파일 업로드 **<br>
<sform:form enctype="multipart/form-data" modelAttribute="uploadFile">
업로드할 파일 선택 : <br>
<input type="file" name="file">
<sform:errors path="file"/> 
<input type="submit" value="전송"/>
</sform:form>
</body>
</html>