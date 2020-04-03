package pack3;

public class ProMain {
	public static void main(String[] args) {
		System.out.println("뭔짓을 하다가... ");
		
		Programmer tom = new Programmer(); // 생성자를 안부르면서 객체를 만드는 방법은 자바에선 없.다.
//		tom.Programmer(); 이건 안됨
		System.out.println("tom : " + tom.spec);
		tom.displayData();
		tom.nickName = "자바도사";
		tom.displayData();
		tom.setAge(28);
		tom.displayData();
		System.out.println("나이는 " + tom.getAge());
		System.out.println(Programmer.moto);
//		tom.pi = 10;
		System.out.println(tom.PI);
		System.out.println(Programmer.PI);
		Programmer.staticMethod(); // 클래스 이름으로 참조할때는 스태틱메소드/스태틱변수인 경우
		
		System.out.println("----------------");
		Programmer oscar = new Programmer();
		oscar.displayData();
//		oscar = null;
//		oscar.displayData();
		oscar.setAge(33);
		oscar.displayData();
	}
}
