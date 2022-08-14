<template>
  <div class="chart_wrapper">
    <svg 
        :viewbox="chart_min_width + ' ' + chart_min_height + ' ' + chart_width + ' ' + chart_height" 
        :width=chart_width+100
        :height=chart_height+100
    >
        <text v-for="musicInfo in musicInfos" :key="musicInfo.music_id"
                :x="musicInfo['valence'] * (chart_width-100) + 100"
                :y="(1 - musicInfo['energy']) * (chart_height-100) + 100"
                :fill="musicInfo['graph_color']"
                @click="displayDetail(musicInfo)"
                :font-size="chart_font_size"
                class="graph_element"
        >{{ musicInfo.display_music_name }}</text>

    </svg>
    <div class="detail_wrapper" v-if="$store.state.player.target_music_id !== ''">
        <div class="player_area">
            <iframe
                style="border-radius:12px"
                :src="'https://open.spotify.com/embed/track/'+$store.state.player.target_music_id+'?utm_source=generator'"
                width="100%"
                height="80"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; fullscreen; picture-in-picture">
            </iframe>
        </div>
        <div class="favorite_area">
            <span 
                v-if="$store.state.player.target_is_favorite"
                class="favorite_icon faved"
            >
                    ★
            </span>
            <span 
                v-else
                @click="registerFavorite"
                class="favorite_icon not_faved"
            >
                    ☆
            </span>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from 'axios'
import Vue from 'vue'
import { Music } from '../pages/index.vue'

export default Vue.extend({
    props: ["musicInfos", "artistName"],
    data(){
        return {
            chart_width: 1300,
            chart_height: 1020,
            chart_min_width: 0,
            chart_min_height: 0,
            chart_font_size: 14,
            normal_color: "white",
            favorite_color: "#00fa9a",
            playing_color: "red",
        };
    },
    mounted() {
        this.preProcess();
        this.$nuxt.$on('addFavoriteToChart', this.addUpdateData);
    },
    watch:{
        artistName: function(){
            this.preProcess();
        }
    },  
    methods: {
        setup(){
            this.chart_width = window.innerWidth - 200;
            this.chart_height = window.innerHeight - 200;

            this.musicInfos.forEach((musicInfo: Music) => {
                if(musicInfo.music_name.length < 10){
                    musicInfo.display_music_name = musicInfo.music_name;
                }else{
                    musicInfo.display_music_name = musicInfo.music_name.slice(0, 9) + "...";
                }
                // グラフの色を設定
                if(musicInfo.music_id == this.$store.state.player.target_music_id){
                    musicInfo.graph_color = this.playing_color;
                }else if(musicInfo.is_favorite){
                    musicInfo.graph_color = this.favorite_color;
                }else{
                    musicInfo.graph_color = this.normal_color;
                }
                
                if('is_favorite' in musicInfo === false) {
                    musicInfo.is_favorite = false
                }
            })
            this.musicInfos.splice();
        },
        preProcess(){
            this.setup();
            this.setFavoriteMusicInfo();
        }, 
        addUpdateData(targetMusicInfo: Music){
            targetMusicInfo.is_favorite = true;
            this.musicInfos.push(targetMusicInfo);
            this.setup()
        },
        displayDetail(music: Music){
            if('is_favorite' in music === false){
                music.is_favorite = false
            }
            this.$store.commit('player/setMusic', music);
            this.setup();
            console.log(this.$store.state.player.target_music_name)
        },
        registerFavorite(){
            if(!this.$store.getters.isAuthenticated) {
                this.$store.commit("modal/showModal", "login-induction");
            }else{
                const url = `${process.env.BACKEND_ROOT}/music/favorite/register`;
                const params = new URLSearchParams();
                params.append('music_name', this.$store.state.player.target_music_name);
                params.append('valence', String(this.$store.state.player.target_valence));
                params.append('energy', String(this.$store.state.player.target_energy));
                params.append('music_id', this.$store.state.player.target_music_id);
                params.append('user_id', this.$store.getters.user.uid);
                
                axios.post(url, params).then((response) => {
                    console.log(response.data);
                    this.$store.commit("player/setPlayerFavorite", true)
                    console.log(this.$store.state.player.is_favorite)
                    this.setFavoriteMusicInfo()                    
                });
            }
        },
        async setFavoriteMusicInfo(){
            const user_id: string = this.$store.getters.user.uid
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/list`
            const params: any = new URLSearchParams()
            params.append('user_id', user_id)
            await axios.post(url, params).then((response) => {
                const favoriteMusicInfos: Array<Music> = response.data.data
                console.log(response.data)
                let favorite_music_ids: Array<string> = [];
                favoriteMusicInfos.forEach((favoriteMusicInfo: Music) => {
                    favorite_music_ids.push(favoriteMusicInfo.music_id)
                });
                this.musicInfos.forEach((musicInfo: Music) => {
                    if(favorite_music_ids.includes(musicInfo.music_id)){
                        musicInfo.is_favorite = true;
                    }
                });
                this.setup();
            })
        },
    },
})
</script>
<style scoped>

    .chart_wrapper{
        padding-bottom:60px;
        text-align: center;
    }
    .detail_wrapper{
        position: fixed;
        bottom: 3%;
        left: 0;
        right: 0;
        margin: auto;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .player_area{
        width: 40%;
    }
    .favorite_area{
        padding-left: 10px;
    }
    .favorite_icon{
        font-weight: bold;
        border-radius: 50%;
        padding: 10px;
        font-size: 18px;
    }
    .faved{
        color: black;
        background: lightgray;
        cursor: default;
    }
    .not_faved{
        background: white;
        cursor: pointer;
    }
    svg{
        background: radial-gradient(midnightblue, rgba(0,0,0,0.8));
    }
    .graph_element{
        cursor: pointer;
        border: 1px solid white;
    }
</style>


