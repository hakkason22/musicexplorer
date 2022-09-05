<template>
    <div id="usage_container">
        <div id="usage_cards">
            <div id='usage_1' class="usage_card" v-show="$store.getters['usage/show_usage_page'](1)">
                <div class="card_title">
                    <p class="card_title_index">STEP1</p>
                    <p class="card_title_text">アーティストを検索！！</p>
                </div>
                <!-- /.card_title -->
                <div id="card_figure_1" class="card_figure">
                    <div id="card_figure_search">
                        <div>
                            <p>気になるアーティストの名前で検索</p>
                        </div>
                    </div>
                    <!-- /#card_figure_search -->
                    <div id="card_figure_artist_select">
                        <div class="card_figure_artist_select_item">
                            <div></div>
                        </div>
                        <!-- /.card_figure_artist_select_item -->
                        <div class="card_figure_artist_select_item">
                            <div></div>
                        </div>
                        <!-- /.card_figure_artist_select_item -->
                        <div class="card_figure_artist_select_item">
                            <p>
                                おすすめアーティストを選択
                            </p>
                        </div>
                        <!-- /.card_figure_artist_select_item -->
                    </div>
                    <!-- /#card_figure_artist_select -->
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
                    <div class="card_figure_graph">
                        <div class="card_figure_graph_overview">
                            <p>検索したアーティストの楽曲が<br> <strong>"楽しさ"</strong> と <strong>"激しさ"</strong> の値で<br>グラフにプロットされる</p>
                        </div>
                        <div v-for="i in Array(5)" :key="i" class="card_figure_graph_item"></div>
                        <!-- /.card_figure_music -->
                    </div>
                    <!-- /#card_figure_graph -->
                    <div id="card_figure_graph_menu">
                        <div id="card_figure_player" class="card_figure_graph_menu_item">
                            <font-awesome-icon icon="fa-solid fa-play" id="player_icon" class="card_figure_graph_menu_icon"/>
                            <p>楽曲を再生</p>
                        </div>
                        <!-- /#card_figure_player -->
                        <div id="card_figure_favorite" class="card_figure_graph_menu_item">
                            <font-awesome-icon icon="fa-solid fa-star" id="favorite_icon" class="card_figure_graph_menu_icon"/>
                            <p>お気に入り登録</p>
                        </div>
                        <!-- /.card_figure_favorite -->
                        <div id="card_figure_map" class="card_figure_graph_menu_item">
                            <font-awesome-icon icon="fa-solid fa-compass" id="location_icon" class="card_figure_graph_menu_icon"/>
                            <p>マップで現在地を確認</p>
                        </div>
                        <!-- /#card_figure_map -->
                    </div>
                    <!-- /#card_figure_player -->
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
                    <div id="card_figure_graph_favorite" class="card_figure_graph">
                        <div class="card_figure_graph_overview">
                            <p>お気に入り登録した楽曲は<br>いつでもグラフにプロットできる</p>
                        </div>
                        <div v-for="i in Array(6)" :key="i" class="card_figure_graph_item"></div>
                        <!-- /.card_figure_music -->
                    </div>
                    <!-- /#card_figure_graph -->
                    <div id="card_figure_graph_favorite_menu">
                        <div>
                            <p>今すぐ楽曲探索を始めよう！！</p>
                        </div>
                    </div>
                    <!-- /#card_figure_player -->
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
        this.$store.commit("usage/set_max_page",3)
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
        color: rgb(100, 100, 100);
    }

    #card_figure_search{
        height: 30%;
        width: 100%;
        font-size: 1rem;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    #card_figure_search div{
        height: 50%;
        width: 65%;
        background-color: white;
        border-radius: 5rem;
        margin-top: 5%;
    }

    #card_figure_search div p{
        line-height: 3rem;
        margin: 0;
    }

    #card_figure_artist_select{
        height: 70%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5% 5%;
    }

    .card_figure_artist_select_item{
        height: 70%;
        width: 27%;
        margin-top: 5%;
        border-radius: 1rem;
        background-color: black;
        border: solid white;
        position: relative;
    }

    .card_figure_artist_select_item:last-child{
        background-color: white;
        border: solid black;
    }

    .card_figure_artist_select_item div{
        position: absolute;
        top: 15%;
        left: 15%;
        background-color: white;
        height: 50%;
        width: 70%;
        border-radius: 0.5rem;
    }

    .card_figure_artist_select_item p{
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
        height: 3rem;
    }

    .card_figure_graph{
        position: relative;
        height: 60%;
        width: 100%;
    }
    .card_figure_graph_overview{
        width: 38%;
        height: 85%;
        line-height: 2rem;
        left: 1%;
        top: 15%;
        position: absolute;
    }
    .card_figure_graph_overview p{
        color: white;
        height: 100%;
        width: 100%;
    }
    .card_figure_graph_item{
        position: absolute;
        width: 5%;
        padding-top: 5%;
        background-color: white;
        border-radius: 50%;
    }
    .card_figure_graph div:nth-child(2){
        left: 45%;
        top: 60%;
    }
    .card_figure_graph div:nth-child(3){
        left: 56%;
        top: 30%;
    }
    .card_figure_graph div:nth-child(4){
        left: 65%;
        top: 55%;
    }
    .card_figure_graph div:nth-child(5){
        background-color: black;
        border: solid white;
        left: 70%;
        top: 20%;
    }
    .card_figure_graph div:nth-child(6){
        left: 85%;
        top: 10%;
    }

    #card_figure_graph_menu{
        height: 40%;
        width: 95%;
        margin: 0 auto;
        display: flex;
    }

    .card_figure_graph_menu_item{
        background-color: white;
        height: 60%;
        width: 37%;
        margin: 2.5% 2%;
        border-radius: 1rem;
        text-align: center;
        vertical-align: middle;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding: 1%;
    }
    .card_figure_graph_menu_icon{
        margin: 10% 5%;
    }
    .card_figure_graph_menu_item p{
        width: 80%;
        margin: 5% 0;
    }
    #player_icon{
        height: 65%;
        width: 20%;
    }
    #favorite_icon{
        width: 20%;
        height: 80%;
    }
    #location_icon{
        width: 20%;
        height: 80%;
    }

    #card_figure_graph_favorite div:nth-child(7){
        background-color: blue;
        border: solid white;
        left: 80%;
        top: 50%;
    }

    #card_figure_graph_favorite_menu{
        height: 40%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    #card_figure_graph_favorite_menu div{
        background-color: white;
        height: 60%;
        width: 90%;
        border-radius: 1rem;
    }

    #card_figure_graph_favorite_menu div p{
        line-height: 1rem;
        font-size: 2rem;
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
