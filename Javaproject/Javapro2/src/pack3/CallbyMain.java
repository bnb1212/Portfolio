package pack3;

public class CallbyMain {

	public static void main(String[] args) {
		// 메소드 호출시 매개변수 전달
		// 기본형을 매개변수로 -> 콜 바이 밸류
		// 참조형을 매개변수로 -> 콜 바이 레퍼런스 Call by reference

		Callby1 my = new Callby1();
		Callby2 your = new Callby2();

		System.out.println("원래 a값: " + my.a + ", b:" + my.b);
		your.ex(my.a, my.b);
		System.out.println("1. 수행 후 a:" + my.a + ", b:" + my.b);
		
		System.out.println();
		your.ex(my);
		System.out.println("2. 수행 후 a:" + my.a + ", b:" + my.b);
		
		System.out.println();
		your.ex(my.c);
		System.out.println("3. 수행 후 a:" + my.a + ", b:" + my.b);
	}

}
