function chkData() {
	// alert('aa');
	if (frm.name.value === "" || isNaN(frm.name.value) == false) {
		frm.name.focus();
		alert("이름을 입력하시오(문자로)");
		return;
	}

	if (frm.id.value.length < 2) {
		frm.id.focus();
		alert("id는 2자 이상");
		return;
	}
	/*
	 * if((frm.email.value.indexOf("@") === -1) || (frm.email.value.indexOf(".")
	 * === -1)){ frm.id.focus(); alert("email을 정확히 입력!"); return; }
	 */

	// 정규 표현식(Regular Expression)
	var regExp = /[0-9a-zA-Z][_0-9a-zA-Z-]*@[_0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$/;
	if (!frm.email.value.match(regExp)) {
		frm.email.focus();
		alert("email을 정확히 입력!");
		return;
	}

	var regExp2 = /^[0-9]{1,2}$/;
	if (!frm.age.value.match(regExp2)) {
		frm.age.focus();
		alert("나이는 숫자 입력!");
		return;
	}

	frm.action = "js11form.jsp";
	frm.method = "post";

	frm.submit();
}

function clsData() {
	// alert('bb');
	frm.name.focus();
}

function maxLengthCheck(object) {
	if (object.value.length > object.maxLength) {
		object.value = object.value.slice(0, object.maxLength);
	}
}