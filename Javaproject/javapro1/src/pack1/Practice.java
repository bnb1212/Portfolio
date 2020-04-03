package pack1;

public class Practice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int start = 'A';
		int end = 'E';
		
		for (int i1 = start; i1 <= end; i1++) { // A ~ E 5회
			// 공백 만들기
			for (int j1 = end; j1 > i1; j1--) { // E ~ (i1) 4, 3, 2, 1
				System.out.print(" ");
			}
			// 정순 문자 출력
			for (int j1 = start; j1 <= i1; j1++) { // A ~ i1
				System.out.print((char) j1);
			}
			// 역순 문자 출력
			for (int j1 = i1; j1 >= start; j1--) {
				System.out.print((char) j1);
			}
			System.out.println();
		}

		for (int i1 = end; i1 >= start; i1--) {
			// 공백 생성
			for (int k = i1; k <= end; k++) {
				System.out.print(" ");
			}
			// 정순 출력
			for (int k = start; k < i1; k++) {
				System.out.print((char) k);
			}
			// 역순 출력
			for (int k = i1 - 1; k >= start; k--) {
				System.out.print((char) k);

			}
			System.out.println();
		}

	}

}
