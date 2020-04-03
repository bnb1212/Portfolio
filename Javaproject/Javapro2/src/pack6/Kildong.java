package pack6;

public class Kildong {
	
	public Saram findSaram() {
//		return new Saram();
		return new Saram()
				
		{	// 익명 (무명) 클래스 ; Anonymous Class
			int abc = 0;
			
			public void aa() {
				System.out.println("익명 클래스의 aa 메소드");
			}
			
			public String getIr() {
				String name = "홍길동 만쉐이";
				return name;
				
			}
		};
	}
}
