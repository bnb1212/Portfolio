<%@page import="pack.product.ProductDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr" />
<%
	String no = request.getParameter("no");
	ProductDto dto = productMgr.getProduct(no);
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>상품 상세보기 - 고객</title>
<script type="text/javascript" src="../js/script.js"></script>
<script type="text/javascript" src="../js/script2.js"></script>
<link href="../css/board.css" rel="stylesheet" type="text/css">
</head>
<body>
	<%@ include file="guest_top.jsp"%>
	<form action="cartproc.jsp">
		<table style="width: 80%">
			<tr>
				<td colspan="3">* 상품 상세 보기 *</td>
			</tr>
			<tr>
				<td style="width: 20%"><img src="../upload/<%=dto.getImage()%>"
					width="150"></td>
				<td style="width: 50%; vertical-align: top">
					<table style="width: 100%">
						<tr>
							<td>번호 :</td>
							<td><%=dto.getNo()%></td>
						</tr>
						<tr>
							<td>품명 :</td>
							<td><%=dto.getName()%></td>
						</tr>
						<tr>
							<td>가격 :</td>
							<td><%=dto.getPrice()%></td>
						</tr>
						<tr>
							<td>등록일 :</td>
							<td><%=dto.getSdate()%></td>
						</tr>
						<tr>
							<td>재고 :</td>
							<td><%=dto.getStock()%></td>
						</tr>
						<tr>
							<td>주문수량 :</td>
							<td><input type="text" name="quantity" value="1" size="5"
								style="text-align: center;"></td>
						</tr>
					</table>
				<td style="vertical-align: top;"><b>- 상품 설명 - </b><br> <%=dto.getDetail()%>
				</td>
			</tr>
			<tr>
				<td colspan="3" style="text-align: center;"><br>
					<input type="hidden" name="product_no" value="<%=dto.getNo()%>">
					<input type="submit" value="장바구니에 담기"> 
					<input type="button" value="뒤로 이동" onclick="history.back()">
				</td>
			</tr>

		</table>
	</form>
	<%@ include file="guest_bottom.jsp"%>

	<form action="productdetail_g.jsp" name="detailFrm">
		<input type="hidden" name="no">	
	</form>
</body>
</html>