<template>
    <div id="usage_container">
        <div id="usage_cards">
            <div id='usage_1' class="usage_card" v-show="$store.getters['usage/show_usage_page'](1)">
                <div class="card_title">
                    <p class="card_title_index">STEP1</p>
                    <p class="card_title_text">アーティストを検索！！</p>
                </div>
                <!-- /.card_title -->
                <div class="card_figure">
                    
                </div>
                <!-- /.card_figure -->
            </div>
            <!-- /.usage_item -->
            <div id='usage_2' class="usage_card" v-show="$store.getters['usage/show_usage_page'](2)">
                <div class="card_title">
                    <p class="card_title_index">STEP2</p>
                    <p class="card_title_text">お気に入りの曲を探そう！！</p>
                </div>
                <!-- /.card_title -->
                <div class="card_figure">
                        
                </div>
                <!-- /.card_figure -->
            </div>
            <!-- /.usage_item -->
            <div id='usage_3' class="usage_card" v-show="$store.getters['usage/show_usage_page'](3)">
                <div class="card_title">
                    <p class="card_title_index">STEP3</p>
                    <p class="card_title_text">お気に入り曲をプロット！！</p>
                </div>
                <!-- /.card_title -->
                <div class="card_figure">
                        
                </div>
                <!-- /.card_figure -->
            </div>
            <!-- /.usage_item -->
            <div id='usage_4' class="usage_card" v-show="$store.getters['usage/show_usage_page'](4)">
                <div class="card_title">
                    <p class="card_title_index">STEP4</p>
                    <p class="card_title_text">……！！</p>
                </div>
                <!-- /.card_title -->
                <div class="card_figure">
                    
                </div>
                <!-- /.card_figure -->
            </div>
            <!-- /.usage_item -->
        </div>
        <!-- /#usage_card -->
        <div id="usage_pagination">
            <a id="back_page" class="usage_pagination_item" @click.prevent="back_usage_page"></a>
            <!-- /.usage_pagination_item -->
            <a id="next_page" class="usage_pagination_item" @click.prevent="next_usage_page"></a>
            <!-- /.usage_pagination_item -->
        </div>
        <!-- /#usage_paging -->
    </div>
    <!-- /#usage -->
</template>
<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
    data(){
        return {
           
        }
    },
    mounted(){
    
    },
    methods:{
        next_usage_page(){
            this.$store.commit("usage/next_usage_page")
            console.log(this.$store.state.usage.usage_page)
        },
        back_usage_page(){
            this.$store.commit("usage/back_usage_page")
            console.log(this.$store.state.usage.usage_page)
        }
    }
})
</script>

<style>
    #usage_container{
        color: white;
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 3% 0;
    }
    #usage_cards{
        display: flex;
        height: 90%;
        width: 100%;
        flex-wrap: wrap;
    }
    .usage_card{
        height: 96%;
        width: 96%;
        background-color: rgb(60, 50, 50);
        border-radius: 10px;
        text-align: center;
        padding: 2%;
    }
    .card_title{
        position: relative;
        width: 100%;
        height: 4rem;
        justify-content: center;
        border-bottom: solid rgba(255, 255, 255, 0.6);
    }
    .card_title_index{
        position: absolute;
        bottom: 0;
        left:0;
        font-size: 3rem;
        margin: 0;
        padding: 0;
        opacity: 0.7;
    }
    .card_title_text{
        position: absolute;
        bottom: 0.5rem;
        right: 0;
        font-size: 1.5rem;
        margin: 0;
        padding: 0;
    }

    .card_figure{
        height: 84%;
        width: 100%;
    }

    #usage_pagination{
        display: flex;
        height: 10%;
        width: 100%;
        align-items: center;
        justify-content: center;
        padding-top: 3%;
        gap: 0 10%;
    }

    a:hover {
        color: rgba(255, 255, 255, 0.5);
    }

    #next_page{
        display: inline-block;
        vertical-align: middle;
        line-height: 1;
        width: 0;
        height: 0;
        border-style: solid;
        border-color: transparent;
        border-width: 1.5em 3em;
        border-left-color: currentColor;
        border-right: 0;
    }

    #back_page{
        display: inline-block;
        vertical-align: middle;
        line-height: 1;
        width: 0;
        height: 0;
        border-style: solid;
        border-color: transparent;
        border-width: 1.5em 3em;
        border-right-color: currentColor;
        border-left: 0;
    }
</style>
