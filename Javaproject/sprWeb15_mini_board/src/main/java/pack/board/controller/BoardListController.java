package pack.board.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.board.model.BoardDao;

@Controller
public class BoardListController {

	@Autowired
	private BoardDao boardDao;

	@RequestMapping("boardlist")
	public ModelAndView list() {
		return new ModelAndView("list", "datas", boardDao.getDataAll());
	}
}
