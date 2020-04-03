package pack1;

import java.util.Scanner;

public class Test8 {

	public static void main(String[] args) {
		// 조건판단문 switch
		int nai = 28;
		nai = nai / 10 * 10;
		System.out.println(nai);

		switch (nai) {
		case 20:
			System.out.println("이십대");
			System.out.println("인생의 황금기");
			break;
		case 30:
			System.out.println("삼십대");
			break;
		default:
			System.out.println("기타");
				
		}
		
		// 키보드로 년과 월을 입력받아 해당 년 월의 날 수 출력, 윤년 체크
		// 윤년은 해당 년이 4의 배수이고, 100의 배수가 아니거나 400의 배수이면
		
		int year, month, nalsu = 28;
		Scanner sc = new Scanner(System.in);
		System.out.println("년도 입력: ");
		year = sc.nextInt();
		System.out.println("월 입력: ");
		month = sc.nextInt();
		
		if ( month < 1 || month  > 12) {
			System.out.println("월은 1~12사이만 허용");
			System.exit(1);
		}
		
		if (year % 4 == 0 && 100 != 0 || year % 400 == 0)
			nalsu = 29;
		
		switch(month) {
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			nalsu = 31;
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			nalsu = 30;
			break;
		}
		
		System.out.println(year + "년 " + month + "월 날수는 " + nalsu );
		System.out.println("종료");
		
		
	}

}
