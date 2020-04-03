package pack8;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

// Set 인터페이스 : 중복 불가, 순서 없다
public class SetTest {
	public static void main(String[] args) {
//		HashSet<Object> list = new HashSet<Object>();
		HashSet<String> list = new HashSet<String>();
		list.add("Kim");
		list.add("Lee");
		list.add("Lee"); // 중복데이터는 담을수 없음
		list.add("Park");
		list.add("Choi");		
//		list.add(1);// Boxing/UnBoxing 기본형은 ~래퍼 클래스에 의해 박싱이 되고 참조형으로 기억됨(오토박싱) 
//		SetTest ts = new SetTest();
//		list.add(ts);
		System.out.println(list.size());
		list.remove("Kim");
		System.out.println(list.size());
		System.out.println(list);
		System.out.println(list.toString());
//		System.out.println(list[0]);
		
		print(list);
	}
	
	public static void print(Set set) {
		Iterator iter = set.iterator();
		while(iter.hasNext()) {
			String ss = (String)iter.next();
			System.out.println(ss);
		}
	}
	
	public static void print2(Object[] obj) {
		int count = obj.length;
		for(int i=0; i < count; i++) {
			System.out.println(obj[1]);
		}
		for(Object aa:obj) {
			System.out.println(aa);
		}
		
	}
}
