package pack5;

public abstract class Animal {
	// ============= METHOD ==========
	abstract public String callName();
	abstract public String eat();
	abstract public String action();
	
	protected void print() {
		System.out.println("동물 클래스의 print 일반 메소드");
		
		
	}
}
