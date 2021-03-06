$(document).ready(function() {
	var speech = $("div.speech");

	var defaultFsize = speech.css("fontSize");
	// alert(defaultFsize);

	$("#switcher button").click(function() { // 버튼 클릭 이벤트
		var num = parseInt(speech.css("fontSize")); // 16px -> 16
		// alert(num);

		switch (this.id) {
		case "switcher-large":
			num += 8;
			break;
		case "switcher-small":
			num -= 8;
			break;
		default:
			// num = parseFloat(defaultFsize, 10);
			// Float형으로 했을 시 10진수로 받겠다 선언하면 사용할 수 있다.
			num = parseInt(defaultFsize);
		}

		speech.animate({
			fontSize : num + 'px'
		}, 'fast'); // css대신 사용하면서 이펙트를 준다
		// fast, 1000, 2000 등의 숫자값으로도 줄 수 있다. 커질수록 빠름

	});
	// 문서의 일부를 보이기 / 숨기기
	var firstPara = $("p:eq(1)"); // 여러 p 태그 중 eq(1); 첫번째
	// :eq()를 주지 않으면 p가 여러개 이기때문에 firstPara는 배열이 된다.
	firstPara.hide(); // 숨기기
	$("a.more").click(function() {
		// alert(firstPara.is(":hidden")); // is(":hidden")으로 숨어있는지 판별; true,
		// false반환
		if (firstPara.is(":hidden")) {
			// show()는 안이쁨 ㅋㅋ 이펙트활용
			// firstPara.fadeIn("slow"); // 서서히 나타나는 이펙트 fadeIn
			firstPara.slideToggle("slow"); // 스스슥 열림 토글형식 이펙트
			$(this).text("read less"); // 하이퍼텍스트 read less로 변경
		} else {
			// firstPara.fadeOut("slow"); // 서서히 사라짐
			firstPara.slideToggle("slow");
			$(this).text("read more"); // 하이퍼텍스트 read more로 변경
		}
	});
	$('button, a.more').hover( // mouseover와 mouseout이 둘다 들어있는 기능 hover
	function() {
		$(this).addClass('myHover'); // 버튼과 링크에 myHover를 추가하고, css에서 myHover에 효과를 줌으로서 꾸밈
	}, function() {
		$(this).removeClass('myHover');
	});
});