function zipCheck() {
	url = "zipcheck.jsp?check=y";
	window
			.open(
					url,
					"post",
					"toolbar=no, width=400, height=400, top=400, left, status, scrollbars=yes, menuber=no");
}

function idCheck() {
	if (regForm.id.value === "") {
		alert("id를 입력하시오");
		regForm.id.focus();
	} else {
		url = "idcheck.jsp?id=" + regForm.id.value;
		window.open(url, "id", "width=300, height=200, top=400, left=300");
	}
}

function inputCheck() {
	if (regForm.id.value === "") {
		alert("id를 입력하시오");
		regForm.id.focus();
		return;

		// 생략 ...

	}
	if (regForm.job.value === "0") {
		alert("직업을선택하시오");
		regForm.job.focus();
		return;
	}
	regForm.submit();
	
}

