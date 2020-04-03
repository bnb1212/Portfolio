<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>휘트니스</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
</head>
<body>
<%@ include file="../index_top.jsp" %>

<%@ include file="guest_top.jsp" %>
<br>
<table style="width: 80%" border="1">
<% if(memid != null){%>
          <tr style="text-align:center;">
          <td>
          <a href="../programs/program_index.jsp">
              <img src="../images/visual.jpg" width="100%"/>
          </a>
          </td>
     <tr>
<%}else{%>
         <tr style="background-position:center;">
          <td>
          <a href="../programs/program_index.jsp">
              <img src="../images/visual.jpg" width="100%"/>
          </a>
          </td>
     <tr>
<%}%>
</table>
<%@ include file="guest_bottom.jsp" %>   
</body>
</html>