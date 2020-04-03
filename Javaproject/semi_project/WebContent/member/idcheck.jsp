<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="memberProcess" class="pack.guest.MemberProcess" scope="page" />
<%
request.setCharacterEncoding("utf-8");
String guest_id = request.getParameter("guest_id");


boolean b = memberProcess.checkId(guest_id);
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
<b><%=guest_id %></b> :
<%
if(b){
%>	
	이미 사용중인 id입니다.<p/>
	<a href="#" onclick="opener.document.regForm.guest_id.focus(); window.close()">닫기</a>
<%}else{%>
	사용 가능한 id입니다.<p/>
	<a href="#" onclick="opener.document.regForm.guest_passwd.focus(); window.close()">닫기</a>
<%	
}
%>
</body>
</html>