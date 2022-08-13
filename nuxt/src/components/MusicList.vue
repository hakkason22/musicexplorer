<template>
    <div class="music_list_wrapper">
        <div class="list_message" >{{ artistName }}
            <span>
                <font-awesome-icon @click="showFavoriteModal" icon="fa-solid fa-circle-chevron-down" />
            </span>
        </div>
    </div>
    
</template>
<script defer src="https://use.fontawesome.com/releases/v5.15.4/js/all.js"></script>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
import { Music } from '../pages/index.vue'
export default Vue.extend({
    props: ["musicInfos", "artistName"],
    data(){
        return{
            show_flag: 1,
        };
    },
    methods: {
        toggle_list(){
            this.show_flag *= -1;
        },
        registerFavorite(musicInfo: Music){
            if(!this.$store.getters.isAuthenticated) {
                this.$store.commit("modal/showModal", "login-induction");
            }else{
                if(confirm('「' + musicInfo.music_name + '」 をお気に入り曲に登録しますか？')){
                    const url = `${process.env.BACKEND_ROOT}/music/favorite/register`;
                    const params = new URLSearchParams();
                    params.append('music_name', musicInfo.music_name);
                    params.append('valence', String(musicInfo.valence));
                    params.append('energy', String(musicInfo.energy));
                    params.append('music_id', musicInfo.music_id);
                    params.append('user_id', this.$store.getters.user.uid);
                    
                    axios.post(url, params).then((response) => {
                        console.log(response.data);                    
                    });
                }
            }
        },
        displayPlayer(music_id: string){
            let el: any = document.getElementById("player_wrapper");
            el.innerHTML =
                    '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/'
                    + music_id
                    + '?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>';

        },
        showFavoriteModal(){
            if(!this.$store.getters.isAuthenticated) {
                this.$store.commit("modal/showModal", "login-induction");
            }else{
                this.$store.commit('modal/showModal', 'add-favorite');
            }
        },
    }

})
</script>
<style scoped>
    .list_message{
        font-size:22px;
        color:black;
        padding:0 10px;
        display: inline-block;
        border-radius: 30px;
        background: #fff;
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
        cursor:pointer;
        flex: 0 0 auto;
        margin-top:5px;
    }
    .music_info:hover{
        opacity: 0.8;
        background: blue;
    }
    .music_list_wrapper{
        width: 90vw;
        margin: 0 auto;        
    }
</style>
