
<%@page import="pack.business.DataDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="memberProcess" class="pack.business.MemberProcess" />

<%
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id"); // id값 받음
	DataDto dto = memberProcess.selectDataPart(id); // 그 받은 id를 dto찾아 변수 dto에 넣음
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h3>*** 회원 정보 수정 ***</h3>
	<form action="updateok.jsp" method="post">
		id : <%=dto.getId()%>
		<input type="hidden" name="id" value="<%=dto.getId()%>"><br>
		name : <input type="text" name="name" value="<%=dto.getName()%>"><br>
		pwd : <input type="text" name="passwd"> 비밀 번호 불 일치시 수정 불가<br>
		<br> <input type="submit" value="동륵">
	</form>
</body>
</html>