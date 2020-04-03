package pack8;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Quiz2_2Main {
	// ==== MEMBER ====
	ArrayList<Quiz2_2Dto> list;

	// ==== CONSTRUCTOR ====
	public Quiz2_2Main() {
		list = new ArrayList<Quiz2_2Dto>();
	}

	// ==== METHOD ====
	public void insertData() {
		Scanner sc = new Scanner(System.in);
		boolean flag = true;

		while (flag) {
			String jungbo;

			System.out.println("지역코드, 상품명, 수량 입력 (콤마로 구분)");
			jungbo = sc.nextLine();
			// 구분
			StringTokenizer tok = new StringTokenizer(jungbo, ",");
			int areacode = Integer.parseInt(tok.nextToken());
			String product = tok.nextToken();
			int amount = Integer.parseInt(tok.nextToken());
			// 저장
			Quiz2_2Dto dto = new Quiz2_2Dto();
			dto.setAreacode(areacode);
			dto.setProduct(product);
			dto.setAmount(amount);
			list.add(dto);
			// 계속할지 묻기
			while (true) { 
				System.out.println("계속 할까요?(y/n)");
				String ch = sc.nextLine();

				if (ch.equals("y"))
					break;
				else if (ch.equals("n")) {
					System.out.println("=========== 보고 ==============");
					flag = false;
					break;

				} else {
					System.out.println("y 또는 n을 입력해야 합니다.");
					continue;
				}
			}

		}
		sc.close();
	}

	public void showData() {
		int saewoo = 0;
		int s_total = 0;
		int gamja = 0;
		int g_total = 0;

		System.out.println("지역\t상품명\t수량\t단가\t금액");
		for (int i = 0; i < list.size(); i++) {
			Quiz2_2Dto dto = new Quiz2_2Dto();
			dto = list.get(i);

			if (dto.getAreacode() == 100)
				System.out.print("강북\t");
			else if (dto.getAreacode() == 200)
				System.out.print("강남\t");
			else if (dto.getAreacode() == 300)
				System.out.print("강서\t");
			else
				System.out.print("기타\t");

			System.out.print(dto.getProduct() + "\t");
			System.out.print(dto.getAmount() + "\t");

			if (dto.getProduct().equals("새우깡")) {
				System.out.print("450\t" + (dto.getAmount() * 450) + "\n");
				saewoo++;
				s_total += (dto.getAmount() * 450);
			} else {
				System.out.print("300\t" + (dto.getAmount() * 300) + "\n");
				gamja++;
				g_total += (dto.getAmount() * 300);
			}
		}
		System.out.println();
		System.out.println("===== 소계 ===== ");
		System.out.println("감자깡 : " + gamja + "건\t소계액 : " + g_total + "원");
		System.out.println("새우깡 : " + saewoo + "건\t소계액 : " + s_total + "원");
		System.out.println("총 건수 : " + list.size() + "건\t총액 : " + (g_total + s_total));
	}

	// ==== Main ====
	public static void main(String[] args) {
		Quiz2_2Main ma = new Quiz2_2Main();
		ma.insertData();
		ma.showData();
	}

}
