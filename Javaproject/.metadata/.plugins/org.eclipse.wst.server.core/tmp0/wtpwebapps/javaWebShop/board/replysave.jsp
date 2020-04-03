<%@page import="pack.board.BoardMgr"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
%>
<jsp:useBean id="bean" class="pack.board.BoardBean" />
<jsp:setProperty property="*" name="bean" />
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr" />

<%
	String spage = request.getParameter("page");

	int num = bean.getNum();
	int gnum = bean.getGnum();
	int onum = bean.getOnum() + 1;
	int nested = bean.getNested() + 1;
	// onum 갱신 원글의 댓글1 + 1
	// 같은 그룹 내에서 새로운 댓글의 onum보다 크거나 같은 값을 댓글 입력 전에 먼저 수정하기.
	// 작으면 수정 안함

	boardMgr.updateOnum(gnum, onum);

	//댓글 저장 준비
	bean.setOnum(onum);
	bean.setNested(nested);
	bean.setBip(request.getRemoteAddr());
	bean.setNum(boardMgr.currentGetNum() + 1);
	bean.setBdate();
	boardMgr.saveReplyData(bean);
	
	response.sendRedirect("boardlist.jsp?page="+spage);
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