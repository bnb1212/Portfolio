package pack9;

public class ThreadTest2 implements Runnable {

	public ThreadTest2() {

	}

	public ThreadTest2(String name) {
		Thread tt = new Thread(this, name);
		tt.start();
	}

	@Override
	public void run() {
		for (int i = 0; i <= 50; i++) {
			System.out.print(i + "(" + Thread.currentThread().getName() + ") ");
			try {
//				Thread.sleep(100);
			} catch (Exception e) {
				// TODO: handle exception
			}

		}
	}

	public static void main(String[] args) {
//		ThreadTest2 my1 = new ThreadTest2();
//		ThreadTest2 my2 = new ThreadTest2();
////		my1.start();
//		Thread t1 = new Thread(my1, "하나");
//		Thread t2 = new Thread(my2, "둘");
//		
//		t1.start();
//		t2.start();
		new ThreadTest2("one");
		new ThreadTest2("two");
		
		System.out.println("종료");
	}
}
