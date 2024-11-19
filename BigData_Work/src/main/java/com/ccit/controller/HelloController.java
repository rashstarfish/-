package com.ccit.controller;

import com.ccit.service.StatisticService;
import com.ccit.util.GsonUtil;
import com.google.gson.Gson;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @Autowired
    private StatisticService statisticService;

    @GetMapping("/avgPrice")
    public String avgPrice() {
        return GsonUtil.gson.toJson(statisticService.getAvgPrice());
    }

    @GetMapping("/wordCloud")
    public String wordCloud() {
        return GsonUtil.gson.toJson(statisticService.getWordCloudMap());
    }

    @GetMapping("/cityCnt")
    public String cityCnt() {
        return GsonUtil.gson.toJson(statisticService.countCity());
    }

}
