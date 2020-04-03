<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	String memid = (String) session.getAttribute("idkey");
	String log = "";

	if (memid == null) // 로그인 안함
		log = "<a href='../guest/login.jsp'><img src='../images/loginin.png'></a>";
	else
		log = "<a href='../guest/logout.jsp'><img src='../images/logout.png'></a>";

	String mem = "";

	if (memid == null)
		mem = "<a href='../member/register.jsp'><img src='../images/signup.png'></a>";
	else
		mem = "<a href='../reviewboard/reviewboardlist.jsp'><img src='../images/review.png'></a>";
%>
<table style="width: 80%" border="1">
	<tr style="background-color: white; text-align: center;">
		<td><a href="../main.jsp"><img src="../images/home.png"></a></td>
		<td><%=log%></td>
		<td><%=mem%></td>
		<td><a class="menu_1" href="../fitness/fitness.jsp"><img
				src="../images/fitness.png"></a></td>
		<td><a href="../trainers/trainers_index.jsp"><img
				src="../images/trainers.png"></a></td>
		<td><a href="../programs/program_index.jsp"><img
				src="../images/programs.png"></a></td>
		<td><a href="../qnaboard/qnaboardlist.jsp"><img
				src="../images/community.png"></a></td>
	</tr>
</table>