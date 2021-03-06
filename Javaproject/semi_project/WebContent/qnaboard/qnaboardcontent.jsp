<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="qnaProcess" class="pack.qnaboard.QnaBoardProcess" />
<jsp:useBean id="dto" class="pack.qnaboard.QnaBoardDto" />

<% 
	String no = request.getParameter("qna_no");
	String spage = request.getParameter("page");

	dto = qnaProcess.getData(no);
	qnaProcess.updateReadcnt(no);

	//굳이 안빼도 되지만 연습.
	
	String qna_title = dto.getQna_title();
	String qna_cont = dto.getQna_cont();
	String qna_bdate = dto.getQna_bdate();
	int qna_readcnt = dto.getQna_readcnt();
%>


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
</head>
<body>
<%@ include file="../index_top.jsp" %>
<%@ include file="aa_top.jsp"%>
* 글 내용 보기 *
	<br>
	<table>
		<tr>
			<td colspan="3" style="text-align: right">
				<a href="qnareply.jsp?qna_no=<%=no %>&page=<%=spage %>">
				<img src = "../images/reply.png">
				</a>
				<a href="qnaedit.jsp?qna_no=<%=no %>&page=<%=spage %>">
				<img src = "../images/edit.png">
				</a>
				<a href="qnadelete.jsp?qna_no=<%=no %>&page=<%=spage %>">
				<img src = "../images/delete.png">
				</a>
				<a href="qnaboardlist.jsp?page=<%=spage %>">
				<img src = "../images/list.png">
				</a>
			</td>
		</tr>
		<tr>
			<td>작성자 : 작성자 </td>
			<td>작성일 : <%=qna_bdate %></td>
			<td>조회수 : <%=qna_readcnt %></td>
		</tr>
		<tr>
			<td colspan="3" style="background-color: silver;">제목 : <%=qna_title %></td>
		</tr>
		<tr>
			<td colspan="3">
				<textarea rows="10" style="width:99%" readonly="readonly"><%=qna_cont %></textarea>
			</td>
		</tr>
	</table>
<%@ include file="../guest/guest_bottom.jsp" %>  
</body>
</html>