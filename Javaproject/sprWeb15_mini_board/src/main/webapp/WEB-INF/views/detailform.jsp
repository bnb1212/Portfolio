<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<script type="text/javascript">
window.onload = function(){
	document.getElementById("btnList").onclick = function(){
		location.href="boardlist";
	}
	
	document.getElementById("btnUpdate").onclick = function(){
		if(confirm("정말 수정할까요?")){
			frm.action="updateAc?num=${data.num}";
			frm.submit();
		}
	}

	document.getElementById("btnDelete").onclick = function(){
		if(confirm("정말 삭제할까요?")){
			frm.action="delete?num=${data.num}";
			frm.submit();
		}
	}
}

</script>
<body>
<h3>내용보기</h3>
<form name="frm" method="post">
	글번호 : ${data.num}<br>
	글제목 : ${data.title }<br>
	작성자 : ${data.author }<br>
	글내용 : ${data.content }<br>

<br>
작성일 : ${data.bwrite }<br>
조회수 : ${data.readcnt }<br>
<input type="button" value="목록" id="btnList">
<input type="button" value="수정" id="btnUpdate">
<input type="button" value="삭제" id="btnDelete">
</form>


<a href="boardlist">목록</a>
</body>
</html>