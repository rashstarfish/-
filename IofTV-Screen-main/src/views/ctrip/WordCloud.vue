<template>
  <div id="wordcloud" :style="{ width: '100%', height: '300px' }"></div>
</template>
<script>
import * as echarts from "echarts";
import "echarts-wordcloud"
import { getWordCloud } from "@/api/ctrip/data";

export default {
  mounted() {
    this.init();
  },
  methods: {
    init(){
      getWordCloud().then((res) => {
        let data = []
        for(let i=0; i<res.length && i<100; i++){
          data.push({name: Object.keys(res[i])[0], value: Object.values(res[i])[0]})
        }
        // console.log(data)
        this.initWordCloud(data)
      })
    },
    initWordCloud(data) {
      const chart = echarts.init(document.getElementById("wordcloud"));
      const option = {
        series: [
          {
            type: "wordCloud",
            shape: "circle",
            left: "center",
            top: "center",
            width: "100%",
            height: "100%",
            sizeRange: [12, 60],
            rotationRange: [-90, 90],
            rotationStep: 45,
            gridSize: 8,
            drawOutOfBound: false,
            layoutAnimation: true,
            textStyle: {
              fontFamily: "sans-serif",
              fontWeight: "bold",
              color: function () {
                return (
                  "rgb(" +
                  [
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                  ].join(",") +
                  ")"
                );
              },
            },
            emphasis: {
              focus: "self",
              textStyle: {
                textShadowBlur: 10,
                textShadowColor: "#999",
              },
            },
            data: data
          },
        ],
      };
      chart.setOption(option);
    },
  },
};
let fakeData = [
    { "name": "服务", "value": 250 },
    { "name": "干净", "value": 200 },
    { "name": "舒适", "value": 180 },
    { "name": "位置", "value": 160 },
    { "name": "房间", "value": 150 },
    { "name": "早餐", "value": 140 },
    { "name": "设施", "value": 130 },
    { "name": "友好", "value": 120 },
    { "name": "酒店", "value": 110 },
    { "name": "工作人员", "value": 100 },
    { "name": "性价比", "value": 90 },
    { "name": "安静", "value": 85 },
    { "name": "整洁", "value": 80 },
    { "name": "方便", "value": 75 },
    { "name": "装修", "value": 70 },
    { "name": "环境", "value": 65 },
    { "name": "床", "value": 60 },
    { "name": "卫生间", "value": 55 },
    { "name": "周边", "value": 50 },
    { "name": "美味", "value": 48 },
    { "name": "氛围", "value": 45 },
    { "name": "宽敞", "value": 42 },
    { "name": "交通", "value": 40 },
    { "name": "性价比高", "value": 38 },
    { "name": "热水", "value": 36 },
    { "name": "性价比高", "value": 35 },  // 注意：这里重复了，实际应去重
    { "name": "停车", "value": 34 },
    { "name": "无线网络", "value": 32 },
    { "name": "空调", "value": 30 },
    { "name": "夜景", "value": 28 },
    { "name": "安全", "value": 26 },
    { "name": "前台", "value": 24 },
    { "name": "风格", "value": 22 },
    { "name": "游泳池", "value": 20 },
    { "name": "健身房", "value": 18 },
    { "name": "推荐", "value": 16 },
    { "name": "夜景美", "value": 15 },
    { "name": "性价比高", "value": 14 },  // 注意：这里又重复了，实际应去重并调整
    { "name": "再来", "value": 13 },
    { "name": "中心", "value": 12 },
    { "name": "氛围好", "value": 11 },
    { "name": "光线", "value": 10 },
    { "name": "隔音", "value": 9 },
    { "name": "枕头", "value": 8 },
    { "name": "电梯", "value": 7 },
    { "name": "景观", "value": 6 },
    { "name": "便利", "value": 5 },
    { "name": "露台", "value": 4 },
    { "name": "宠物", "value": 3 },
    { "name": "特色", "value": 2 },
    { "name": "亲子", "value": 1 }
]
</script>
