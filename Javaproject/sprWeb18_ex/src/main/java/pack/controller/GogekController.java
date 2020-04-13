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
import pack.model.GogekDto;

@Controller
public class GogekController {
	@Autowired
	private DataDao dataDao;

	@RequestMapping(value = "gogeklist", method = RequestMethod.GET)
	@ResponseBody
	public Map<String, Object> gogekFunc(@RequestParam("jikwon_no") String jikwon_no) {
		List<Map<String, String>> dataList = new ArrayList<Map<String, String>>();
		Map<String, String> data = null;

		System.out.println(jikwon_no);
		List<GogekDto> goList = dataDao.gogekList(jikwon_no);

		for (GogekDto s : goList) {
			data = new HashMap<String, String>();

			data.put("gogek_no", s.getGogek_no());
			data.put("gogek_name", s.getGogek_name());
			data.put("gogek_tel", s.getGogek_tel());
			dataList.add(data);
		}
		Map<String, Object> gogeks = new HashMap<String, Object>();
		gogeks.put("gogekDatas", dataList);

		return gogeks;
	}

}
