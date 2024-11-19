import * as API from "./api";
import xzqCode from "@/utils/map/xzqCode";

export function getAvgPrice(){
    return API.GETNOBASE('/api/avgPrice')
}

export function getWordCloud(){
    return API.GETNOBASE('/api/wordCloud')
}

export function getCityCnt(regionCode){
    return API.GETNOBASE('/api/cityCnt').then(res => {
        let datalist = []
        for (let i = 0; i < res.length; i++) {
            datalist.push({
                name:res[i].CITY,
                value: res[i].CNT
            })
        }
        
        if (regionCode && regionCode != 'china') {
            const a = {
                success: true,
                data: {
                    dataList: datalist,
                    regionCode: regionCode,//-代表中国
                }
            }
            return a
        } else {
            const a = {
                success: true,
                data: {
                    dataList: datalist,
                    regionCode: 'china',
                }
            }
            return a
        }
    })
}