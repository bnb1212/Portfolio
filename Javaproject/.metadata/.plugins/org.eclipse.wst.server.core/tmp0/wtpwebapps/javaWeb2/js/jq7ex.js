$(document).ready(function() {
	$("#btnOk").on("click", function() {
		
		// alert("버튼 클릭"); // ====== TEST ======
		$("#dispJik").empty();
		$("#countJik").empty();
		$("#dispGogek").empty();
		var buser_name = $("#buserName").val();
		if(buser_name === ""){
			alert("빈칸 안돼");
		}
		// alert(buser_name);
		
		$.ajax({
			type : "get",
			url : "jq7json.jsp",
			data:"buserName=" + buser_name,
			dataType : "json",
			success : function(data) {
				var str = "<table border='1'>";
				str += "<tr><th>직원번호</th>" 
					+ "<th>직원명</th>" 
				    + "<th>부서전화</th>"
				    + "<th>관리고객 수</th></tr>";
				$.each(data, function(index, entry){
					str += "<tr>";
					str += "<td>" + entry["jikNo"] + "</td>";
					str += "<td><a href=\"javascript:func('" + entry["jikNo"] + "')\">" +entry["jikName"]+"</a></td>";
					str += "<td>" + entry["buserTel"] + "</td>";
					str += "<td>" + entry["gogekSu"] + "</td>";
					str += "</tr>"
				})
				str += "</table>";
				$("#dispJik").append(str);
				
				str2 = "<b> 직원수 : " + Object.keys(data).length + "</b>";
				$("#countJik").append(str2);
			},
			error : function() {
				alert("error");
			}
		});
		});
	
	/*
	$("a.more").click(function() {
		System.out.println("클릭");
		alert("이름 클릭");
	});
	*/
	//끝
	});

function func(arg) {
	alert(arg);
	$("#dispGogek").empty();
	var jikwonNo = arg;
	// alert(buser_name);
	
	$.ajax({
		type : "get",
		url : "jq7json2.jsp",
		data:"jikwonNo=" + jikwonNo,
		dataType : "json",
		success : function(data) {
			var str = "<table border='1'>";
			str += "<tr><th>고객명</th>" 
				+ "<th>고객전화</th>" 
			    + "<th>성별</th></tr>";
			
			$.each(data, function(index, entry){
				str += "<tr>";
				str += "<td>" + entry["gogekName"] + "</td>";
				str += "<td>"+ entry["gogekTel"] + "</td>";
				str += "<td>" + entry["gogekGen"] + "</td>";
				str += "</tr>"
			})
			str += "</table>";
			$("#dispGogek").append(str);

		},
		error : function() {
			alert("error");
		}
	});
	}
