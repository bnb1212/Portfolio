<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
뷰1 결과 : <br>
출력 1: <%=request.getAttribute("result") %><br>
출력 2 : ${requestScope.result} == ${result}


</body>
</html>