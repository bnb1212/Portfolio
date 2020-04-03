function zipCheck(){
	url = "zipcheck.jsp?check=y";
	window.open(url, "post", "toolbar=no,width=550,height=400,top=400,left=300,status=yes,scrollbars=yes,menubar=no");
}
function idCheck(){
	if(regForm.guest_id.value === ""){
		alert("id를 입력하시오");
		regForm.guest_id.focus();
	}else{
		url = "idcheck.jsp?guest_id=" + regForm.guest_id.value;
		window.open(url, "id" , "width=300,height=200,top=400,left=300");
		
	}
}

function inputCheck(){
	if(regForm.guest_id.value === ""){
		alert("아이디를 입력하세요");
		regForm.guest_id.focus();
		return;
	}
	//생략...
	
	regForm.submit();
}

function productdetail(no){	//관리자에서 상품 처리 시
	//alert("번호는 " + no);
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}

function productUpdate(no){
	document.updateFrm.no.value = no;
	document.updateFrm.submit();
}

function productDelete(no){
	if(confirm('정말 삭제할가요?')){
		
		document.delFrm.no.value = no; 
		document.delFrm.submit();
	}
}

function productDetail(no){
	
}

function productDetail(no){	//관리자에서 상품 처리 시
	//alert("번호는 " + no);
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}

//Cart 처리용 

