<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<%
	request.setCharacterEncoding("utf-8");
%>
<jsp:useBean id="qnaProcess" class="pack.qnaboard.QnaBoardProcess" />
<jsp:useBean id="dto" class="pack.qnaboard.QnaBoardDto" />

<%
	String no = request.getParameter("qna_no");
	String spage = request.getParameter("page");
 
	dto = qnaProcess.getData(no); //수정 대상 자료 읽기
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판 수정</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<script type="text/javascript">
function check() {
	if(confirm("정말 수정할까요?")){
		frm.submit();
	}
}
</script>
</head>
<body>
<%@ include file="../index_top.jsp" %>
<%@ include file="aa_top.jsp"%>
<br>
	<form name="frm" method="post" action="qnaeditsave.jsp">
		<!-- 데이터 들고갈거 정의 -->
		<input type="hidden" name="qna_no" value="<%=no%>"> <input
			type="hidden" name="page" value="<%=spage%>">

		<table border="1">
			<tr>
				<td colspan='2'><h2>*** 글수정 ***</h2></td>
			</tr>
			<tr>
				<td align="center" width="100">작성자</td>
				<td width="430"><input name="name" size="15" value="작성자"></td>
			</tr>
			<tr>
				<td align="center">제 목</td>
				<td><input name="qna_title" size="50"
					value="<%=dto.getQna_title()%>"></td>
			</tr>
			<tr>
				<td align="center">내 용</td>
				<td><textarea name="qna_cont" cols="50" rows="10"><%=dto.getQna_cont()%></textarea></td>
			</tr>
			<tr>
				<td colspan="2" align="center" height="30"><input type="button"
					value="수정완료" id="btnOk" onclick="check()">&nbsp; <input type="button"
					value="목록보기"
					onClick="location.href='qnaboardlist.jsp?page=<%=spage%>'"></td>
			</tr>
		</table>
	</form>
<%@ include file="../guest/guest_bottom.jsp" %>
</body>
</html>