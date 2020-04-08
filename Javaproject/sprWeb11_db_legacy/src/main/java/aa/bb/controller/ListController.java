package aa.bb.controller;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.model.DataDao;
import aa.bb.model.SangpumDto;

@Controller
public class ListController {
	@Autowired
	private DataDao dataDao;
	
	
	@RequestMapping("testdb")
	public ModelAndView listProcess() {
		// 모델과 통신 가능
		ArrayList<SangpumDto> list = dataDao.getDataAll();
		
		return new ModelAndView("show", "datas", list);
	}
}
