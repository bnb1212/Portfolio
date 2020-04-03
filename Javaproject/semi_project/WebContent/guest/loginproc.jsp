<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
request.setCharacterEncoding("utf-8");
request.getParameter("guest_id");
request.getParameter("guest_passwd");
%>    
<jsp:useBean id="gbean" class="pack.guest.GuestBean" />
<jsp:setProperty property="*" name="gbean"/>
<jsp:useBean id="memberProcess" class="pack.guest.MemberProcess" />

<%
boolean b = memberProcess.loginCheck(gbean);
if(b){
	session.setAttribute("idkey", gbean.getGuest_id());
	//response.sendRedirect("login.jsp");
	response.sendRedirect("../main.jsp");
}else{
	response.sendRedirect("loginfail.html");
}
%>