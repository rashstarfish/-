<template>
    <Echart
    :options="options"
    :optfunc="optfunc"
    ></Echart>
</template>
<script>
import * as echarts from 'echarts';
import { getAvgPrice } from '@/api/ctrip/data';
    export default {
        data(){       
            return{
                options : {}
            }
        },
        mounted(){
            this.init();
        },
        methods: {
            optfunc(myChart,options){
                let dataAxis = options.xAxis.data;
                let data = options.series[0].data;
                const zoomSize = 6;
                myChart.on('click', function (params) {
                    console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
                    myChart.dispatchAction({
                        type: 'dataZoom',
                        startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
                        endValue:
                        dataAxis[Math.min(params.dataIndex + zoomSize / 2, data.length - 1)]
                    });
                });
            },
            init(){
                getAvgPrice().then(response => {
                    // console.log(response);
                    let cities=[];
                    let values=[];
                    Array.from(response).forEach(item => {
                        cities.push(item.CITY);
                        values.push(item.PRICE);
                    })
                    this.setData({cities:cities,values:values})
                })
                
            },
            setData(data){
                // // prettier-ignore
                // let dataAxis = ['点', '击', '柱', '子', '或', '者', '两', '指', '在', '触', '屏', '上', '滑', '动', '能', '够', '自', '动', '缩', '放'];
                // // prettier-ignore
                // let data = [220, 182, 191, 234, 290, 330, 310, 123, 442, 321, 90, 149, 210, 122, 133, 334, 198, 123, 125, 220];
                let dataAxis = data.cities;
                data = data.values;

                let yMax = 500;
                let dataShadow = [];
                for (let i = 0; i < data.length; i++) {
                dataShadow.push(yMax);
                }
                this.options = {
                title: {
                    // text: '特性示例：渐变色 阴影 点击缩放',
                    // subtext: 'Feature Sample: Gradient Color, Shadow, Click Zoom'
                },
                xAxis: {
                    data: dataAxis,
                    axisLabel: {
                    inside: true,
                    color: '#fff'
                    },
                    axisTick: {
                    show: false
                    },
                    axisLine: {
                    show: false
                    },
                    z: 10
                },
                yAxis: {
                    axisLine: {
                    show: false
                    },
                    axisTick: {
                    show: false
                    },
                    axisLabel: {
                    color: '#999'
                    }
                },
                dataZoom: [
                    {
                    type: 'inside'
                    }
                ],
                series: [
                    {
                    type: 'bar',
                    showBackground: true,
                    itemStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: '#83bff6' },
                        { offset: 0.5, color: '#188df0' },
                        { offset: 1, color: '#188df0' }
                        ])
                    },
                    emphasis: {
                        itemStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: '#2378f7' },
                            { offset: 0.7, color: '#2378f7' },
                            { offset: 1, color: '#83bff6' }
                        ])
                        }
                    },
                    data: data
                    }
                ]
                };
            }
        },
        
    }

</script>
    
<style lang="scss" scoped>

</style>