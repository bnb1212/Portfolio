package pack8;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.StringTokenizer;

public class Quiz2_1Main {

	ArrayList<Quiz2_1Dto> list = new ArrayList<Quiz2_1Dto>();
	Calendar cal = Calendar.getInstance();

	public void inputData(String[] args) {
		for (int i = 0; i < args.length; i++) {
			StringTokenizer tokenizer = new StringTokenizer(args[i], ",");
			String num = tokenizer.nextToken();
			String name = tokenizer.nextToken();
			String salary = tokenizer.nextToken();
			String year = tokenizer.nextToken();

			Quiz2_1Dto sal = new Quiz2_1Dto(num, name, salary, year);
			list.add(sal);
		}
	}

	public int calGeunsok(int year) {
		int geun = 0;
		if (year > 0 && year <= 3) {
			geun = 150000;
		} else if (year >= 4 && year <= 8) {
			geun = 450000;
		} else {
			geun = 1000000;
		}

		return geun;
	}

	public int calGongjae(int gibon, int geunsok) {
		int gongjae = 0;

		int geupyeo = gibon + geunsok;

		if (geupyeo < 2000000) {
			gongjae = (int) Math.round(geupyeo * 0.15);
		} else if (geupyeo >= 2000000 && geupyeo < 3000000) {
			gongjae = (int) Math.round(geupyeo * 0.3);
		}

		else {
			gongjae = (int) Math.round(geupyeo * 0.5);
		}

		return gongjae;
	}

	public void showData() {
		int year = cal.get(Calendar.YEAR);
		System.out.println("사번\t이름\t기본급\t근무년수\t근속수당\t공제액\t수령액");

		for (int i = 0; i < list.size(); i++) {
			Quiz2_1Dto s = new Quiz2_1Dto();
			s = list.get(i);

			int gibon = Integer.parseInt(s.getSalary());
			int geunsok = calGeunsok((year - Integer.parseInt(s.getyear())));
			int gongjae = calGongjae(Integer.parseInt(s.getSalary()), geunsok);

			System.out.println(s.getNum() 
					+ "\t" + s.getName() 
					+ "\t" + s.getSalary() 
					+ "\t" + (year - Integer.parseInt(s.getyear())) 
					+ "\t" + geunsok 
					+ "\t" + gongjae 
					+ "\t" + (gibon + geunsok - gongjae));
		}
	}

	public static void main(String[] args) {
		Quiz2_1Main sm = new Quiz2_1Main();
		sm.inputData(args);
		sm.showData();

//		int year = cal.get(Calendar.YEAR);
//		int month = cal.get(Calendar.MONTH) +1 ;
//		int date = cal.get(Calendar.DATE);
//		
//		System.out.println(year+ "" + month +"" + date);
	}

}
