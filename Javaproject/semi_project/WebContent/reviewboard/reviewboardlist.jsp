<%@page import="pack.reviewboard.ReviewBoardDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="reviewProcess"
	class="pack.reviewboard.ReviewBoardProcess" />
<jsp:useBean id="dto" class="pack.reviewboard.ReviewBoardDto" />
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="f" uri="http://java.sun.com/jsp/jstl/functions"%>
 
<%
	int pageSu, spage = 1;
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<script type="text/javascript">
	window.onload = function() {
		document.getElementById("btnSearch").onclick = function() {
			if (frm.review_sword.value == "") {
				frm.review_sword.focus();
				alert("검색어를 입력하세요");
				return;
			}
			frm.submit(); //stype과 sword를 들고 간다.
		}
	}
</script>
</head>
<body>
	<%@ include file="../index_top.jsp"%>
	<%@ include file="bb_top.jsp"%>
	<br>
	<h3>** 리뷰 게시판 **</h3>
	<table>
		<tr>
			<td>[<a href="reviewboardlist.jsp?page=1">최근목록</a>]&nbsp; [<a
				href="reviewboardwrite.jsp">새글작성</a>]&nbsp; <br> <br>
				<table border='1' style='width: 100%'>
					<tr style="background-color: silver;">
						<th>번호</th>
						<th>글제목</th>
						<th>작성자</th>
						<th>작성일</th>
						<th>조회수</th>
					</tr>
					<%
						request.setCharacterEncoding("utf-8");

						//paging 처리
						try {
							spage = Integer.parseInt(request.getParameter("page"));
						} catch (Exception e) { //페이지가 안나오면 err가 떨어진다. 그래서 spage에 1을 준다.
							//System.out.println("paging err : " + e);
							spage = 1;
						}
						if (spage <= 0)
							spage = 1; //spage는 무조건 1 이상이여야 한다.
						//out.println("spage : " + spage);
						reviewProcess.totalList();
						pageSu = reviewProcess.getPageSu();

						String stype = request.getParameter("review_stype");
						String sword = request.getParameter("review_sword");

						ArrayList<ReviewBoardDto> list = (ArrayList<ReviewBoardDto>) reviewProcess.selectDataAll(spage, stype,
								sword);
					%>
					<c:set var='list' value="<%=list%>" />
					<c:if test="${empty list }">
						<tr>
							<td colspan='5'>자료 없음</td>
						</tr>
					</c:if>
					<c:forEach var='q' items="<%=list%>">
						<tr>
							<td style="text-align: center;">${q.review_no }</td>
							<td><a
								href="reviewboardcontent.jsp?review_no=${q.review_no }&page=<%=spage%>">${q.review_title }</a></td>
							<td style="text-align: center;">작성자</td>
							<td style="text-align: center;">${f:substring(q.review_bdate , 0, 10) }</td>
							<td style="text-align: center;">${q.review_readcnt }</td>
						</tr>
					</c:forEach>
				</table>
				<br>
				<table style='width: 100%;'>
					<tr>
						<td style="text-align: center">
							<%
								//paging 처리 함수
								for (int i = 1; i <= pageSu; i++) {
									if (i == spage) {
										out.print("<b style='color:red;'>[" + i + "]</b>");
									} else {
										out.print("<a href='reviewboardlist.jsp?page=" + i + "'>[" + i + "]</a>");
									}
								}
							%> <br>
						<br>
							<form action="reviewboardlist.jsp" name='frm' method='post'>
								<select name='review_stype'>
									<option value="review_title" selected="selected">글제목</option>
									<option value="name">작성자</option>
								</select> <input type="text" name='review_sword'> <input
									type="button" value='검색' id='btnSearch'>
							</form>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	<%@ include file="../guest/guest_bottom.jsp"%>
</body>
</html>