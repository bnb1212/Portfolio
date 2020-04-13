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
		//alert("good");
		$("#btnOk").click(function(){
			//alert("aa");
			$("#showData").html("");
			$.ajax({ // 아작스 사용
				type:"get",
				url:"list",
				data:{"name":"oscar"}, // JsonController의 파라미터(매개변수)
				dataType:"json", // 리턴 받는 데이터 타입
				success:function(data){
					//alert(data);
					var str="";
					str += data.name + " <br>";
					str += data.skills[0] + " " + data.skills[1];
					$("#showData").html(str);
					
				},error:function(){
					$("#showData").text("에러 발생");
				}
			
			}); 
			
		});
		$("#btnOk2").click(function(){
			//alert("bb");
			$("#showData").html("");
			$.ajax({
				type:"get",
				url:"list2",
				dataType:'json',
				success:function(data){
					//alert(data);
					var str = "<table>";
					var list = data.datas;// 하나면 그냥 받으면 되는데 여러개임. 배열의 대표명을 써주자
					$(list).each(function(index, obj){ // ajax의 list 반복처리
						str += "<tr>";
						str += "<td>" + obj["name"] + "</td>";
						str += "<td>" + obj.age + "</td>";
						str += "</tr>";
						
					}); 				
					str += "</table>";
					$("#showData").html(str);
				},
				error:function(){
					$("#showData").text("에러발생2");
				}
			
			});
		});
	});
</script>
</head>
<body>
	JSON 자료 읽기 - Ajax
	<br>
	<input type="button" value="한 개의 자료 읽기" id="btnOk">
	<br>
	<input type="button" value="여러 개의 자료 읽기" id="btnOk2">
	<br>
	<br>
	<div id="showData"></div>

</body>
</html>