package pack.controller;

import pack.model.SetterShowData;

public class SetterProcess { // BL
	private int nai;
	private SetterShowData setterShowData;

	public SetterProcess() {
		// TODO Auto-generated constructor stub
	}

	public void setNai(int nai) {
		this.nai = nai;
	}

	public int getNai() {
		return nai;
	}

	public void setSetterShowData(SetterShowData setterShowData) {
		this.setterShowData = setterShowData;
	}
	
	public void showData() {
		System.out.println("이름은 " + setterShowData.getName() + " " + "\n나이는 " + nai + "\n별명은 " + setterShowData.getHobby());
	}
}
