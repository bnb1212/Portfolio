$(document).ready(function() {
	$("#btn1").on("click", function() {
		$("#disp").empty();
		$.ajax({
			type : "get",
			url : "jq6xml1.jsp",
			dataType : "xml",
			success : function(data) {
				// alert(data);
				var str = "";
				$(data).find("person").each(function() {
					str += $(this).find("irum").text() + "&nbsp;";
				});// find로 person 요소 찾아 반복
				$("#disp").append(str);
				// $("#disp").appendTo(data);
			},
			error : function() {
				alert("error");

			},
			statusCode : {
				200 : function() {
					// alert("읽기 성공");
				},
				404 : function() {
					alert("찾기 실패");
				}
			}

		})
	});

	$("#btn2").on("click", function() {
		$("#disp").empty();
		$.ajax({
			type : "get", // post로 적어도 jsp는 get과 post를 구분하지 않으므로 상관없다
			// 값을 담아서 넘기는 방법 1. url에 ? 붙이기
			url : "jq6xml2.jsp",
			// 방법 2.
			// data :"irum=" + "아야세 에리",
			// 방법 3.
			data : {
				"irum" : "안젤리카 안젤루스"
			},
			dataType : "xml",
			success : function(data) {
				// alert(data);
				var str = "";
				$(data).find("person").each(function() {
					str += $(this).find("irum").text() + "&nbsp;";
				});// find로 person 요소 찾아 반복
				$("#disp").append(str);
				// $("#disp").appendTo(data);
			},
			error : function() {
				alert("error");

			}
		});
	});
	$("#btn3").on("click", function() {
		$("#disp").empty();
		$.ajax({
			type : "get",
			url : "jq6json1.jsp",
			dataType : "json",
			success : function(data) {
				var str = "";
				$.each(data, function(index, entry){
					str += entry["name"] + ", " + entry.age;
				})
				$("#disp").append(str);
			},
			error : function() {
				alert("error");
			}
		});
	});
	$("#btn4").on("click", function() {
		$("#disp").empty();
		$.ajax({
			type : "get",
			url : "jq6json2.jsp",
			data:"irum=" + "장비" + "&nai=" + "35",
			dataType : "json",
			success : function(data) {
				var str = "";
				$.each(data, function(index, entry){
					str += entry["name"] + ", " + entry.age;
				})
				$("#disp").append(str);
			},
			error : function() {
				alert("error");
			}
		});
	});

});