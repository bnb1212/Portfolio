<%@page import="pack.member.ZipCodeDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr" scope='page' />

<%
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id");

	boolean b = memberMgr.checkId(id);
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
</head>
<body>
	<%
		if (b) {
	%>이미 사용중인 id입니다.
	<p/>
	<a href="#" onclick="opener.document.regForm.id.focus(); window.close()">닫기</a>

	<%
		} else {
	%>
	사용 가능한 id입니다.
	<a href="#" onclick="opener.document.regForm.passwd.focus(); window.close()">닫기</a>
	<p />
	<%
		}
	%>
</body>
</html>