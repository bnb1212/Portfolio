package pack.controller;

import pack.model.ExGugudanInter;
import pack.model.ExSetStudent;
import pack.model.ExStudentInter;

public class ExProcess implements ExInter {
	private ExGugudanInter inter;
	private ExStudentInter inter2;
	
	public ExProcess(ExGugudanInter inter) {
		this.inter = inter;
	}
	
	public void setExSetStudent(ExSetStudent exSetStudent) {
		this.inter2 = exSetStudent;
	}
	
	public void showStudent() {
		System.out.println("작성자의 이름은 : " + inter2.getStudent());
		inter.dispGugudan();
		
	}

}
