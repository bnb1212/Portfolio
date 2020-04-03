<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="bean" class="pack.reviewboard.ReviewBoardBean" />
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="reviewProcess" class="pack.reviewboard.ReviewBoardProcess" />

<%
	String spage = request.getParameter("page");
	//String no = request.getParameter("review_no");
	boolean b = reviewProcess.editSave(bean);	
	 
	if(b){	
		response.sendRedirect("reviewboardlist.jsp?page="+spage);
	}else{	
		response.sendRedirect("fail.jsp");	
	}
%>
