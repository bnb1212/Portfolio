package pack8;

public class Quiz2_1Dto {

	private String name, num, salary, year;

	Quiz2_1Dto(String num, String name, String salary, String year) {
		this.num = num;
		this.name = name;
		this.salary = salary;
		this.year = year;
	}
	public Quiz2_1Dto() {
		// TODO Auto-generated constructor stub
	}

	public String getNum() {
		return this.num;
	}

	public String getSalary() {
		return this.salary;
	}

	public String getyear() {
		return this.year;
	}

	public String getName() {
		return this.name;
	}

}
