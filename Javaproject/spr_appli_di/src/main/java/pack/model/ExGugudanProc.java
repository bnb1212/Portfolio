package pack.model;

public class ExGugudanProc implements ExGugudanInter {
	public void dispGugudan() {
		for(int i=2; i<10; i++) {
			for(int j=1; j<10; j++) {
				System.out.println(i + " x " + j + " = " + (i*j));
			}
		}
	}
}
