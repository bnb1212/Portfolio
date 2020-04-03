<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
%>

<jsp:useBean id="bean" class="pack.board.BoardBean" scope="page" />
<jsp:setProperty property="*" name="bean" />
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr" />

<%
	bean.setBip(request.getRemoteAddr());
	bean.setBdate();
	int maxNum = boardMgr.currentGetNum() + 1;
	bean.setNum(maxNum);
	bean.setGnum(maxNum);
	boardMgr.saveData(bean); // 저장
	
	response.sendRedirect("boardlist.jsp?page=1");
	
%>
