<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
%>

<jsp:useBean id="boardMgr" class="pack.board.BoardMgr" />

<%
	String spage = request.getParameter("page");
	String num = request.getParameter("num");
	String pass = request.getParameter("pass");
	boolean b = boardMgr.chkPass(Integer.parseInt(num), pass);

	if (b) {
		boardMgr.delData(num);
		response.sendRedirect("boardlist.jsp?page=" + spage);
	} else {
%>
<script>
	alert("비밀번호 불일치!");
	history.back();
</script>
<%
	}
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