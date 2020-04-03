var xhr;
var checkFirst = loopSend = false;

function sijak() {

	// alert('a');
	if (checkFirst === false) {
		kbs = setTimeout("sendKeyword()", 1000);
		loopSend = true;
	}
}

function sendKeyword() {
	// console.log('good');
	if (loopSend === false)
		return;

	var keyword = document.frm.keyword.value;
	// console.log(keyWord);
	if (keyword === "") {
		hide();
	} else {
		var para = "keyword=" + keyword;

		xhr = new XMLHttpRequest();
		xhr.open("post", "ajax7.jsp", true);
		xhr.onreadystatechange = function() {
			if (xhr.readyState === 4) {
				if (xhr.status === 200) {
					processPost();
				} else {
					alert('err : ' + xhr.status)
				}
			}
		}
		xhr.setRequestHeader("Content-Type",
				"application/x-www-form-urlencoded");
		xhr.send(para);
	}
}
function processPost() {
	var data = xhr.responseText;
	var result = data.split("|");

	var tot = result[0]; // 5
	if (tot > 0) {
		var datas = result[1].split(","); // 홍길동, 홍두깨, ...
		var imsi = "";
		for (var i = 0; i < datas.length; i++) {
			imsi += "<a href=\"javascript:func('" + datas[i] + "')\">"
					+ datas[i] + "</a><br>";
		}
		// alert(imsi);
	}

	var listView = document.getElementById("suggestList");
	listView.innerHTML = imsi;
	show();
}

function func(arg) {
	//alert(arg);
	frm.sel.value = arg;
	
	loopSend = checkFirst = false;
	hide();
	frm.keyword.value = "";
}

function hide() {
	document.getElementById("suggest").style.display = "none";
}

function show() {

	document.getElementById("suggest").style.display = "";
}
