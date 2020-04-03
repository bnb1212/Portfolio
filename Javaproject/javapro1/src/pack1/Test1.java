package pack1;

public class Test1 {
	public static void main(String ar[]) {
		System.out.println("성공");
		System.out.println(10 + 20); // 한 줄 주석
		/*
		 * 여러줄 주석
		 * 
		 * 주석을 열심히 잘 달자
		 * 
		 */
		System.out.println("a");
		System.out.print("b");
		System.out.println("c");

		// 변수 : 기억장소의 이름 - 기본형

		byte var1 = 10; // 1byte 정수 기억
		var1 = 20;
		System.out.println(var1);
		System.out.println(Byte.MAX_VALUE);
		System.out.println(Byte.MIN_VALUE);

		short var2 = 20;
		System.out.println("var2 : " + var2);
		// 2byte 정수 기억 ~32768 ~ 32767

		int var3 = 2147483647;
		System.out.println("var3 : " + var3);
		// 4byte 정수 기억

		long var4 = 314783647L;
		System.out.println(Long.MAX_VALUE);
		System.out.println("var4 : " + var4);
		// 8바이트 정수 기억 -9223372036854775808 ~ 9223372036854775807
		// promotion : 자동 형 변환, cast : 강제 형변환
		byte b1 = 12;
		// 12는 정수형이지만 자동 형변환(promotion)이 일어나 byte에 들어감
		byte b2 = (byte) 128;
		// byte 형이라 127까지만 가능하지만 강제로 형변환(cast)
		System.out.println("b1 : " + b1);
		System.out.println("b2 : " + b2);

		b2 = 10;

		short s1 = 10;
		int i1 = s1; // promotion
		System.out.println("i1 : " + i1);

		System.out.println();
		System.out.println("\n실수처리 --------");

		double d1 = 10.5;
		d1 = 5;
		System.out.println("d1 : " + d1);
		// 실수의 기본은 double

		float f1 = (float) 4.5;
		System.out.println("f1 : " + f1);
	
		int i2 = (int) 4.5 + 10;
		System.out.println("i2 : " + i2);

		System.out.println();
		boolean bu = true;
		bu = false;
		System.out.println("bu : " + bu);

		System.out.println();
		char c1 = 'a';
		System.out.println("c1 : " + c1 + (int) c1 + " " + (char) 8);

		System.out.println("안녕" + "\n" + "반가워");
		System.out.println("안녕" + (char)10 + "반가워");
		
		System.out.println(0xa); // hex 16진수
		System.out.println(0xf);
		System.out.println(05); // octal 8진수
		System.out.println(052);
		
		
		// 참조형 
		String irum = "홍길동";
		System.out.println(irum);
	}
}
