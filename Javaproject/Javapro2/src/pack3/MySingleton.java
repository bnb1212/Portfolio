package pack3;

import java.util.Calendar;

public class MySingleton {
	int kor = 10;
	// ...

	private static MySingleton singleton = new MySingleton();
	// 내부에서 객체 생성
	public static MySingleton getInstance() {
		return singleton;
	}
	// 내부에서 만든 객체에 public 메소드로 접근할 수 있도록 함
	

	Calendar cal = Calendar.getInstance();

}
