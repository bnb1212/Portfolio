package pack.board.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import pack.board.model.Board;
import pack.board.model.BoardDao;

@Controller
public class UpdateController {

	@Autowired
	private BoardDao boardDao;
	
	@RequestMapping("updateAc")
	public ModelAndView updateAccess(@RequestParam("num") String num){
		Board board = boardDao.detail(num);
		return new ModelAndView("updateform", "dto", board);
	}
	
	@RequestMapping(value = "update", method=RequestMethod.POST)
	public String upFormProcess(BoardBean bean){
		boolean b = boardDao.update(bean);
		if(b)
			return "redirect:/detail?num="+bean.getNum(); // 추가후 목록 보기
		else
			return "error";
	}
}
