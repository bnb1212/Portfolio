package pack.business;

public class DataFormBean {
	private String id, name, passwd, aa, bb, cc;
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPasswd() {
		return passwd;
	}
	public void setPasswd(String passwd) {
		this.passwd = passwd;
	}
	public String getAa() {
		return aa;
	}
	public void setAa(String aa) {
		this.aa = aa;
	}
	public String getBb() {
		return bb;
	}
	public void setBb(String bb) {
		this.bb = bb;
	}
	public String getCc() {
		return cc;
	}
	public void setCc(String cc) {
		this.cc = cc;
	}
	public String getColname() {
		return colname;
	}
	public void setColname(String colname) {
		this.colname = colname;
	}
	private String colname; // sql문의 조건
	
}
