package pack3;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

@Service
public class LogicImpl implements LogicInter{	//핵심 로직
	@Autowired	//articleInter에 자식클래스가 하나라서 이것만 쓴다.
	@Qualifier("articleDao")	//articleInter에 자식이 여러개일 경우 자식클래스객체를 지정해줘야 한다.
	private ArticleInter articleInter;
	
	public LogicImpl() {
		
	}

	public LogicImpl(ArticleInter articleInter) {	//생성자 주입
		this.articleInter = articleInter;
	}
	
	public void selectDataProcess() {
		articleInter.selectAll();
	}
	
	public void updateDataPart() {
		System.out.println("updateDataPart 수행");
	}
	
	public void abc() {	//고유 메소드
		System.out.println("abc 수행");
	}
}
