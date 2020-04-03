package pack3;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

//@Component
//@Repository	//DB참조를 하는 용도의 클래스는 이것을 사용한다.
@Repository("articleDao")	//@Repository 와 @Repository("articleDao") 는 동일하다.
public class ArticleDao implements ArticleInter{	//DB 처리 관련
	public void selectAll() {
		//DB 다녀왔다고 가정함.
		System.out.println("DB의 고객 전체 자료 읽기");
	}
}
