package pack3;

// method overloading(메소드 재명명) : 동일한 이름의 메소드를 여러 개 선언 가능(단, 조건 O)
public class Animal {
	private int leg = 4;
	private int age;
	private String name;
	public final static int MOUTH = 1;
	
	public Animal() {
		//생성자는 내용이 없을 경우 생략 가능.(컴파일러가 만들어 준다 고마워 컴파일러!)
		
	}
	
	public Animal(int leg) { // 생성자 오버로딩
		this.leg = leg;
	}
	
	public Animal(String irum) { // 생성자 오버로딩
		name = irum;
	}
	
	
	
	public void display() {
		System.out.println("leg : " + leg + ", age: " + age + ", name: " + name );
	}
	
	public void display(int age) { // 메소드 오버로딩 : 인자의 갯수가 다름
		this.age = age;
		System.out.println("leg : " + leg + ", age: " + age + ", name: " + name );	
		}
	
	public void display(String name) { // 인자의 type 다름
		this.name = name;
		System.out.println("leg : " + leg + ", age: " + age + ", name: " + name );
	}
	public void display(String name, int nai) { // 인자의 type 다름
		this.name = name;
		age = nai;
		System.out.println("leg : " + leg + ", age: " + nai + ", name: " + name );
	}
	public void display(int nai, String name) { // 인자의 type 다름, 순서 바뀌어도 노상관
		this.name = name;
		age = nai;
		System.out.println("leg : " + leg + ", age: " + nai + ", name: " + name );
	}
	
}
