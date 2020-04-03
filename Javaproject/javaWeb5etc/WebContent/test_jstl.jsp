<%@page import="pack.Person"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	* 서블릿에서 작성한 개체 출력 * - 방법 비교
	<br> 전통 : 안녕
	<%=request.getAttribute("man")%><br> EL : 안녕 ${requestScope.man }
	${man }
	<p />
	requestScope는 하도 많이 써서 생략 가능 \${requestScope.man } -> \${man }
	<br>
	<br> 전통 :
	<%
		Person p = (Person) request.getAttribute("person");
	%>
	<%=p.getName()%>
	EL : ${person.name }
	<br> EL : ${student.age }
	<br> ${animal[0] } ${animal[1] } ${animal["2"] }
	<br>
	<br>
	<c:if test="${list != null}">
		<c:forEach var="a" items="${list }">
		${a[0] },${a[1] },${a[2] }
	</c:forEach>
	</c:if>
	<br>
	<br>
	<c:if test="${list != null}">
		<c:forEach var="a" items="${list }">
			<c:forEach var='b' items="${a }">
			${b	 }
			</c:forEach>
		</c:forEach>
	</c:if>
	<br>
	<c:choose>
		<c:when test="${list eq null }">자료 없음</c:when>
		<c:otherwise>자료있음</c:otherwise>
	</c:choose>
	
	<hr>
	try ~ except 처리 <br>
	자바와 비교해보자<br>
	
	<c:catch var="myErr">
		<% int a = 10/0; %>
		out.println("a는 " + a);
	</c:catch>
	<c:if test="${myErr != null }">
	에러 발생 : ${myErr.message }
	</c:if>
	<br>
	<br>
	다른 문서 포함<br>
	include 지시어 사용 : <%@include file="poham.jsp" %><br>
	jsp action tag 사용 : <jsp:include page="poham.jsp"/><br>
	jstl 사용 :<c:import url="poham.jsp"/>
	<%-- <br>
	<c:import url="https://www.dcinside.co.kr"/>
	<br>--%>
	<c:set var="url" value="https://www.naver.com"/>
	<c:import url="${url}" var="u"/>
	<c:out value="${url}"/>
	<c:out value="${u}"/>
	
</body>
</html>