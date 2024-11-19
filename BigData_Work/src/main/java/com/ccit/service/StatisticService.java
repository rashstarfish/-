package com.ccit.service;

import com.ccit.dao.CommentMapper;
import com.ccit.dao.HotelMapper;
import com.ccit.pojo.Area;
import com.ccit.util.AreaUtil;
import com.ccit.util.ConstUtil;
import com.ccit.util.WordCloudUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class StatisticService {
    @Autowired
    private HotelMapper hotelMapper;

    @Autowired
    private CommentMapper commentMapper;

    public List<Map<String, String>> getAvgPrice() {
        return hotelMapper.calcAvgPrice();
    }

    public String getWordCloudBase64(){
        List<String> comments = commentMapper.getComments();
        List<String> words = new ArrayList<>();
        for(String comment : comments){
            words.addAll(WordCloudUtil.splitText(comment));
        }
        String base64 = WordCloudUtil.getWordCloud(words);
        return base64;
    }

    public List<Map<String,Integer>> getWordCloudMap(){
        List<String> comments = commentMapper.getComments();
        List<String> words = new ArrayList<>();
        for(String comment : comments){
            words.addAll(WordCloudUtil.splitText(comment));
        }
        List<Map<String,Integer>> list = new LinkedList<>();
        for(String word : words){
            if(",:.?!，。？！：".contains(word))continue;
            Map<String,Integer> map = new HashMap<>();
            map.put(word,1);
            list.add(map);
        }
        return list;
    }

    public List<Map<String,String>> countCity(){

        List<Map<String,String>> list = hotelMapper.countCity();
        Map<String,Integer> statisticMap = new HashMap<>();
        for(Map<String,String> map : list){
            if(statisticMap.containsKey(AreaUtil.getXzq(String.valueOf(map.get("CITY"))))){
                statisticMap.replace(AreaUtil.getXzq(String.valueOf(map.get("CITY"))),
                        statisticMap.get(AreaUtil.getXzq(String.valueOf(map.get("CITY"))))
                                +Integer.parseInt(String.valueOf(map.get("CNT"))));
            }else{
                statisticMap.put(AreaUtil.getXzq(String.valueOf(map.get("CITY"))),Integer.parseInt(String.valueOf(map.get("CNT"))));
            }
            if(statisticMap.containsKey(AreaUtil.getCity(String.valueOf(map.get("CITY"))))){
                statisticMap.replace(AreaUtil.getCity(String.valueOf(map.get("CITY"))),
                        statisticMap.get(AreaUtil.getCity(String.valueOf(map.get("CITY"))))
                                +Integer.parseInt(String.valueOf(map.get("CNT"))));
            }else{
                statisticMap.put(AreaUtil.getCity(String.valueOf(map.get("CITY"))),Integer.parseInt(String.valueOf(map.get("CNT"))));
            }

        }
        list = new LinkedList<>();
        for(String key : statisticMap.keySet()){
            Map<String,String> map = new HashMap<>();
            map.put("CITY",key);
            map.put("CNT",statisticMap.get(key).toString());
            list.add(map);
        }
    
        return list;

    }

}
