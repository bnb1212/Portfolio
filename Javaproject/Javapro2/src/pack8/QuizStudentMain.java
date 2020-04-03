package pack8;

import java.util.ArrayList;
import java.util.Scanner;

public class QuizStudentMain {

	ArrayList<QuizStudentDto> list = new ArrayList<QuizStudentDto>();

	public void insertData() {
		Scanner sc = new Scanner(System.in);
		boolean flag = true;

		while (flag) {
			QuizStudentDto dto = null;

			dto = new QuizStudentDto();
			System.out.print("이름 입력 : ");
			dto.setName(sc.next());
			System.out.print("국어 점수 : ");
			dto.setKor(sc.nextInt());
			System.out.print("영어 점수 : ");
			dto.setEng(sc.nextInt());
			list.add(dto);

			System.out.println();
			while (true) {
				System.out.println("계속할까요?(y/n)");
				String c = sc.next();

				if (c.equals("y"))
					break;
				else if (c.equals("n")) {
					System.out.println("입력 종료");
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
		System.out.println("이름\t국어\t영어\t총점");

		for (int i = 0; i < list.size(); i++) {
			QuizStudentDto dto = new QuizStudentDto();

			dto = list.get(i);

			System.out.println(
					dto.getName() + "\t" + dto.getKor() + "\t" + dto.getEng() + "\t" + (dto.getKor() + dto.getEng()));
		}
		System.out.println("응시인원 " + list.size() + "명");
	}

	public static void main(String[] args) {

		QuizStudentMain quiz = new QuizStudentMain();
		quiz.insertData();
		quiz.showData();
	}

}
