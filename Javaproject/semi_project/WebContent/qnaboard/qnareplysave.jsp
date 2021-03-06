<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="bean" class="pack.qnaboard.QnaBoardBean" />
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="qnaProcess" class="pack.qnaboard.QnaBoardProcess" />

<%
	String spage = request.getParameter("page");
 
	int no = bean.getQna_no();
	int gnum = bean.getQna_gnum();
	int onum = bean.getQna_onum() + 1;
	int nested = bean.getQna_nested() + 1;
	//onum 갱신  - 원글의 댓글1 -> onum+1		원글의 댓글2  현재댓글1 이전댓글+1(2가 됨)
	//같은 그룹 내에서 새로운 댓글의 onum 보다 크거나 같은 값을 댓글 입력 전에 먼저 수정하기 . 작으면 수정 안함.
	qnaProcess.updateOnum(gnum, onum);
	
	//댓글 저장 준비
	bean.setQna_onum(onum);
	bean.setQna_nested(nested);
	bean.setQna_no(qnaProcess.currentGetNum() + 1);	//가장 큰 번호 + 1
	qnaProcess.saveReplyData(bean);
	
	response.sendRedirect("qnaboardlist.jsp?page=" + spage); //댓글 저장 후 목록 보기
	
%>