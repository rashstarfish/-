package com.ccit.util;

import com.ccit.pojo.Area;
import com.google.gson.Gson;

import java.io.FileReader;
import java.io.InputStreamReader;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;


public class AreaUtil {
    public static List<Area> areas=null;
    public static List<Area> xzqs=null;
    public static List<Area> cities=null;
    static{
        Gson gson=GsonUtil.gson;
        Type areaListType = new com.google.gson.reflect.TypeToken<List<Area>>(){}.getType();
        ClassLoader classLoader = AreaUtil.class.getClassLoader();
        InputStreamReader reader = null;
        try{
            reader = new InputStreamReader(classLoader.getResourceAsStream("area_index.json"));
            areas=gson.fromJson(reader,areaListType);
        }catch(Exception e){
            e.printStackTrace();
        }finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        xzqs=new ArrayList<Area>();
        cities=new ArrayList<Area>();
        for(Area area:areas){
            if("city".equals(area.getType())){
                cities.add(area);
            }
            if("xzq".equals(area.getType())){
                xzqs.add(area);
            }
        }
    }

    public static String format(String name){
        for (Area area : areas) {
            if (area.getName().contains(name)) {
                return area.getName();
            }
        }
        return name;
    };

    public static String getCity(String name){
        for(Area area : areas){
            if(area.getName().contains(name)){
                return area.getCity();
            }
        }
        return name;
    };

    public static String getXzq(String name){
        for(Area area : areas){
            if(area.getName().contains(name)){
                return area.getXzq();
            }
        }
        return name;
    }
}
