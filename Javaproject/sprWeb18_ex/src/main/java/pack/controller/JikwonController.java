package pack.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import pack.model.DataDao;
import pack.model.JikwonDto;

@Controller
public class JikwonController {
	@Autowired
	private DataDao dataDao;

	@RequestMapping(value = "jikwonlist", method = RequestMethod.GET)
	@ResponseBody
	public Map<String, Object> jikwonFunc(@RequestParam("buser_name") String buser_name) {
		List<Map<String, String>> dataList = new ArrayList<Map<String, String>>();
		Map<String, String> data = null;
		
		System.out.println(buser_name);
		List<JikwonDto> jikList = dataDao.jikwonList(buser_name);

		for (JikwonDto s : jikList) {
			data = new HashMap<String, String>();

			data.put("jikwon_no", s.getJikwon_no());
			data.put("jikwon_name", s.getJikwon_name());
			data.put("buser_tel", s.getBuser_tel());
			data.put("jikwon_jik", s.getJikwon_jik());
			data.put("gogek_damsano", s.getGogek_damsano());
			dataList.add(data);
		}
		Map<String, Object> jikwons = new HashMap<String, Object>();
		jikwons.put("jikDatas", dataList);

		return jikwons;
	}
}
