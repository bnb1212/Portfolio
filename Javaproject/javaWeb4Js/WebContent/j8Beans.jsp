<%@page import="pack.Gugudan"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	** 현재 실력으로 구구단 출력 **
	
	<br>
	<%
		int dan = Integer.parseInt(request.getParameter("dan"));
			out.println(dan + "단 출력<br>");

		//	Gugudan gugudan = new Gugudan(); // 클라이언트 갯수 만큼 new 하고 있어서 부하가 심하게 걸린다
			// 해답 : 싱글톤을 활용한다
			Gugudan gugudan = Gugudan.getInstance();
		
			int re[] = gugudan.computeGugu(dan);
			for (int a = 0; a < 9; a++) {
		out.println(dan + "*" + (a + 1) + "=" + re[a] + "&nbsp;&nbsp;");
			}
	%>
	<hr>
	** Beans 실력으로 구구단 출력 **<br>
	<jsp:useBean id="gugu" class="pack.Gugudan" scope="page"/> <!-- 싱글톤을 이렇게 제공 
	기본 scope옵션은 page-->
	
	<%
	
	int re2[] = gugudan.computeGugu(dan);
	for (int a = 0; a < 9; a++) {
		out.println(dan + "*" + (a + 1) + "=" + re[a] + "&nbsp;&nbsp;");
	}
	//비즈니스 로직을 바깥으로 뺴고
	%>
</body>
</html>