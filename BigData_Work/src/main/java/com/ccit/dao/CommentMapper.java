package com.ccit.dao;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface CommentMapper {
    @Select("select comment_text from comment_text limit 100")
    List<String> getComments();
}
