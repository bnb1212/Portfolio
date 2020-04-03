package Pack7;

public class A { // 바깥쪽 클래스

	int field1;
	// ==== CONSTRUCTOR ====
	public A() {
		System.out.println("A 생성자");
	}
	// ==== METHOD ====
	void method1() {
		System.out.println("메소드1 수행 : " + field1);
	}
	// ==== MEMBER CLASS ====
	
	class B { // 인스턴스 멤버 클래스
		int field2;

		public B() {
			System.out.println("B 객체 생성자");
		}

		void method2() {
			System.out.println("메소드2 수행 : " + field2);

		}
	}

	static class C { // 정적 멤버 클래스

		int field3;

		public C() {
			System.out.println("C 객체 생성자");
		}

		void method3() {
			System.out.println("메소드3 수행 : " + field3);

		}

	}

	void a_method4() { // 메소드 안에도 클래스 생성 가능
		System.out.println("a_method4가 진행");

		class D {

			int field4;

			public D() {
				System.out.println("D 생성자");
			}

			void method4() {
				System.out.println("메소드4 수행 : " + field4);
			}
		}

		D d = new D();
		d.field4 = 4;
		d.method4();
	}

	// ======= 허용 범위 ===========
	// * 테스트 케이스 
	void test1() {
		B b3 = new B(); 
		C c3 = new C();
//		D d2 = new D(); // 지역 멤버 클래스로 선언했으니 외부에서 사용 안됨
	}

	static C c4 = new C();

	static void test2() {
//			B b4 = new B(); B는 인스턴스 클래스라서 스태틱 메소드 안에 생성불가
			C c5 = new C();
		}
	// =========================
	public static void main(String[] args) {

		A a = new A();

		a.field1 = 1;
		a.method1();

		System.out.println("인스턴스 멤버 클래스========");
		A.B b = a.new B();
		b.field2 = 2;
		b.method2();

		System.out.println("정적 인스턴스 멤버 클래스 ====");
		A.C c = new A.C();
		c.field3 = 3;
		c.method3();

		C c2 = new C();
		c2.field3 = 4;
		c2.method3();

		System.out.println("로컬 클래스 멤버 ============");
		a.a_method4();

		System.out.println();
		a.test1();
		a.test2();
		A.test2();
	}

}
