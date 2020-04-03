<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	// 현재 jsp 파일은 Business Logic을 담당합니다. 출력용 X
	request.setCharacterEncoding("utf-8");
	String data = request.getParameter("data");
	String msg = "Mr. " + data;

	//1. redirect
	//response.sendRedirect("js5called.jsp?data=" + msg);

	//2. forward
	
	request.setAttribute("data", msg);
	
	ArrayList<String> list = new ArrayList<String>();
	list.add("tom");
	list.add("oscar");
	list.add("alex");
	request.setAttribute("friend", list); 
	// redirect 방식은 string만 넘기는 것이 가능하지만
	// forward 방식은 이런 list 객체도 넘길수 있다
	
	//RequestDispatcher dispatcher = request.getRequestDispatcher("js5called.jsp");
	//dispatcher.forward(request, response);
	
	
%>
<jsp:forward page="js5called.jsp"></jsp:forward>
