package pack;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import other.OutFileInterImpl;

@Configuration
public class Config { // arrange.xml 대신 클래스에 어노테이션을 적용
	
	
		@Bean
		public MyInfo myInfo() {
			return new MyInfo();
	}
		
		@Bean
		public MessageImpl messageImpl() {
			MessageImpl impl = new MessageImpl("장비", "관우", 2000, myInfo());
			impl.setSpec("파이썬 선수 예정");
			impl.setMyInfo2(myInfo());
			impl.setFileInter(fileInterImpl());
			return impl;
		}
		
		@Bean
		public OutFileInterImpl fileInterImpl() {
			OutFileInterImpl fileInterImpl = new OutFileInterImpl();
			fileInterImpl.setFilePath("c:/work/ohmygod.txt");
			return fileInterImpl;
		}
}
