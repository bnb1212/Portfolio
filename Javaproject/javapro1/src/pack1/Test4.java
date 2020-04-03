package pack1;

public class Test4 {
	public static void main(String[] args) {
		boolean a = true, b = true, c;
		c = a || b;
		System.out.println(c);
		c = a && b;
		System.out.println(c);
		
		System.out.println("------------");
		//System.out.println(aa());
		boolean b1, b2;
		b1 = aa();
		System.out.println(b1);
		System.out.println(bb());
		
		System.out.println("주의할 점 -------");
		// b2 = aa() || bb(); 
		// aa만 수행 (true이기때문에 b2가 결정됨)
		b2 = bb() || aa();
		System.out.println(b2);
		
		System.out.println();
		//b2 = aa() && bb();
		b2 = bb() && aa();
		System.out.println(b2);
		
		System.out.println("~~~~~~~~~~~~~");
		b2 = aa() | bb();
		System.out.println(b2);
		System.out.println();
		
		b2 = bb() & aa();
		System.out.println(b2);
		System.out.println("*** 종료 ***");
	}

	public static boolean aa() {
		System.out.println("aa 출력");
		return true;
	}

	public static boolean bb() {
		System.out.println("bb 수행");
		return false;
	}
}
