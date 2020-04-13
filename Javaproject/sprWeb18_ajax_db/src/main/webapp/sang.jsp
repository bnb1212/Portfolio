<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://code.jquery.com/jquery-latest.js"></script>
<script type="text/javascript">
	$(document).ready(function() {
		//alert("a");
		$(".showData").empty();

		$.ajax({
			type : "get",
			url : "sangpum",
			dataType : "json",
			success : function(sangpumData) {
				//alert(sangpumData);
				var str = "<table border='1'>";
				str += "<tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>"
				var list = sangpumData.datas;// 하나면 그냥 받으면 되는데 여러개임. 배열의 대표명을 써주자
				$(list).each(function(index, obj) { // ajax의 list 반복처리
					str += "<tr>";
					str += "<td>" + obj["code"] + "</td>";
					str += "<td>" + obj["sang"] + "</td>";
					str += "<td>" + obj["su"] + "</td>";
					str += "<td>" + obj["dan"]+ "</td>";
					str += "</tr>";

				});

				str += "</table>";
				$(".showData").append(str);
			},
			error : function() {
				$(".showData").text("에러!!!");
			}
		});
	});
</script>

</head>
<body>
	** 상품 정보 (@MVC-MyBatis-Ajax) **
	<br>
	<div class="showData"></div>
</body>
</html>