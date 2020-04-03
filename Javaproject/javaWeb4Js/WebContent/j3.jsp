<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>include</title>
</head>
<body>
	<%@ include file="top.jsp"%>
	<h1>파일의 포함(include)</h1>
	<!-- 지시어는 include지시어와 page 지시어가 있음 -->
	어쩌구 저쩌구
	<br>
	<jsp:include page="action1.jsp" />
	<br>
	<div style="color: blue">
		<jsp:include page="action2.jsp">
			<jsp:param value="korea" name="msg" />

		</jsp:include>
	</div>
	<hr>
	<%@ include file="bottom.jsp"%>
</body>
</html>