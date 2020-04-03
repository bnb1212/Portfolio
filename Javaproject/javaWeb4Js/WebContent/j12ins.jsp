<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
%>
<jsp:useBean id="fbean" class="pack.SangpumBean" />
<jsp:setProperty property="*" name="fbean" />
<jsp:useBean id="connBean" class="pack.ConnBeanPooling" />

<%
// System.out.println(fbean.getSang() + " " +fbean.getSu() + " " + fbean.getDan());

	boolean b = connBean.insertData(fbean);
	
	if(b){
		response.sendRedirect("j12db_dbcp.jsp");
	}else{
		response.sendRedirect("j12db_fail.html");
	}
%>
