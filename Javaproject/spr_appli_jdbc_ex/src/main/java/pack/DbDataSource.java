package pack;

import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Component;

@Component("dbSource")
public class DbDataSource extends DriverManagerDataSource{
	public DbDataSource() {
		this.setDriverClassName("org.mariadb.jdbc.Driver");
		setUrl("jdbc:mysql://localhost:3306/test");
		setUsername("root");
		setPassword("123");
	}
}
