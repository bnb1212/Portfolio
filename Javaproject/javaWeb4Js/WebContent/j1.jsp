<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h2>JSP 출발</h2>
	<%
	String ir = "홍길동";  // TomCat에 의해서
	// System.out.println(ir); // 콘솔에 찍히니 개발할땐 사용가능하지만 서비스시 지워야 한다
	out.print(ir + "님의 홈페이지!"); // out.print '내장객체'
	%> 
	
	<!-- h1부터 h6까지 반복해서 점점 작아지게 출력하고 싶다 -->
	<%
	for (int i = 1; i<7; i++){
		out.print("<h" + i + ">");
		out.print("jsp");
		out.print("</h" + i + ">");
	}
	out.println("<br>출력 자료");
	%>
	<br>여기는 html
	<br> <% // <% 는 스크립틀릿
	out.println("<br>출력 자료 2");
	%>
	<br>여기는 html
	<br><%= "<br>출력 자료 3" %>
 	<br>
 	<%
 	int a = 0, sum=0;
 	do{
 		a++;
 		sum += a;
 	}while(a < 10);
 	%>
 	<br>
 	<b><%= "10까지의 합은" + sum %></b>
	<br>
	<!-- 자바스크립트는 클라이언트에 있어 서버단에서 활동못함-->
	<%
	String tel = "02-111-1111"; // JSP도 사실 클래스 
	//...
	
	%>
	<!-- 스크립틀릿 내부의 변수선언 한 것들은 모두 지역변수 -->
	<%= ir + "님의 전화번호는 "%>
	<%! // 이렇게 <%!하면 클래스의 멤버변수(전역변수)를 선언하는것
	 String tel = "02-111-1111";
	//...
	%>
	<%!
		public int add(int m, int n){
		return m + n;
	}
	%>
	<br>
	<%= add(10,20) %>
	
</body>
</html>