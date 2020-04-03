<%@page import="pack.product.ProductMgr"%>
<%@page import="pack.product.ProductDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>상품목록 - 고객</title>
<link href="../css/board.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="../js/script.js"></script>
<script type="text/javascript" src="../js/script2.js"></script>
</head>
<body>
	<h2>전문 쇼핑몰</h2>
	<%@ include file="guest_top.jsp"%>
	* 고객님 지갑을 마음껏 열어주세요 *
	<br>
	<table style="width: 80%">
		<tr style="backgroud-color: silver;">
			<th>상품명</th>
			<th>가격</th>
			<th>재고량</th>
			<th>상세보기</th>
		</tr>
		<%
			ArrayList<ProductDto> list = productMgr.getProductAll();
			for (ProductDto p : list) {
		%>
		<tr>
			<td><img src="../upload/<%=p.getImage()%>" width="100"> <%=p.getName()%></td>
			<td><%=p.getPrice()%></td>
			<td><%=p.getStock()%></td>
			<td><a href="javascript:productDetail('<%=p.getNo()%>')">상세보기</a></td>
		</tr>
		<%
			}
		%>
	</table>
	
	<%@include file="guest_bottom.jsp"%>
	<form action="productdetail_g.jsp" name="detailFrm" method="post">
	<input type="hidden" name="no">
	</form>
</body>
</html>