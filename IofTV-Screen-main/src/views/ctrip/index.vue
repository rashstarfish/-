<template>
    <div class="contents">
        <div class="content-left">
            <CenterMap/>
            <!-- <ItemWrap style="height: 300px;">
            </ItemWrap> -->
        </div>
        <div class="content-right">
            <ItemWrap style="height: 400px" title="评论词云">
                <WordCloud/>
            </ItemWrap>
            <ItemWrap style="height: 500px;" title="平均价格">
                <ChartOne/>
            </ItemWrap>
        </div>
    </div>

</template>
<script>
import ChartOne from './ChartOne.vue'
import WordCloud from './WordCloud.vue';
import CenterMap from './CenterMap.vue';
import ItemWrap from '@/components/item-wrap/item-wrap.vue';
export default {
    components:{
       ChartOne,
       WordCloud,
       CenterMap
    },
    data(){
        return{
            options:{}
        }
    },
    mounted(){
      
    }

}

</script>

<style lang="scss">

.contents {
  .content-left{
    width: 900px;
    box-sizing: border-box;
  }
  .content-right {
    width: 900px;
    box-sizing: border-box;
    // padding: 16px 0;
  }
}




</style>