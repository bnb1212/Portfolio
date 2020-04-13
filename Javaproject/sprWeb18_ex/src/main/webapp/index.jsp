<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://code.jquery.com/jquery-latest.js"></script>
<script type="text/javascript">
$(document).ready(function(){
	//alert("aa");
	$("#clear").click(function(){
		$("#jikwonpart").empty();
		$("#gogekpart").empty();
		$(".buser").val("");
	});
	
	$("#sub").click(function(){
		var buser_val = $(".buser").val();
		if(buser_val == null || buser_val == ""){
			alert("값을 입력하세요");
			return false;
		}
		
		$("#jikwonpart").empty();
		var buser = $(".buser").serialize();
		
		$.ajax({
		
		type:"get",
		url:"jikwonlist",
		data: buser,
		dataType : "json",
		success:function(jikwonData){
		//alert(jikwonData);
			var str="<table border='1'>";
			str += "<tr><th>직원번호</th><th>직원명</th><th>부서전화</th><th>직급</th>";
			var list = jikwonData.jikDatas;
			$(list).each(function(index, obj){

				var gogek = obj["gogek_damsano"]
				var jik_no = obj["jikwon_no"]
				
				str += "<tr>";
				str += "<td>" + obj["jikwon_no"] +"</td>";
				
				if(gogek != null){
				str += "<td><a href='#' onclick='go("+jik_no+")'>"+obj["jikwon_name"]+"</a></td>";
				}
				else{
					str += "<td>"+obj["jikwon_name"]+"</td>";
				}
				
				str += "<td>" + obj["buser_tel"] +"</td>";
				str += "<td>" + obj["jikwon_jik"] +"</td>";
				str += "<tr>"
				
			});
			str +="</table>";
			$("#jikwonpart").append(str);
			
		},
		error : function(){
			$("#jikwonpart").text("직원 조회 에러");
		}
		});
	});
	
});

	function go(jikno){	
		$("#gogekpart").empty();
		
		$.ajax({
			type:"get",
			url:"gogeklist?jikwon_no="+jikno,
			dataType : "json",
			success:function(gogekData){
			//alert(jikwonData);
				var str="<table border='1'>";
				str += "<tr><th>고객번호</th><th>고객명</th><th>고객전화</th>";
				var list = gogekData.gogekDatas;
				$(list).each(function(index, obj){
					str += "<tr>";
					str += "<td>" + obj["gogek_no"] +"</td>";
					str += "<td>" + obj["gogek_name"]+"</td>";
					str += "<td>" + obj["gogek_tel"] +"</td>";
					str += "<tr>"
					
				});
				str += "<tr><td colspan='3'>고객수 : "+$(list).length+"</td></tr>";
				
				str +="</table>";
				$("#gogekpart").append(str);
				
			},
			error : function(){
				$("#gogekpart").text("고객 조회 에러");
			}
		});
	}

</script>
</head>



<body>
<div id="inputpart">
<form action="jikwonlist" name="frm">
	부서명 : <input class="buser" type="text" name="buser_name"/> &nbsp;
	<input id="sub" type="button" value="확인"/> 
	<input id="clear" type="button" value="초기화"/>
</form>
</div>
<div id="jikwonpart">

</div>
<div id="gogekpart">

</div>
</body>
</html>