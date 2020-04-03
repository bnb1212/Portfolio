<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String code= request.getParameter("code");
%>
<jsp:useBean id="connBean" class="pack.ConnBeanPooling" />

<%
// System.out.println(fbean.getSang() + " " +fbean.getSu() + " " + fbean.getDan());
	
	if(connBean.deleteData(code)){
		response.sendRedirect("j12db_dbcp.jsp");
	}else{
		response.sendRedirect("j12db_fail.html");
	}
%>