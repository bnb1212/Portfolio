package pack6;

// 내부 클래스 : 클래스의 내에 클래스를 선언
public class Outer {
	// == MEMBER ==
	private int a;
	private InnerClass inner;

	// == CONSTRUCTOR ==
	public Outer() {
		System.out.println("Outer 생성자");
		a = 10;
		inner = new InnerClass();
	}

	// == METHOD ==
	public void aa() {
		System.out.println("Outer : aa 메소드");
		bb();
		inner.cc();
		System.out.println("Outer의  a는 " + a + ", Inner의 b는 " + inner.b);

	}

	private void bb() {
		System.out.println("Outer : bb 메소드");
	}

	// 내부 클래스
	class InnerClass {
		private int b;

		public InnerClass() {
			System.out.println("Inner 생성자");
			b = 20;
		}

		public void cc() {
			System.out.println("Inner - cc method");
			System.out.println("Inner : " + b + ", Outer : " + a);
			bb();
		}

		// 내부 클래스 내의 내부 클래스 선언
		class InnerInnerClass {

		}
	}

	// =======================================
	public static void main(String[] args) {
		Outer outer = new Outer();
		outer.aa();
		System.out.println();
		// 권장 아님
//		Inner inner = new Inner();
//		Outer.InnerClass inner = outer.new InnerClass();
//		inner.cc();

	}
}
