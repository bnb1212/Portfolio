package pack1;

public class Test2 {

	public static void main(String[] args) {
		// 연산자
		// 우선순위 () > 산술 ( *, /, > +, -) > 관계 > 논리 > =
		// 산술연산자
		// bcbsil boolean char byte short int long

		int a = 5; // 치환
		int b = 3;

		System.out.println(a + b);
		System.out.println(a / b);
		System.out.println(a % b);
		System.out.println(a / (double) b);
		System.out.println(a / 0.0);
		System.out.println(a % 0.0);
		System.out.println(0 / 0.0);

		System.out.println(3 + 4 * 5);
		System.out.println((3 + 4) * 5);

		// 참조형
		System.out.println();
		String ss1 = "대한";
		String ss2 = "민국";
		String ss3 = ss1 + ss2;
		System.out.println("ss3 : " + ss3);
		System.out.println("ss3 : " + ss3 + "2010");
		System.out.println("ss3 : " + ss3 + 2010);
		System.out.println("ss3 : " + ss3 + Integer.toString(2010));
		System.out.println(10 + 20);
		System.out.println(10 + "20");
		System.out.println(10 + Integer.parseInt("20"));

		System.out.println();
		// 누적
		int no = 1;
		no = no + 1;
		no += 1;
		no++; // 증감연산 (++, --)
		++no; // 전위증감연산 파이썬에선 못씀
		System.out.println("no : " + no);

		// 증감 연산자
		int imsi = 5;
		int result = ++imsi + 1;
		System.out.println(imsi + " " + result);

		int imsi2 = 5;
		int result2 = imsi2++ + 1;
		System.out.println(imsi2 + " " + result2);
		// 증감연산은 다른 연산과 함께 하지 마라 ( 가독성 박살남 )

		int imsi3 = 3;
		System.out.println(imsi3);
		System.out.println(-imsi3);
		System.out.println(-imsi3 * -1);
		System.exit(0);

	}

}
