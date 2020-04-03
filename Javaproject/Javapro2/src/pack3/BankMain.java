package pack3;

public class BankMain {
	public static void main(String[] args) {
		// 뭔가를 하다가

		Bank tom = new Bank();
		tom.dePosit(5000);
		tom.withDraw(3000);
		System.out.println("tom의 잔고 : " + tom.getMoney());

		System.out.println("================");
		Bank oscar = new Bank(3000);
		oscar.dePosit(1000);
		oscar.withDraw(7000);
		oscar.withDraw(4000);
		System.out.println("oscar의 잔고 : " + oscar.getMoney());

		System.out.println("주소 관련 ==================");
		System.out.println("tom 주소 : " + tom);
		System.out.println("oscar 주소 : " + oscar.toString());
		System.out.println("oscar 주소 : " + oscar.hashCode());

		Bank james = null;
		System.out.println("james 주소 : " + james);
//		james.dePosit(2000); // java.lang.NullPointerException
		james = oscar;
		System.out.println("james 주소 : " + james);
		james.dePosit(2000);
		System.out.println("oscar의 잔고 : " + oscar.getMoney());
		System.out.println("james의 잔고 : " + james.getMoney());
		oscar = null;

		System.out.println("========================");
		if (james == oscar)
			System.out.println("같은 객체 주소 참조");
		else
			System.out.println("달라요");

		System.out.println();
		System.out.println("string 클래스 타입값 비교 ============");
		String ss1 = "kor";
		String ss2 = new String();
		ss2 = "kor";
		String ss3 = new String("kor");
		System.out.println(ss1 + " " + ss2 + " " + ss3);

		if (ss1 == ss2)
			System.out.println("같음1");
		else
			System.out.println("다름1");

		if (ss1.equals(ss3))
			System.out.println("같음2");
		else
			System.out.println("다름2");

		if (ss2.equalsIgnoreCase(ss3))
			System.out.println("같음3");
		else
			System.out.println("다름3");

		// 문자열 비교용 메소드 equals : String객체의 값을 비교
		// String 은 비교할떄 == 쓰면 안된다 -

		System.out.println("\n배열 관련 ==============");
		int ar1[] = { 1, 2, 3 };
		System.out.println(ar1);
		System.out.println(ar1[0] + " " + ar1[1]);
		int[][] ar2 = { { 1, 2, 3 }, { 4, 5, 6 } };
		System.out.println(ar2);
		System.out.println(ar2[0]);
		System.out.println(ar2[0][0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               );

	}
}
