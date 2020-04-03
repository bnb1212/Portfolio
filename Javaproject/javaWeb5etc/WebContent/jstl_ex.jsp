<%@page import="java.util.Date"%>
<%@page import="java.util.HashMap"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<jsp:useBean id="connBean" class="pack.ConnBean" scope="page" />


<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
* JSTL(JSP Standard tag Library) * <p/>
*** 변수 연습<br>
<c:set var="irum" value="홍길동" scope="page" /> <!-- page, request, session, application -->
<c:out value="${irum }"/>
<br>
<c:set var="ir" scope="session">
한국인
</c:set>
<c:out value="${ir }"/>
<br>
<c:set var="aa" value="${header['User-Agent']}" scope="page" />
aa 변수 값은 <c:out value="${aa}"/>
<br>
<c:set var="su1" value="10"/>
<c:set var="su2">
10.5
</c:set>
합은 ${su1 + su2 }
<p>
** 조건문(if)<br>
<c:set var="bb" value="star" />
<c:if test="{bb} == 'tar'"></c:if>
if 연습 : bb 값은 <c:out value="${bb }"/>
<br>
<c:if test="${bb != null}">
if 연습2 : 조건 참
</c:if>
<p>

** 조건문(choose)<br>
<c:choose>
<c:when test="${bb == 'moon' }">
달이야
</c:when>
<c:when test="${bb eq 'star'}">
별
</c:when>
<c:otherwise>어떠한 조건도 만족하지 않을 경우</c:otherwise>
</c:choose>

<hr>
** 반복문(forEach)<br>
<c:forEach var="i" begin="1" end="9">
	<c:out value="${i }" />&nbsp;&nbsp;
</c:forEach>
<br>
구구단(3)<br>
<c:forEach var="su" begin="1" end="9">
3 * ${su } = ${3 * su }<br>
</c:forEach>
<br>
header정보 출력<br>
<c:forEach var="h" items="${headerValues }">
	속성 : <c:out value="${h.key }"/>&nbsp;&nbsp;
	값 : <c:forEach var="k" items="${h.value }">
		${k }<br>
	</c:forEach>
</c:forEach>
<hr>
<%
HashMap map = new HashMap();
map.put("name", "신기해");
map.put("today", new Date());
%>
<c:set var="m" value="<%=map %>"/>
<c:forEach var="i" items="${map }">
	${i.key } : ${i.value }<br>
</c:forEach>
<br>
<c:set var="arr" value="<%= new int[]{1,2,3,4,5}  %>"></c:set>
<c:forEach var="i" items="${arr }" begin="2" end="8" step="2">
	${i }&nbsp;
</c:forEach>
<hr>
********** 문자열 분할 ********** <br>
<c:forTokens var="animal" items="horse,tiger,lion,pig,cat" delims=",*" varStatus="num"> 
	동물 ${num.count }: ${animal }&nbsp; 
</c:forTokens>
<hr>
<br>
** 숫자 및 날짜 관련 서식 <br>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
숫자 : <fmt:formatNumber value="12345.6789" type="number"/><br>
통화 : <fmt:formatNumber value="12345.6789" type="currency" currencySymbol="$"/><br>
백분율 : <fmt:formatNumber value="12345.6789" type="percent"/><br>
소수 이하 : <fmt:formatNumber value="12345.6789" type="number" pattern="#,##0.0"/> --> #,##0.0<br>
소수 이하 : <fmt:formatNumber value="12345.6789" type="number" pattern="0,000.0"/> --> 0,000.0<br>
소수 이하 : <fmt:formatNumber value="1.6789" type="number" pattern="#,##0.0"/> --> #,##0.0<br>
소수 이하 : <fmt:formatNumber value="1.6789" type="number" pattern="0,000.0"/> --> 0,000.0<br>
# : 무효의 제로<br>
0 : 유효의 제로<br>
, : 자릿수마다 콤마찍기<br>
<c:set var="now" value="<%=new Date() %>" />
<c:out value="${now }"/>
<fmt:formatDate value="${now }" type="date"/><br>
<fmt:formatDate value="${now }" type="time"/><br>
<fmt:formatDate value="${now }" type="both"/><br>
<fmt:formatDate value="${now }" type="both" pattern="yyyy년 MM월 dd일"/><br>
<br>


</body>
</html>