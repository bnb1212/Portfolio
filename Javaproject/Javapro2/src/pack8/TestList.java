package pack8;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

// === List 인터페이스, 중복 가능, 순서 있음0
public class TestList {
	public static void main(String[] args) {

		ArrayList<String> list = new ArrayList<String>();
		list.add("kim");
		list.clear();
		System.out.println(list.size());
		list.add("kim");
		list.add("lee");
		list.add("park");
		list.add("kim"); // list는 중복 허용
		list.add("choi");
		list.remove("lee");
		list.remove(0);
		System.out.println(list.size());
		System.out.println(list);
//		System.out.println(list[0]);
		System.out.println(list.get(0));
		System.out.println(list.contains("parks"));
		System.out.println();
		print(list);
		print2(list);
	}

	public static void print(List list) {
		Iterator iter = list.iterator();
		while (iter.hasNext()) {
			String ss = (String) iter.next();
			System.out.println(ss);
		}
	}

	public static void print2(List obj) {
		for (Object aa : obj) {
			System.out.println(aa);
		}
	}
}