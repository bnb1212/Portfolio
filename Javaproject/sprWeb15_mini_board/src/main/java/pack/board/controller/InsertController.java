package pack.board.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import pack.board.model.Board;
import pack.board.model.BoardDao;

@Controller
public class InsertController {
	
	@Autowired
	private BoardDao boardDao;
	
	@RequestMapping(value = "insert", method=RequestMethod.GET)
	public String insFormAccess(){
		return "insform";
	}

	@RequestMapping(value = "insert", method=RequestMethod.POST)
	public String insFormProcess(BoardBean bean){
		int b = boardDao.insert(bean);
		if(b > 0)
			return "redirect:/boardlist"; // 추가후 목록 보기
		else
			return "error";
	}
	
	
	
	
}
