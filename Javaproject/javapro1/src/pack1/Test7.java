package pack1;

import java.util.Scanner;

public class Test7 {

	public static void main(String[] args) {
		// 조건판단문 if
		int num = 5;

		if (num >= 3) {
			System.out.println("크다잉");
			System.out.println("참일 때");
		}

		num = 5;
		if (num < 3) {
			System.out.println("작군요");
			System.out.println("난 TRUE!");

		} else {
			System.out.println("작지 않아용");
		}

		System.out.println("-----------------");
		System.out.println("다중 if ");
		int jumsu = 60;
		if (jumsu >= 70) {
			if (jumsu >= 90) {
				System.out.println("우수");
			} else
				System.out.println("보통");
		} else {
			if (jumsu >= 50) {
				System.out.println("조금 부족");
			} else {
				System.out.println("저조");
			}
		}

		System.out.println();
		int jum = 75;
		String result = "평가결과: ";
		if (jum >= 90) {
			result += "수";
		} else if (jum >= 80) {
			result += "우";
		} else if (jum >= 70) {
			result += "미";
		} else if (jum >= 60) {
			result += "양";
		} else {
			result += "가";
		}
		System.out.println(result);

		// 문) 키보드로 부터 상품명, 수량, 단가 입력받아 각각 입력받아 금액(수량 * 단가)을 출력
		// 조건 : 금액이 5만원 이상이면 금액의 10%를 그 외는 금액의 5%를 세금으로 출력
		// 출력 ==> 상품명: *** 금액: *** 세금: ***

		Scanner sc = new Scanner(System.in);

		System.out.println("상품명 입력: ");
		String product = sc.next();
		System.out.println("수량 입력: ");
		int count = sc.nextInt();
		System.out.println("가격 입력: ");
		int unit_price = sc.nextInt();

		int total_price = count * unit_price;
		double tax = 0;

		if (total_price >= 50000) {
			tax = total_price / 10;
		} else {
			tax = total_price / 20;
		}

		System.out.println("상품명: " + product + " / " + "금액: " + total_price + " / " + "세금: " + tax + " ");
		System.out.println("종료");
	}

}
