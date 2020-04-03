package pack1;

public class Test3 {

	public static void main(String[] args) {
		// 관계, 논리 연산자, 기타
		int a = 5;
		System.out.println(a > 3);
		System.out.println(a <= 3);
		System.out.println(a == 3);
		System.out.println(a != 3);

		System.out.println();
		int b = 10;
		System.out.println(a > 3 && b <= 10); // and 연산
		System.out.println(a >= 3 && b == 7);

		System.out.println(a > 6 || b <= 10); // or 연산
		System.out.println(a > 7 || b < 5 + 10); // or 연산

		System.out.println();
		int ii = 8, ij;
//		System.out.println(ii + " " + ij);
		System.out.println("ii : " + ii + " " + Integer.toBinaryString(ii));
		ij = ii << 1; // shift 연산자. 좌로 1비트 이동. 남는 우측은 0으로 채우기
		System.out.println("ij : " + ij);
		ij = ii >> 2; // shift 연산자. 우로 2비트 이동. 남는 좌측은 0으로 채우기
		System.out.println("ij ; " + ij);
		
		System.out.println();
		// 삼항연산자
		int re = ( ii > 5 )? 100 : 50 + 20;
		System.out.println("re : " + re);
		
		int x, y, z;
		x = y = z = 5;
		System.out.println(x + " " + y + " " + z);
		
		aa();
		bb(11);
		System.out.println("프로그램 종료");
		
	}
	public static void aa() { // 성격이 비슷한 명령문들을 모아놓은 집단
		System.out.println("aa 메소드 수행");
	}
	public static void bb(int mdc) {
		System.out.println("bb 메소드 처리");
		System.out.println("bb " + " bcc");
	}

}
