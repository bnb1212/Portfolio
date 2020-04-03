function productDetail(no) {
	// alert("번호는 "+no);
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}

function productUpdate(no) {
	document.updateFrm.no.value = no;
	document.updateFrm.submit();

}

function productDelete(no) {
	if (confirm("정말 삭제할카요?")) {

		document.delFrm.no.value = no;
		document.delFrm.submit();
	}
}

function productDetail_g(no) {
	// alert("번호는 "+no);
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}


