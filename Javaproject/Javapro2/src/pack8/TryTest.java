package pack8;

import java.io.FileNotFoundException;
import java.io.FileReader;

// 예외 처리 : 외부장치( 키보드, 파일처리, DB작업, 네트워크 등등 )와 연결해 작업시 반드시 기술.
// 그 외에는 선택적으로  기술

public class TryTest {

	public void test() {
		try {

			int a[] = { 1, 2, 3 };
//			System.out.println("배열 값 : " + a[0]);
			System.out.println("배열 값 : " + a[5]);

		} catch (Exception e) {
			System.out.println("허걱 에러 : " + e); // 지역 우선 에러 체크 (전역-main보다 우선)
		}
	}

//	public static void main(String[] args) throws Exception{
	public static void main(String[] args) {
//		FileReader fr = new FileReader("c:/work/aa.txt");
//		FileReader fr = new FileReader("c:\\work\\aa.txt");
		try {
			FileReader fr = new FileReader("c:\\work\\aa.txt");
			int re = 10 / 2;

			System.out.println("re : " + re);

			TryTest tt = new TryTest();
			tt.test();

//		} catch (FileNotFoundException e) {
//			System.out.println("파일 오류");
//		} catch (ArithmeticException e) {
//			e.printStackTrace();
//			System.out.println("나누기 에러 : " + e.getMessage());
//		} catch (NullPointerException e) {
//			System.out.println("객체 오류");
//		} catch (ArrayIndexOutOfBoundsException e) {
//			System.out.println("배열 참조 오류 : " + e);
//		}
		} catch (Exception e) {
			System.out.println("오류 : " + e); // 모든 에러메세지를 다 받음
		}									 // 다른 에러를 받는 구문을 표기하면 그 catch 구문을 우선 실행
		System.out.println("종료");
	}
}
