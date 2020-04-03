package pack8;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

// Map 인터페이스 : 자료를 key, value 형태로 저장. 많은 양의 데이터인 경우 검색이 편리
public class TestMap {
	public static void main(String[] args) {
		HashMap<String, String> list = new HashMap<String, String>();
		list.put("0", "LEE"); // value 중복은 허용되나, key값 중복은 허용되지 않는다.
		list.clear();
		list.put("1", "LEE");
		list.put("2", "KIM");
		list.put("3", "LEE");
		list.put("4", "PARK");
		list.put("5", "CHOI");
		list.remove(2);

		System.out.println(list.size());
		System.out.println(list.containsKey("0"));
		System.out.println(list.containsValue("KIM"));

		System.out.println();
		print(list);
	}

	public static void print(Map map) {
		Set set = map.keySet();
		Iterator iter = set.iterator();
		while (iter.hasNext()) {
			String key = (String) iter.next();
			System.out.println("Key : " + key);
			System.out.println("value : " + map.get(key)); // get(key)로 대응되는 value 출력
		}
	}
}
