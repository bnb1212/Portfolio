<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="bean" class="pack.qnaboard.QnaBoardBean" />
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="qnaProcess" class="pack.qnaboard.QnaBoardProcess" />

<%
request.setCharacterEncoding("utf-8");
int maxNo = qnaProcess.currentGetNum() + 1;
bean.setQna_no(maxNo);
bean.setQna_gnum(maxNo);
qnaProcess.saveData(bean);	//저장하기
 
response.sendRedirect("qnaboardlist.jsp?page=1");	//최근글은 항상 1페이지에 있다.?page=1
%>