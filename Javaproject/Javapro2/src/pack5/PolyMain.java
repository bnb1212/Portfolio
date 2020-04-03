package pack5;

public class PolyMain {
	
	public static void main(String[] args) {
		
		PolyCar car1 = new PolyCar();
		car1.dispData();
		
		System.out.println();
		PolyBus bus1 = new PolyBus();
		bus1.dispData();
		bus1.show();
		
		System.out.println();
		PolyTaxi taxi1 = new PolyTaxi();
		taxi1.dispData();
		taxi1.show();
		
		System.out.println("==============");
		PolyCar car2 = new PolyBus(); // promotion
		car2.dispData(); 
		System.out.println(car2.getSpeed());
//		car2.show(); // 오버라이딩된 메소드만 호출 가능. 불간섭의 원칙. car2는 자식타입(PolyBus)의 메소드를 부를수 없다
		
		System.out.println();
		PolyCar	car3 = new PolyTaxi();
		car3.dispData();
		
		System.out.println("****************");
//		PolyBus bus2 = new PolyCar(); // 큰타입(부모)의 주소는 작은타입(자식)의 주소에 할당할수 없음
		PolyBus bus2 = (PolyBus)car2; // casting!
		bus2.dispData();
		bus2.show();
		
		
		System.out.println();
		PolyTaxi taxi2 = (PolyTaxi)car3;
//		PolyTaxi taxi3 = (PolyTaxi)car1; // 문법오류 X, 실행오류:ClassCastException
	
	
		System.out.println("#################");
		PolyCar p[] = new PolyCar[3];
		p[0] = car1;
		p[1] = bus1;
		p[2] = taxi1;
		for (int i = 0; i < p.length; i++) {
			p[i].dispData();
		}
		
		System.out.println();
		for(PolyCar car:p) {
			car.dispData();
		}
		}
}
