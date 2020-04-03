$(document).ready(function(){
	//alert('a');
	// 1. html 읽기
	$("#test1").click(function(){
		$("#disp").load("jq5h.html");
	});
	
	
	// 1. json 읽기1
	$("#test2").click(function(){
		$("#disp").empty();
		$.getJSON("jq5j1.json", function(data){
			// alert(data);
			$.each(data,function(keyindex, value){ // object를 반복할 떄는 each사용
				var str = "<ol>";
				str += "<li>" + value["title"] + "</li>";
				str += "<li>" + value["desc"] + "</li>";
				str += "<li>" + value["author"] + "</li>";
				str += "</ol>";
				$("#disp").append(str);
			});
		});
	
	});
	
	// 1. json 읽기2
	$("#test3").click(function(){
		$("#disp").empty();
		$.getJSON("jq5json.jsp", function(data){
			// alert(data);
			var items =[];
			$.each(data,function(keyindex, value){ // object를 반복할 떄는 each사용
				var str = "<ul>";
				str += "<li>" + value["code"] + "</li>";
				str += "<li>" + value["sang"] + "</li>";
				str += "<li>" + value["su"] + "</li>";
				str += "<li>" + value["dan"] + "</li>";
				str += "</ul>";
				//$("#disp").append(str);
				items.push(str);
			});
			$("<b/>", {html:items}).appendTo("#disp");
			// appendTo는 disp의 뒤로 들어가고, append하면 앞으로 들어감
		});
	
	});
	// 1. xml 읽기1
	$("#test4").click(function(){
		$("#disp").empty();
		
		$.get("jq5x1.xml", function(data){
			// alert($(data).find("aa").size()); // 불러온 data에 자식으로 aa라는 Element가 있는지 찾아서 사이즈 확인
			$(data).find("aa").each(function(){ // each는 반복
				var fdata = $(this); // 현재 읽힌 aa 요소(Element)
				var str = "<div>";
				str += fdata.attr("part") + " "; // attr()로 속성값 받기
				str += fdata.attr("term") + " - ";
				str += fdata.find("desc").text();
				str += "</div>";
				
				$("#disp").append(str);
			});
		});
	});
	
	// 1. xml 읽기2
	$("#test5").click(function(){
		$("#disp").empty();
		
		$.get("jq5xml.jsp", function(data){
			$(data).find("sangpum").each(function(){
				var sangpum =  $(this);
				var str = "<div>";
				str += sangpum.find("code").text() + " ";
				str += sangpum.find("sang").text() + " ";
				str += sangpum.find("su").text() + " ";
				str += sangpum.find("dan").text();
				str + "<div>";
				
				$("#disp").append(str);
				
			});
		});
		
	});
	
	
});
