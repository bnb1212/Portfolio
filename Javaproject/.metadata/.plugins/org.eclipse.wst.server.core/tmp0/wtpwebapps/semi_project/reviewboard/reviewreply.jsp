<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="reviewProcess" class="pack.reviewboard.ReviewBoardProcess" />
<jsp:useBean id="dto" class="pack.reviewboard.ReviewBoardDto" />
<%
	String no = request.getParameter("review_no");
	String spage = request.getParameter("page");
	dto = reviewProcess.getReplyData(no);	//답글 대상 자료 읽기
%>  
 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>답글 추가</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<script type="text/javascript">
function check(){
	if(frm.review_name.value==""){
		alert("이름을 입력하세요");
		frm.review_name.focus();
	}else if(frm.review_title.value ==""){
		alert("제목을 입력하세요");
		frm.review_title.focus();
	}else if(frm.review_cont.value ==""){
		alert("내용을 입력하세요");
		frm.review_cont.focus();
	}else
		frm.submit();
}
</script>
</head>
<body>
<form name="frm" method="post" action="reviewreplysave.jsp">
	<!-- 데이터 들고갈거 정의 -->
	<input type="hidden" name ="review_no" value="<%=no %>">
	<input type="hidden" name ="page" value="<%=spage %>">
	<input type="hidden" name ="review_gnum" value="<%=dto.getReview_gnum() %>">
	<input type="hidden" name ="review_onum" value="<%=dto.getReview_onum() %>">
	<input type="hidden" name ="review_nested" value="<%=dto.getReview_nested() %>">
	
	<table border="1" style="width:530">
		<tr>
			<td colspan='2'><h2>*** 댓글쓰기 ***</h2></td>
		</tr>
		<tr>
			<td align="center" width="100">이 름</td>
			<td width="430"><input name="review_name" size="15" value="작성자"></td>
		</tr>
		<tr>
			<td align="center">제 목</td>
			<td><input name="review_title" size="50" value="[Re]:<%=dto.getReview_title() %>"></td>
		</tr>
		<tr>
			<td align="center">내 용</td>
			<td><textarea name="review_cont" cols="50" rows="10"></textarea></td>
		</tr>
		<tr>
			<td colspan="2" align="center" height="30">
				<input type="button" value="작  성" onClick="check()">&nbsp;
				<input type="button" value="목  록"
				  onClick="location.href='reviewboardlist.jsp?page=<%=spage%>'"></td>
		</tr>
	</table>
</form>
</body>
</html>