<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="bean" class="pack.qnaboard.QnaBoardBean" />
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="qnaProcess" class="pack.qnaboard.QnaBoardProcess" />

<%
	String spage = request.getParameter("page");
	//String no = request.getParameter("qna_no");
	boolean b = qnaProcess.editSave(bean);	
	  
	if(b){	
		response.sendRedirect("qnaboardlist.jsp?page="+spage);
	}else{	
		response.sendRedirect("fail.jsp");	
	}
%>
