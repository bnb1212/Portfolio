<!-- 이클립스에서는 당장 import data가 보이지 않아 에러로 보이지만
	  실행시켜보면 top에 date를 import했기때문에 j3에서 top, bottom을 같이 부르면
	  문제없이 잘 실행됨을 알 수 있다.
	 -->
<%@page import="java.util.Date"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%= "여기는 bottom ================" %>
<br>문서의 바닥글

<% Date date = new Date(); %>
<%=date.toLocaleString() %>
