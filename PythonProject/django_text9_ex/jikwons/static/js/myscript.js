$(document).ready(function() {
	$("#btnSearch").click(function() {
//		alert('눌림')
		gogek_name = $("name['inp_gogek_name]").val()
		gogek_tel = $("name['inp_gogek_tel]").val()
		$.ajax({
			url : "damsano",
			data : {
				name : gogek_name,
				tel : gogek_tel
			},
			type : "POST",
			dataType : "json",
			success : function(response) {
				$("#jikwon_name").val(response.jikwon_name)
				$("#jikwon_jik").val(response.jikwon_jik)
				$("#buser_name").val(response.buser_name)
				$("#buser_tel").val(response.buser_tel)
				$("#jikwon_gen").val(response.jikwon_gen)
				var ibsail = response.jikwon_ibsail
				var ibsayear = ibsail.substring(0, 4)
				var year = 2020 - parseInt(ibsayear)
				$("#jikwon_ibsail").val(year)
				if (response.jikwon_gen == '남') {
					$("#gen_img").attr("src", "/static/images/질리언.png")
				} else {
					$("#gen_img").attr("src", "/static/images/케이틀린.jpg")
				}

				if (response.jikwon_rating == 'a') {
					$("#jikwon_rating").val('우수')
				} else if (response.jikwon_rating == 'b') {
					$("#jikwon_rating").val('보통')
				} else {
					$("#jikwon_rating").val('일반')
				}
			},
			error : function(request, status, error) {
				alert('ajax 에러')
			}
		});
	});
});