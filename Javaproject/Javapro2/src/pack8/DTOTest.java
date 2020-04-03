package pack8;

import java.util.ArrayList;

public class DTOTest {
	// Data Transfer Object : 레코드형 기억장소 연습
	ArrayList<StudentDTO> list = new ArrayList<StudentDTO>();

	public void aa() {
		String[] persons = new String[3];
		persons[0] = "홍길동";
		persons[1] = "고길동";
		persons[2] = "나길동";
		for (String s : persons) {
			System.out.println(s);
		}
	}

	public void insertData() {
		// 학생들의 학번, 이름, 점수를 레코드 단위로 입력 후 기억
		StudentDTO dto = null;

		dto = new StudentDTO();
		dto.setHakbun("ks1");
		dto.setIrum("홍길동");
		dto.setJumsu(90);
		list.add(dto); // 첫번쨰 학생 자료 기억

		// list.add(dto)를 하지 않으면 덮어쓰기 당함
		dto = new StudentDTO();
		dto.setHakbun("ks2");
		dto.setIrum("고길동");
		dto.setJumsu(80);
		list.add(dto);

		dto = new StudentDTO();
		dto.setHakbun("ks3");
		dto.setIrum("신길동");
		dto.setJumsu(70);
		list.add(dto);
	}

	public void showData() {
		System.out.println("학생 수는 : " + list.size() + "명");
	    for(int i = 0; i < list.size(); i++) {
	    	StudentDTO dto = new StudentDTO();
	    	dto = list.get(i);
//	    	System.out.println(dto); dto의 주소출력
	    	System.out.println(dto.getHakbun() + " " + dto.getIrum()+ " " + dto.getJumsu());
	    	// GETTER를 이용해 뽑아 먹는당
	    	
	    }
	
	}

	public static void main(String[] args) {
		DTOTest test = new DTOTest();
		test.aa();
		test.insertData();
//		System.out.println(test.list.size()); 3
		test.showData();
	}
}
