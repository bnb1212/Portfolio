package pack3;

public class Programmer {
//	public String nickName = "";
	public String nickName; // 초기값은 null, 참조형임
	private int age; // 기본 자료형, 초기값은 0
	String spec = "JAVA, C, PYTHON";
	static String moto = "미치자!";
	public final static double PI = 3.14;
	
	
	public Programmer() {
		System.out.println("생성자. 생략도 가능");
		age = 20;
	}

	public void displayData() {
		String re = reSpeck();
		System.out.println("별명이 " + nickName + " " + age + "살 " + re);
	}

	private String reSpeck() {
		return "보유 기술은 " + spec;
	}
	
	public void setAge(int age) {
		this.age = age;
	}
	
	public int getAge() {
		return age;
	}

	public static void staticMethod() { // static 영역에 new 선언 전에 저장됨
//		System.out.println("age : " + age);
		System.out.println("moto : " + moto);
		
	}
}
