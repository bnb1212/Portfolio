<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%
    request.setCharacterEncoding("utf-8");
    //String msg = request.getParameter("message");
    %>
    
    <jsp:useBean id="my" class="pack.Para1Class" /> <!-- Para1Class 클래스를 가지는 객체를 싱글톤으로 생성-->
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
* 클래스 private 멤버 필드에 값 설정하고 참조하기 *
<br>
<%
// 지금까지 기술로 코드를 작성하면
//my.setMessage(msg);
//out.println(my.getMessage());

%>
<!-- 
<jsp:setProperty property="message" name="my" value="푸하하하"/>
-->
<jsp:setProperty property="message" name="my"/>
<jsp:getProperty property="message" name="my"/>
 <!-- setter와 같은 역할함. property의 값은 멤버필드-->
 <!-- 클라이언트에서 넘겨받는 파라미터 이름과 프로퍼티 이름값을 일치시키면 시스템에서 자동적으로  
 	넘겨받은 파라미터 값을 세팅해준다 -->
</body>
</html>