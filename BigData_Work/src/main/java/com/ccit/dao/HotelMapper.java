package com.ccit.dao;

import com.ccit.pojo.Hotel;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

@Mapper
public interface HotelMapper {
    @Select("select * from hotels_info")
    List<Hotel> findAll();

    @Select("select count(*) from hotels_info")
    int count();

    @Select("select city,AVG(TO_NUMBER(price)) AS price from hotels_info group by city")
    List<Map<String,String>> calcAvgPrice();

    @Select("select city,count(*) as cnt from hotels_info group by city")
    List<Map<String,String>> countCity();


}
