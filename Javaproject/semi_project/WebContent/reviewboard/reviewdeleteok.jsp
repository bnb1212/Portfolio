<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>

<jsp:useBean id="reviewProcess" class="pack.reviewboard.ReviewBoardProcess" />

<%
	String spage = request.getParameter("page");
	int no = Integer.parseInt(request.getParameter("review_no"));
	 
	boolean b = reviewProcess.deleteData(no);	//비밀번호 비교
	
	if(b){
		response.sendRedirect("reviewboardlist.jsp");		
	}else{
		response.sendRedirect("fail.jsp");		
	}
%>