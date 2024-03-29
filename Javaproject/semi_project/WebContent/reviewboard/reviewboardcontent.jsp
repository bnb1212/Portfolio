<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="reviewProcess" class="pack.reviewboard.ReviewBoardProcess" />
<jsp:useBean id="dto" class="pack.reviewboard.ReviewBoardDto" />

<%
	String no = request.getParameter("review_no");
	String spage = request.getParameter("page");
 
	dto = reviewProcess.getData(no);
	reviewProcess.updateReadcnt(no);

	//굳이 안빼도 되지만 연습.
	 
	String review_title = dto.getReview_title();
	String review_cont = dto.getReview_cont();
	String review_bdate = dto.getReview_bdate();
	int review_readcnt = dto.getReview_readcnt();
%>


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
</head>
<body>

* 글 내용 보기 *
<%@ include file="../index_top.jsp" %>
<%@ include file="bb_top.jsp"%>
	<br>
	<table>
		<tr>
			<td colspan="3" style="text-align: right">
				<a href="reviewreply.jsp?review_no=<%=no %>&page=<%=spage %>">
				<img src = "../images/reply.png">
				</a>
				<a href="reviewedit.jsp?review_no=<%=no %>&page=<%=spage %>">
				<img src = "../images/edit.png">
				</a>
				<a href="reviewdelete.jsp?review_no=<%=no %>&page=<%=spage %>">
				<img src = "../images/delete.png">
				</a>
				<a href="reviewboardlist.jsp?page=<%=spage %>">
				<img src = "../images/list.png">
				</a>
			</td>
		</tr>
		<tr>
			<td>작성자 : 작성자 </td>
			<td>작성일 : <%=review_bdate %></td>
			<td>조회수 : <%=review_readcnt %></td>
		</tr>
		<tr>
			<td colspan="3" style="background-color: silver;">제목 : <%=review_title %></td>
		</tr>
		<tr>
			<td colspan="3">
				<textarea rows="10" style="width:99%" readonly="readonly"><%=review_cont %></textarea>
			</td>
		</tr>
	</table>
<%@ include file="../guest/guest_bottom.jsp" %> 
</body>
</html>