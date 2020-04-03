package pack5;

public class DogMain {

	public static void main(String[] args) {

		Dog dog = new Dog();
		dog.print();
		System.out.println(dog.callName());

		System.out.println("================");
		HouseDog houseDog = new HouseDog("집개");
		houseDog.print();
		houseDog.show();
		System.out.println(houseDog.callName());

		System.out.println("=================");
		WolfDog wolfDog = new WolfDog("늑대");
		wolfDog.print();
		wolfDog.show();
		System.out.println(wolfDog.callName());

		System.out.println("=================");
		WolfDog bushDog = wolfDog;
		bushDog.print();

		System.out.println();
		Dog dog2 = wolfDog; // 타입은 부모타입의 객체 변수이지만
		dog2.print(); // 자식의 주소를 갖고 있기 때문에 자식클래스에서 메소드를 따온다 ( promotion이 이루어짐) 
							// 자식타입의 객체 변수의 주소를 부모타입의 객체 변수에 주고, 부를때는 자식타입의 메소드를 부른다
		// dog2.display()  => 호출 불가능. 자식 고유의 메소드는 호출 불가능함. 불간섭의 원칙
		// promotion이 일어났을때 , 부모타입의 객체변수에 자식타입의 객체를 할당 받았을때 오버라이딩된 메소드만 호출가능하다
		
		// bushDog = dog2; // wolfDog을 받은 dog2(부모)를 bushdog에 줄수 없었음
							// 부모타입의 개체는 자식타입에 넣을순 없음. 하.지.만.
		//==========================================================//
		bushDog = (WolfDog)dog2; // casting을 한다면 가능하다! 
								 //부모타입의 객체변수가 자식타입의 객체주소를 할당받았을때.
		bushDog.print();
		
		System.out.println("==========================");
		Dog coyote = new Dog("코요테");
		coyote.print();
		coyote = bushDog;
		coyote.print();
		coyote = houseDog;
		coyote.print();
		
	}
}
