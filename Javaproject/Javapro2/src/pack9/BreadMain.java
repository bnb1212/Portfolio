package pack9;

public class BreadMain {
    public static void main(String[] args) {
		// 두 개 이상의 스레드로 빵 자원을 공유
    	BreadPlate breadPlate = new BreadPlate();
    	BreadMaker maker = new BreadMaker(breadPlate);
    	BreadEater eater = new BreadEater(breadPlate);
    	
    	maker.setPriority(8);
    	
    	maker.start();
    	eater.start();
    	
	}
}
