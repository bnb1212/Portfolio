package aa.bb.cc;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("list2")
public class JsonController2 {
	@RequestMapping(method=RequestMethod.GET)
	@ResponseBody
	public Map getJson() {
		List<Map<String, String>> dataList = new ArrayList<Map<String,String>>();
		
		Map<String, String> data = new HashMap<String, String>();
		data.put("name", "홍길동");
		data.put("age", "22");
		dataList.add(data);

		data = new HashMap<String, String>();
		data.put("name", "라스");
		data.put("age", "17");
		dataList.add(data);
		
		data = new HashMap<String, String>();
		data.put("name", "빌트레드");
		data.put("age", "37");
		dataList.add(data);
		
		//return data;
		
		Map<String, Object> datas=new HashMap<String, Object>();
		datas.put("datas", dataList);
		return datas;
		
		
	}
	
}
