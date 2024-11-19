import com.ccit.dao.HotelMapper;
import com.ccit.pojo.Hotel;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.JdbcTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.TestComponent;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;
import java.util.List;

@SpringBootTest(classes = com.ccit.App.class)
public class TestDb {

    @Autowired
    private DataSource dataSource;

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Autowired
    private HotelMapper hotelMapper;

    @Test
    public void test(){
        List<String> result = jdbcTemplate.queryForList("select TABLE_NAME from SYSTEM.\"CATALOG\"",String.class);
        System.out.println(result);
    }

    @Test
    public void test1(){
        System.out.println(hotelMapper.count());
    }


}
