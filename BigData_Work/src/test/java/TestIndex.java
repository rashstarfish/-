import com.ccit.util.AreaUtil;
import org.junit.jupiter.api.Test;

import java.io.FileReader;

public class TestIndex {
    @Test
    public void test() {
        System.out.println(AreaUtil.getCity("大丰"));
        System.out.println(AreaUtil.getXzq("青岛"));
    }
}
