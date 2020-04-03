package pack3; // package명 : 성격이 비슷한 클래스들을 저장한 폴더명

// 접근 지정자 - public, protected, default, private
public class Car { // 접근 지정자 Class 클래스명(대문자로 시작하고 source 파일명과 일치)
	// 멤버 필드(전역 변수) : 속성(특성, 구성 요소)
	int wheel; // default type name; - 현재 패키지 내에서 호출 가능
	private int airBag = 1; // private : 캡슐화 - 현재 클래스 내에서만 호출 가능
	private int speed;
	public String irum; // 현재 프로젝트 내에서 호출 가능

	// 생성자 (특별한 메소드로 객체 생성시 초기화를 담당) -> 메우 중요함
	public Car() {
		System.out.println("난 생성자!");
		speed = 10;
		irum = "홍길동";

	}

	// 멤버 메소드
	public void abc() {
		int aa; // 지역변수는 초기화를 해줘야 한다 전역변수는 자동으로 0 할당
		System.out.println("abc 수행 : speed => " + speed);
		abc2(); // 메소드는 메소드를 부를수 있다
		String result = abc3(7);
		System.out.println("result : " + result);
	}

	private void abc2() {
		System.out.println("abc2 수행");
	}

	String abc3(int num) {
		int local = num + 3; // local은 지역변수 : 초기화 필요
		System.out.println("abc3 수행");
		System.out.println("num : " + num);
		return "반환된 값은 " + (local * 10);

	}
	// 인자(인수, argument, parameter)가 있는 메소드

//	public int getAirBag() { // private 멤버 변수 처리용(출력) getter
////		System.out.println("airBag : " + airBag);
//		return airBag;
//	}

	public int getAirBag() {
		return airBag;
	}

	public void setAirBag(int pwd, int airBag) { // private 멤버 변수 값 주입용(입력) setter
		if (pwd == 123) {
			this.airBag = airBag;
		}
	}
}
