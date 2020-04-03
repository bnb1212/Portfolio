package pack3;

public class MyMain {

	public static void main(String[] args) {
		// 응용 프로그램이 시작
//		int kbs = 9;
//		System.out.println("kbs : " + kbs);
		
		Car mycar1 = new Car();
//		Car mycar1 = null;
		System.out.println(mycar1.wheel);
		mycar1.abc();
		// mycar1.airBag; // private 멤버이므로 접근 불가
		int air = mycar1.getAirBag();
		System.out.println("air : " + air);
		System.out.println("air : " + mycar1.getAirBag());
//		mycar1.airBag = 4;
		mycar1.setAirBag(111, 4);
		System.out.println("air : " + mycar1.getAirBag());
	}
}
