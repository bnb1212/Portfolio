<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="bean" class="pack.reviewboard.ReviewBoardBean" />
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="reviewProcess" class="pack.reviewboard.ReviewBoardProcess" />

<%
request.setCharacterEncoding("utf-8");
int maxNo = reviewProcess.currentGetNum() + 1;
bean.setReview_no(maxNo);
bean.setReview_gnum(maxNo);
reviewProcess.saveData(bean);	//저장하기
 
response.sendRedirect("reviewboardlist.jsp?page=1");	//최근글은 항상 1페이지에 있다.?page=1
%>