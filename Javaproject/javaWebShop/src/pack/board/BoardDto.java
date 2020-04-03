package pack.board;

import java.util.Calendar;

public class BoardDto { // DTO. Business Logic에서 사용
	//	레코드 단위의 처리 목적
	
	private String name, pass, mail, title, cont, bip, bdate;
	private int num, readcnt, gnum, onum, nested;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPass() {
		return pass;
	}
	public void setPass(String pass) {
		this.pass = pass;
	}
	public String getMail() {
		return mail;
	}
	public void setMail(String mail) {
		this.mail = mail;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getCont() {
		return cont;
	}
	public void setCont(String cont) {
		this.cont = cont;
	}
	public String getBip() {
		return bip;
	}
	public void setBip(String bip) {
		this.bip = bip;
	}
	public String getBdate() {
		return bdate;
	}
	public void setBdate(String bdate) {
		this.bdate = bdate;
	}

	
	public int getNum() {
		return num;
	}
	public void setNum(int num) {
		this.num = num;
	}
	public int getReadcnt() {
		return readcnt;
	}
	public void setReadcnt(int readcnt) {
		this.readcnt = readcnt;
	}
	public int getGnum() {
		return gnum;
	}
	public void setGnum(int gnum) {
		this.gnum = gnum;
	}
	public int getOnum() {
		return onum;
	}
	public void setOnum(int onum) {
		this.onum = onum;
	}
	public int getNested() {
		return nested;
	}
	public void setNested(int nested) {
		this.nested = nested;
	}

	
	/*
	| num     | int(5)      | NO   | PRI | NULL    |       |
	| name    | varchar(20) | NO   |     | NULL    |       |
	| pass    | varchar(20) | NO   |     | NULL    |       |
	| mail    | varchar(30) | YES  |     | NULL    |       |
	| title   | varchar(50) | YES  |     | NULL    |       |
	| cont    | text        | YES  |     | NULL    |       |
	| bip     | varchar(20) | YES  |     | NULL    |       |
	| bdate   | varchar(20) | YES  |     | NULL    |       |
	| readcnt | int(3)      | YES  |     | NULL    |       |
	| gnum    | int(5)      | YES  |     | NULL    |       |
	| onum    | int(3)      | YES  |     | NULL    |       |
	| nested  | int(3)      | YES  |     | NULL    |       |
	*/
}
