package pack.board.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.board.model.Board;
import pack.board.model.BoardDao;

@Controller
public class SearchController {
	@Autowired
	private BoardDao boardDao;

	@RequestMapping("search")
	public ModelAndView search(BoardBean bean) {
			List<Board> list = boardDao.search(bean);
		return new ModelAndView("list", "datas", list);
	}
}
