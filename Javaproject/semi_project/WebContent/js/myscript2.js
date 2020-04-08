$(document).ready(function() {

	var del_row = $("#btn_insert");
	// ========== 장비 추가 =================
	// +를 누르면 입력창
	$("#btn_equip_insert").click(function(){
		if($(".ins_equip").length){
			$("div.add_div").empty();
		}else{
			
		str = "<form action='admin_equipinsert.jsp' method='post' class='insertform'>"
			+ "<table class='ins_equip'>" 
			+ "<tr><td>품명</td>"
			+ "<td><input type='text' size='5' name='equip_name'></td></tr>"
			+ "<tr><td>보유수</td>"
			+ "<td><input type='text' size='5' name='equip_stock'></td></tr>"
			+ "<tr><td>장비 정보</td>" 
			+ "<td><textarea style='width:300px; height:200px; resize:vertical;' name='equip_info'></textarea></td></tr>"
			+ "<tr><td>이미지 찾기</td>"
			+ "<td><input type='file' name='image'></td></tr>"
			+ "<tr><td colspan='2' style='text-align:right'>" 
			+ "<input type='submit' value='등록'>	</td></tr>"
		str += "</table></form>";
		
		$("div.add_div").append(str);
		}
		return true;
	});
	// ============ 장비 삭제 ==================
	$("#btn_equip_delete").click(function(){
		var del_no = prompt("삭제할 장비 번호를 입력하세요");
		if(confirm("정말 삭제할까요?")){
			location.href="admin_equipdelete.jsp?no="+del_no;
		}else{
			return false;
		}
	});
	
	// ============ 회원 삭제 ===================
	$("#btn_guest_delete").click(function(){
		var del_no = prompt("삭제할 회원 번호를 입력하세요");
		if(confirm("정말 삭제할까요?")){
			location.href="admin_guestdelete.jsp?no="+del_no;
		}else{
			return false;
		}
	});
});
	