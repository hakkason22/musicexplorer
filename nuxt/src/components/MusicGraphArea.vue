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
                :fill="normal_color"
                @click="displayDetail(musicInfo)"
                :font-size="chart_font_size"
                class="graph_element"
        >{{ musicInfo.display_music_name }}</text>
        <text v-for="favoriteMusicInfo in favoriteMusicInfos" :key="favoriteMusicInfo.music_id"
                :x="favoriteMusicInfo['valence'] * (chart_width-100) + 100"
                :y="(1 - favoriteMusicInfo['energy']) * (chart_height-100) + 100"
                :fill="favorite_color"
                @click="displayDetail(favoriteMusicInfo)"
                :font-size="chart_font_size"
                class="graph_element"
        >{{ favoriteMusicInfo.music_name }}</text>
        <text v-if="$store.state.player.target_music_id!==''"
                :x="$store.state.player.target_valence * (chart_width-100) + 100"
                :y="(1 - $store.state.player.target_energy) * (chart_height-100) + 100"
                :fill="playing_color"
                :font-size="chart_font_size"
                class="graph_element"
        >{{ $store.state.player.target_display_music_name }}</text>
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
            <span @click="registerFavorite">＋</span>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from 'axios'
import Vue from 'vue'
import { Music } from '../pages/index.vue'

export default Vue.extend({
    props: ["musicInfos"],
    data(){
        return {
            chart_width: 1300,
            chart_height: 1020,
            chart_min_width: 0,
            chart_min_height: 0,
            chart_font_size: 14,
            favorite_music_id_list: [] as Array<string>,
            normal_color: "white",
            favorite_color: "#00fa9a",
            playing_color: "red",
            favoriteMusicInfos: [] as Array<Music>,
            playingMusicInfo: {} as Music,
        };
    },
    mounted() {
        this.preProcess();
        this.$nuxt.$on('addFavoriteToChart', this.addUpdateData);
    },
    watch:{
        musicInfos: function(){
            this.preProcess();
        }
    },  
    methods: {
        preProcess(){
            this.chart_width = window.innerWidth - 200;
            this.chart_height = window.innerHeight - 200;

            this.musicInfos.forEach((musicInfo: Music) => {
                if(musicInfo.music_name.length < 10){
                    musicInfo.display_music_name = musicInfo.music_name;
                }else{
                    musicInfo.display_music_name = musicInfo.music_name.slice(0, 9) + "...";
                }
            })
        },
        addUpdateData(targetMusicInfo: Music){
            this.favoriteMusicInfos.push(targetMusicInfo);
        },
        displayDetail(music: Music){
            //this.playingMusicInfo = music;
            this.$store.commit('player/setMusic', music);
            console.log(this.$store.state.player.target_music_name)
        },
        registerFavorite(){
            if(!this.$store.getters.isAuthenticated) {
                this.$store.commit("modal/showModal", "login-induction");
            }else{
                if(confirm('「' + this.$store.state.player.target_music_name + '」 をお気に入り曲に登録しますか？')){
                    const url = `${process.env.BACKEND_ROOT}/music/favorite/register`;
                    const params = new URLSearchParams();
                    params.append('music_name', this.$store.state.player.target_music_name);
                    params.append('valence', String(this.$store.state.player.target_valence));
                    params.append('energy', String(this.$store.state.player.target_energy));
                    params.append('music_id', this.$store.state.player.target_music_id);
                    params.append('user_id', this.$store.getters.user.uid);
                    
                    axios.post(url, params).then((response) => {
                        console.log(response.data);                    
                    });
                }
            }
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
    .favorite_area span{
        color: black;
        font-weight: bold;
        background: white;
        border-radius: 50%;
        padding: 10px;
        font-size: 18px;
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


