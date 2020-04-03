<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="qnaProcess" class="pack.qnaboard.QnaBoardProcess" />
<jsp:useBean id="dto" class="pack.qnaboard.QnaBoardDto" />
<%
	String no = request.getParameter("qna_no");
	String spage = request.getParameter("page");
	dto = qnaProcess.getReplyData(no);	//답글 대상 자료 읽기
%>  
 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>답글 추가</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<script type="text/javascript">
function check(){
	if(frm.qna_name.value==""){
		alert("이름을 입력하세요");
		frm.qna_name.focus();
	}else if(frm.qna_title.value ==""){
		alert("제목을 입력하세요");
		frm.qna_title.focus();
	}else if(frm.qna_cont.value ==""){
		alert("내용을 입력하세요");
		frm.qna_cont.focus();
	}else
		frm.submit();
}
</script>
</head>
<body>
<form name="frm" method="post" action="qnareplysave.jsp">
	<!-- 데이터 들고갈거 정의 -->
	<input type="hidden" name ="qna_no" value="<%=no %>">
	<input type="hidden" name ="page" value="<%=spage %>">
	<input type="hidden" name ="qna_gnum" value="<%=dto.getQna_gnum() %>">
	<input type="hidden" name ="qna_onum" value="<%=dto.getQna_onum() %>">
	<input type="hidden" name ="qna_nested" value="<%=dto.getQna_nested() %>">
	
	<table border="1" style="width:530">
		<tr>
			<td colspan='2'><h2>*** 댓글쓰기 ***</h2></td>
		</tr>
		<tr>
			<td align="center" width="100">이 름</td>
			<td width="430"><input name="qna_name" size="15" value="작성자"></td>
		</tr>
		<tr>
			<td align="center">제 목</td>
			<td><input name="qna_title" size="50" value="[Re]:<%=dto.getQna_title() %>"></td>
		</tr>
		<tr>
			<td align="center">내 용</td>
			<td><textarea name="qna_cont" cols="50" rows="10"></textarea></td>
		</tr>
		<tr>
			<td colspan="2" align="center" height="30">
				<input type="button" value="작  성" onClick="check()">&nbsp;
				<input type="button" value="목  록"
				  onClick="location.href='qnaboardlist.jsp?page=<%=spage%>'"></td>
		</tr>
	</table>
</form>
</body>
</html>