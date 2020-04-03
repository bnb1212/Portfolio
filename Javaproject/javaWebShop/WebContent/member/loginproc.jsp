<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="mbean" class="pack.member.MemberBean" />
<jsp:setProperty property="*" name="mbean" />
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr" />
<%-- id 첫글자에 대문자 쓰지 마라  --%>

<%
boolean b = memberMgr.loginCheck(mbean.getId(), mbean.getPasswd());
if(b){
	session.setAttribute("idKey", mbean.getId());
	//response.sendRedirect("login.jsp");
	response.sendRedirect("../index.jsp");
}else{
	response.sendRedirect("loginfail.html");
}
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

</body>
</html>