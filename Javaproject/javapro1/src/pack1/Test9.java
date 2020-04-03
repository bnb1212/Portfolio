package pack1;

import java.util.Scanner;

public class Test9 {

	public static void main(String[] args) {
		// 반복문 for
		int a;
		int sum = 0;
		for (a = 1; a <= 1000; a += 1) {
			System.out.print(a + "\t");
			sum += a; // 누적
			// a = 7; 이러믄 안댕
		}
		System.out.println("\nfor 탈출 후 a " + a);
		System.out.println("합은 " + sum);

		System.out.println();
		for (int i = 65; i <= 90; i++) {
			System.out.print((char) i + " ");
		}

		System.out.println();
		for (int i = 'A'; i <= 'Z'; i++) {
			System.out.print(i + " ");
		}

		System.out.println();
		for (int i = 10; i > 1; i--) {
			System.out.print(i + " ");
		}

		System.out.println();
		for (int ytn = 0, tvn = 5; ytn < 5; ytn++, tvn++) {
			System.out.println(ytn + " " + tvn);
		}
		System.out.println();
		int aa = 1;
		for (; aa < 5; aa++) {
			System.out.print(aa + " ");
		}

		// 문1) 키보드로부터 숫자를 입력받아 (2 ~ 9사이만 허용) 구구단 출력
		// 2 * 1 = 2 ...

		// 문2) 1 ~ 100 사이의 숫자 중 3의 배수 이면서 5의 배수의 갯수와 그들의 합은?
		System.out.println(2);
		Scanner sc = new Scanner(System.in);
		System.out.print("문1 ) 숫자를 입력하세요: ");
		int value = sc.nextInt();

		if (value < 2 || value > 9) {
			System.out.println("입력숫자는 2~9사이만 허용");
			System.exit(1);
		}

		for (int i = 1; i <= 9; i++) {
			System.out.println(value + " * " + i + " = " + value * i);
		}
		// 여기서부터는 문2
		System.out.println();
		int sum2 = 0;
		int count = 0;
		for (int i = 1; i <= 100; i++) {
			if (i % 3 == 0 && i % 5 == 0) {
				count++;
				sum2 += i;
			}

		}
		System.out.println("1부터 100까지의 3, 5 동시 배수의 갯수는 : " + count);
		System.out.println("1부터 100까지의 3, 5 동시 배수의 합은 : " + sum2);
	}

}
