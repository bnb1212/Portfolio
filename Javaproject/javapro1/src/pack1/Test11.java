package pack1;

import java.util.Scanner;

public class Test11 {

	public static void main(String[] args) {
		// 반복문 while
		int w = 1;

		while (w <= 5) { // 조건이 참이면 반복 실행하므로 루프를 멈출 state가 꼭 필요하다
			System.out.print("w: " + w + " ");
			w++; // 반복문 탈출 문장(state)이 반드시 필요
		}
		System.out.println("\n반복문 탈출 후 w : " + w);

		System.out.println();
		w = 0;
		while (true) {
			++w;
			if (w == 10)
				break;
			if (w == 5)
				continue;
			System.out.print("w=" + w + " ");
		}
		System.out.println();

		w = 10;
		do {
			System.out.println("w=" + w + " ");
			w++;
		} while (w <= 5);

		System.out.println();

		// 문1 ) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고 합과 갯수를 출력

		int i = 1;
		int count = 0;
		int sum1 = 0;
		System.out.println("****** 문1 ******");
		while (i < 101) {
			if (i % 3 == 0 && i % 2 != 0) {
				count += 1;
				sum1 += i;
			}
			i++;
		}
		System.out.println("합: " + sum1);
		System.out.println("갯수: " + count);
		System.out.println();

		// 문2) -1, 3, -5, 7, -9, -11 ~ 99까지의 합
		System.out.println("****** 문2 ******");
		int j = -1;
		int sum2 = 0;
		int abs_j = 1;

		while (abs_j < 100) {
			sum2 += j; // 일단 j를 합에 더함

			if (j < 0) { // j가 음수라면 -2
				j += -2;
				j = -j;
			} else { //
				j += 2;
				j = -j;
			}
			abs_j += 2;

			System.out.println("중간합: " + sum2);
		}
		System.out.println("합: " + sum2);
		System.out.println();

		// 문3) 1 ~ 1000 사이의 소수와 그 갯수를 출력
		System.out.println("****** 문3 ******");
		int count2 = 0;
		int check = 0;

		for (int x = 2; x <= 1000; x++) { // 1은 소수가 아니므로 2부터 시작
			check = 0; // check 초기화
			for (int y = 2; y < x; y++) {
				if (x % y == 0) { // 나누어 떨어지면 소수가 아님
					check++; // check를 늘림
					break;
				}
			}

			if (check == 0) { // check 한번도 체크가 안늘었다면 소수임
				System.out.print(String.format("%3d\t", x));
				count2++;
				if (count2 % 6 == 0) {
					System.out.println();
				}
			}
		}
		System.out.println();
		System.out.println("소수의 개수 : " + count2);

		// 소수 : 1보다 크고 1과 그 수 자체로만 나누어 떨어지는 수
		// 방법1 : while 방법2: for
		// 문4)
		/*
		 * AA ABBA ABCCBA ABCDDCBA ABCDEEDCBA
		 * 
		 */
		System.out.println();
		System.out.println("****** 문4 ******");
//		int start = 65; // A
//		int end = 69; // E
//		
//		//상단
//		for (int i1 = start; i1 <= end; i1++) {
//			// 공백 생성
//			for (int j1 = end; j1 > i1; j1--) {
//				System.out.print(" ");
//			}
//			// 정순 출력
//			for (int j1 = start; j1 <= i1; j1++) {
//				System.out.print((char) j1);
//			}
//			// 역순 출력
//			for (int j1 = i1; j1 >= start; j1--) {
//				System.out.print((char) j1);
//			}
//			System.out.println();
//		}
//		
//		// 하단
//		for (int i1 = end; i1 >= start; i1--) { // E ~ A 69 to 65
//			for (int k = i1; k < end; k++) {
//				System.out.print(" ");
//			}
//			for (int k = start; k <= i1; k++) {
//				System.out.print((char) k);
//			}
//			for (int k = i1; k >= start; k--) {
//				System.out.print((char) k);
//			}
//			System.out.println();
//		}
		

//강사님 방식
		for (int a = 5; a >= -5; a--) {
		if (a != 0) {
			System.out.println();
			int atemp = 0;
			if (a < 0)
				atemp = a * -1;
			else
				atemp = a;

			for(int b = 1; b < atemp; b++) {
				System.out.print(" ");
			}

			for(int c = 1; c <= 6 - atemp; c++) {
				char ch = 'A';
				System.out.print((char)(ch + c - 1));
			}
			
			for(int c = atemp; c <= 5; c++) {
				char ch = 'E';
				System.out.print((char)(ch - (c - 1)));
			}
		}
	}
		
		// 문5) 키보드로 숫자 입력 후 그 숫자까지의 합을 출력
		// 계속할까요?(y/n) 묻게하고 y면 다시 키보드로 정수 받아 합 출력하고 n이면 탈출

		System.out.println();
		System.out.println("****** 문5 ******");

		Scanner sc = new Scanner(System.in);

		while (true) {
			System.out.print("숫자를 입력하세요 : ");
			// 변수
			int num = sc.nextInt();
			int q5_sum = 0;
			// 정수합 구하는 for
			for (int q5_k = 1; q5_k <= num; q5_k++) {
				q5_sum += q5_k;
			}
			System.out.println("입력한 정수의 합 : " + q5_sum);
			System.out.println("-------------");
			// 재질문
			System.out.println("계속할까요? (y/n)");
			char q5_ans = sc.next().charAt(0);
			if (q5_ans == 'y')
				continue;
			else if (q5_ans == 'n') {
				System.out.println("프로그램 종료");
				break;
			} else {
				System.out.println("y나 n을 입력하세요. 프로그램 종료");
				System.exit(1);
			}
		}
	}
}
