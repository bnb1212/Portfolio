package pack9;

public class ThreadTest1 extends Thread { 
	public ThreadTest1() {

	}

	public ThreadTest1(String name) {
		super(name);
	}

	@Override
	public void run() { // Thread 클래스 상속 받아 run() override
		for (int i = 0; i <= 50; i++) {
			System.out.print(i + "(" + super.getName() + ") ");
			try {
//				Thread.sleep(100);
			} catch (Exception e) {
				// TODO: handle exception
			}
		
		}
	}

	public static void main(String[] args) {
		// 메인(Demon) 스레드에 의해 main() 수행
		try {
			// process 단위 수행
//			Process p1 = Runtime.getRuntime().exec("calc.exe");
//			Process p2 = Runtime.getRuntime().exec("notepad.exe");
//			p1.waitFor(); // 자신은 정상종료. 다른 프로세스는 비정상 종료
//			p2.destroy();

			// thread로 메소드 단위 수행
//			ThreadTest1 t1 = new ThreadTest1();
//			ThreadTest1 t2 = new ThreadTest1();
//			t1.run();
//			System.out.println();
//			t2.run();
			
//			ThreadTest1 t1 = new ThreadTest1();
//			ThreadTest1 t2 = new ThreadTest1();
			ThreadTest1 t1 = new ThreadTest1("일"); // 데몬, 1, 2 해서 쓰레드 3개
			ThreadTest1 t2 = new ThreadTest1("둘");
//			t1.run() // 스레드는 이런식으로 부르지 않음
			t1.start();
			t2.start();
			t2.setPriority(MAX_PRIORITY); // t2에게 우선 순위를 요청
			t1.join(); // join() : 사용자 스레드가 종료될 때까지 메인 스레드를 대기
			t2.join(); 
			
			System.out.println("프로그램 종료");
			// 메인이 끝나도 스레드가 안끝나는 경우도 있음 -> 응용프로그램이 끝나면 스레드도 꺼져야 하는데 안꺼지는 경우
			// 							   -> 느려짐. 이런걸 조심해야함
			// 스레드는 잘만 쓰면 효과적이지만 이런 점을 주의해야 한다
			
		} catch (Exception e) {
			System.out.println("err : " + e);
		}

	}
}
