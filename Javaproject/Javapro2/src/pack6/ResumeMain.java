package pack6;

public class ResumeMain {
	public static void main(String[] args) {
		System.out.println("====== 톰 이력서 ==========");
		R_Tom r_Tom = new R_Tom();
		r_Tom.setIrum("김톰");
		r_Tom.setPhone("111-1111");
		r_Tom.setJuso("역삼동 123");
	
		r_Tom.print();
		
		System.out.println();
		r_Tom.playJava(false);
//		r_Tom.changeData();
		Resume.changeData();
		r_Tom.abc();
	
		System.out.println("====== 제임스 이력서 ==========");
		R_James r_James = new R_James();
		r_James.setIrum("최제임스");
		r_James.setPhone("111-1111");
		r_James.setSkill("스프링 전문가");
	
		r_James.print();
		
		System.out.println("====== 인사 담당자가 이력시 취합 후 확인 ======");
		Resume[] resBox = new Resume[2];
		resBox[0] = r_Tom;
		resBox[1] = r_James;
		
		for (Resume box:resBox) {
			box.print();
			System.out.println("========");
		}
		
	
	}
}
