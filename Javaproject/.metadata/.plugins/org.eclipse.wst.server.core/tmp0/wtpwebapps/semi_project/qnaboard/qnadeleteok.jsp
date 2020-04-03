<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>

<jsp:useBean id="qnaProcess" class="pack.qnaboard.QnaBoardProcess" />

<%
	String spage = request.getParameter("page");
	int no = Integer.parseInt(request.getParameter("qna_no"));
	
	boolean b = qnaProcess.deleteData(no);	//비밀번호 비교
	 
	if(b){
		response.sendRedirect("qnaboardlist.jsp");		
	}else{
		response.sendRedirect("fail.jsp");		
	}
%>