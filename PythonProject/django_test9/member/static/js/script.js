window.onload = function(){
	document.getElementById("btnZip").onclick = zipCheck;
	document.getElementById("btnId").onclick = idCheck;
	document.getElementById("btnSubmit").onclick = inputCheck;
}

function zipCheck(){
	url = "/member/zipcheck?check=y"
	window.open(url, "zip", "toolbar=no, width=500, height=600, top=200, left=300")
}

function idCheck(){
	if(regForm.memid.value ===""){
		alert('회원 id 입력')
		regForm.memid.focus()
	} else{
		url = '/member/idcheck?memid='+ regForm.memid.value
		window.open(url, "memid", "toolbar=no, width=300, height=150, top=200, left=300")
	}
	
}

// 주소창 채우기
function send(zipcode, a1, a2, a3, a4){
	opener.document.regForm.zipcode.value = zipcode
	if(a4 === "None") a4 = "";
	var addr = a1 + ' ' + a2 + ' ' + a3 + ' ' + a4
	opener.document.regForm.address.value = addr
	window.close() // 검색창 닫기  
}

// 입력 검사 
function inputCheck(){
	if(regForm.memid.value ===""){
		alert("회원 id 입력")
		regForm.memid.focues()
		return
	}
	
	//비밀번호 입력
	if(regForm.passwd.value ===""){
		alert("비밀번호 입력")
		regForm.passwd.focues()
		return
	}
	
	//비밀번호 재확인 입력
	if(regForm.passwd.value !== regForm.repasswd.value){
		alert("비밀번호 불일치")
		regForm.repasswd.focues()
		return
	}
	
	// 생략 ...
	
	regForm.submit()
}