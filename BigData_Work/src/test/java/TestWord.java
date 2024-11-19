import com.huaban.analysis.jieba.JiebaSegmenter;
import com.kennycason.kumo.CollisionMode;
import com.kennycason.kumo.WordCloud;
import com.kennycason.kumo.WordFrequency;
import com.kennycason.kumo.bg.CircleBackground;
import com.kennycason.kumo.font.KumoFont;
import com.kennycason.kumo.font.scale.SqrtFontScalar;
import com.kennycason.kumo.nlp.FrequencyAnalyzer;
import com.kennycason.kumo.nlp.tokenizers.ChineseWordTokenizer;
import com.kennycason.kumo.palette.ColorPalette;
import org.junit.jupiter.api.Test;

import java.awt.*;
import java.io.ByteArrayOutputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class TestWord {
    public static String getWordCloud(List<String> words) {
        FrequencyAnalyzer frequencyAnalyzer = new FrequencyAnalyzer();
        frequencyAnalyzer.setWordFrequenciesToReturn(600);
        frequencyAnalyzer.setMinWordLength(2);

        // 引入中文解析器
        frequencyAnalyzer.setWordTokenizer(new ChineseWordTokenizer());

        final List<WordFrequency> wordFrequencyList = frequencyAnalyzer.load(words);

        // 设置图片分辨率
        Dimension dimension = new Dimension(500, 500);
        // 此处的设置采用内置常量即可，生成词云对象
        WordCloud wordCloud = new WordCloud(dimension, CollisionMode.PIXEL_PERFECT);
        java.awt.Font font = new java.awt.Font("STSong-Light", 2, 18);
        wordCloud.setKumoFont(new KumoFont(font));
        wordCloud.setPadding(2);
        wordCloud.setColorPalette(new ColorPalette(new Color(0xed1941), new Color(0xf26522), new Color(0x845538),new Color(0x8a5d19),new Color(0x7f7522),new Color(0x5c7a29),new Color(0x1d953f),new Color(0x007d65),new Color(0x65c294)));
        wordCloud.setBackground(new CircleBackground(200));
        wordCloud.setFontScalar(new SqrtFontScalar(10, 40));
        wordCloud.setBackgroundColor(new Color(255, 255, 255));
        // 生成词云
        wordCloud.build(wordFrequencyList);
        OutputStream output = new ByteArrayOutputStream();
        wordCloud.writeToStream("png", output);
        byte[] outputByte = ((ByteArrayOutputStream)output).toByteArray();
        return org.apache.commons.codec.binary.Base64.encodeBase64String(outputByte);
    }

    @Test
    public void testWordCloud() {
        JiebaSegmenter segmenter = new JiebaSegmenter();
        String text="这是一个测试字符串，用于统计中文词频。这个字符串包含了一些重复的词语。";
        List<String> words = segmenter.sentenceProcess(text);
        System.out.println(getWordCloud(words));
    }

}
