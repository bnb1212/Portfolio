package pack3;

public class MySingtonMain {
	
	public static void main(String[] args) {
		// 객체를 new 하더라도 매번 객체가 만들어지지 않도록 할 경우 Singleton 패턴을 이용한다.
		MySingleton s1 = new MySingleton();
		MySingleton s2 = new MySingleton();
		System.out.println(s1 + " " + s2);
		
		s1.kor = 80;
		s2.kor = 100;
		System.out.println(s1.kor + " " + s2.kor);
		
		System.out.println();
		MySingleton s3 = MySingleton.getInstance();
		MySingleton s4 = MySingleton.getInstance();
		
		System.out.println(s3 + " " + s4);
		s3.kor = 88;
		System.out.println(s3.kor + " " + s4.kor);
	}
}
