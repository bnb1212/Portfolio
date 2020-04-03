
<%@page import="pack.SangpumDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	String code = request.getParameter("code");
	out.print(code);
%>
<jsp:useBean id="connBean" class="pack.ConnBeanPooling"/>
<%
SangpumDto dto = connBean.updateList(code);

if(dto == null){
%>
	<script>
	alert("등록된 상품코드가 아닙니다.");
	location.href="j12db_dbcp.jsp";
	</script>
<%	
	return;
}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
** 상품 수정 ** <br>
<form action="j12upok.jsp" method="post">
코드 : <%=dto.getCode() %><br>
<input type="hidden" name="code" value='<%=dto.getCode()%>'>
 
품명 : <input type="text" name="sang" value="<%=dto.getSang()%>"><br> 
수량 : <input type="text" name="su" value="<%=dto.getSu()%>"><br> 
단가 : <input type="text" name="dan" value="<%=dto.getDan()%>"><br> 
<br>
<input type="submit" value="자료수정">
<input type="button" value="목록보기" onclick="javascript:location.href='j12db_dbcp.jsp'">
</form>

</body>
</html>