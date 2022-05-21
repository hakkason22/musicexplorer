<template>
    <div class="music_list_wrapper">
        <div class="list_message" >{{ artistName }}
            <span @click="toggle_list">
                <font-awesome-icon v-if="show_flag<0" icon="fa-solid fa-circle-chevron-down" />
                <font-awesome-icon v-else-if="show_flag>0" icon="fa-solid fa-circle-chevron-up" />
            </span>
            <span>
                <font-awesome-icon @click="showFavoriteModal" icon="fa-solid fa-circle-plus" />
            </span>
        </div>
        <div class="music_list" v-if="show_flag>0">
            <div class="music_info" v-for="musicInfo in musicInfos" :key="musicInfo.music_id" @click="displayPlayer(musicInfo.music_id)"  @click.right.prevent="registerFavorite(musicInfo)">
                {{ musicInfo.music_name }}
            </div>
        </div>
    </div>
    
</template>
<script defer src="https://use.fontawesome.com/releases/v5.15.4/js/all.js"></script>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
export default Vue.extend({
    props: ["musicInfos", "artistName"],
    data(){
        return{
            show_flag: -1,
        };
    },
    methods: {
        toggle_list(){
            this.show_flag *= -1;
        },
        registerFavorite(musicInfo){
            if(confirm('「' + musicInfo.music_name + '」 をお気に入り曲に登録しますか？')){
                const url = "http://52.192.42.106/music/favorite/register";
                const params = new URLSearchParams();
                params.append('music_name', musicInfo.music_name);
                params.append('valence', musicInfo.valence);
                params.append('energy', musicInfo.energy);
                params.append('music_id', musicInfo.music_id);
                params.append('user_id', this.$store.getters.user.uid);
                
                axios.post(url, params).then((response) => {
                    console.log(response.data);                    
                });
            }
        },
        displayPlayer(music_id){
            let el = document.getElementById("player_wrapper");
            el.innerHTML =
                    '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/'
                    + music_id
                    + '?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>';

        },
        showFavoriteModal(){
            this.$store.commit('showFavoriteModal');
        }
    }

})
</script>
<style scoped>
    .list_message{
        font-size:22px;
        color:black;
    }
    .list_message span{
        cursor: pointer;
    }

    .music_list{
        display: flex;
        overflow-x: auto;
    }
    .music_info{
        padding:5px 10px;
        background: black;
        color: white;
        margin-bottom: 5px;
        cursor:pointer;
        flex: 0 0 auto;
    }
    .music_info:hover{
        opacity: 0.8;
        background: blue;
    }
    .music_list_wrapper{
        width: 100%;        
    }
</style>
