package pack6;

public interface Resume {
	// 인터페이스의 멤버변수는 public final static이 붙어 있는 거나 마찬가지
	String SIZE = "A4";
	
	void setIrum(String irum);
	void setPhone(String phone);
	void print();
	
	default void playJava(boolean b) {
		if(b) {
			System.out.println("자바 프로그래밍 가능");
		}else {
			System.out.println("자바 불가능");
		}
	}
	
	static void changeData() {
		System.out.println("스태틱 메소드 처리가능");
	}
}
