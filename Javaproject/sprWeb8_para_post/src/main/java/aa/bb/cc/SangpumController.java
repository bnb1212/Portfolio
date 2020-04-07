package aa.bb.cc;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
//@service 
public class SangpumController {
	@Autowired
	private SangpumModel sangpumModel;
	
	@RequestMapping(value = "sangpum", method = RequestMethod.POST)
	public ModelAndView submit(@ModelAttribute("my") SangpumBean bean) { // 별명 my로 참조가능
		ModelAndView view = new ModelAndView();
		view.setViewName("result");
		view.addObject("data", sangpumModel.ComputeData(bean));
		return view;
		
	}
	
	@ModelAttribute("hongList")
	public List<String> aaa(){
		List<String> list = new ArrayList<String>();
		list.add("데스티나");
		list.add("만세");
		
		return list;
	}
}
