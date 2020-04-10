package pack.board.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import pack.board.model.BoardDao;

@Controller
public class DeleteController {

	@Autowired
	private BoardDao boardDao;
	
	@RequestMapping("delete")
	public String del(@RequestParam("num") String num) {
		if(boardDao.delete(num))
			return "redirect:/boardlist";
		else
			return "error";
	}
}
