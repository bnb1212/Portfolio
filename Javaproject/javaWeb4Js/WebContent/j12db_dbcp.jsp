<%@page import="pack.SangpumDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="connBean" class="pack.ConnBeanPooling" scope="page" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<script type="text/javascript">
	function funcUp() {
		// alert("수정");
		var code = prompt("수정할 코드 입력");
		if (code != "" && code != null)
			location.href = "j12up.jsp?code=" + code;

	}
	function funcDel() {
		//		alert("삭제");
		var code = prompt("삭제할 코드 입력");
		if (code != "" && code != null) {
			if (confirm("진짜 삭제한다? 한다? 진짜해?") == true) {
				location.href = "j12del.jsp?code=" + code;
			}
		}
	}
</script>
</head>
<body>
	<h2>*상품자료 출력(Beans + DBCP 사용)*</h2>
	<a href="j12ins.html">추가</a>&nbsp;
	<a href="javascript:funcUp()">수정</a>&nbsp;
	<a href="javascript:funcDel()">삭제</a>&nbsp;
	<table border='1'>
		<tr>
			<th>code</th>
			<th>sang</th>
			<th>su</th>
			<th>dan</th>
		</tr>
		<%
			ArrayList<SangpumDto> list = connBean.getDataAll();
			for (SangpumDto s : list) {
		%>
		<tr>
			<td><%=s.getCode()%></td>
			<td><%=s.getSang()%></td>
			<td><%=s.getSu()%></td>
			<td><%=s.getDan()%></td>
		</tr>
		<%
			}
		%>

	</table>
</body>
</html>