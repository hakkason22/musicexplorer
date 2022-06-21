<template>
    <div class="modal_wrapper">
        <div class="favorite_music_wrapper">
            <div class="close_button">
                <font-awesome-icon icon="fa-solid fa-xmark" class="close_icon" @click="closeFavoriteModal" />
            </div>
            <div class="favorite_list_field">
                <div class="favorite_infos">
                    <div class="favorite_info" v-for="favoriteMusicInfo in favoriteMusicInfos" :key="favoriteMusicInfo.music_id">
                        <input type="checkbox" :id="favoriteMusicInfo.music_id" :value="favoriteMusicInfo.favorite_music_id" v-model="selectedMusicIds">
                        {{ favoriteMusicInfo.music_name }}
                    </div>
                </div>
                <div class="submit_field">
                    <span @click="deleteFavorite">選択した曲をお気に入りから削除</span>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

type musicInfos = {
    music_id: string,
    music_name: string,
    valence: number,
    energy: number,
    favorite_music_id: number,
}

export type datatype = {
    favoriteMusicInfos: musicInfos[],
    selectedMusicIds: string[]
}

export default Vue.extend({
    data(): datatype{
        return {
            favoriteMusicInfos: [],
            selectedMusicIds: [],
        }
    },
    mounted(){
        this.getFavoriteMusicInfo()

    },
    methods:{
        closeFavoriteModal(){
            this.$store.commit('closeFavoriteModal');
        },
        getFavoriteMusicInfo(){
            const user_id: string = this.$store.getters.user.uid
            const url: string = "http://localhost:5000/music/favorite/list"
            const params: any = new URLSearchParams()
            params.append('user_id', user_id)
            axios.post(url, params).then((response) => {
                this.favoriteMusicInfos= response.data
                console.log(response.data)
            })
        },
        deleteFavorite(){
            const url: string = "http://localhost:5000/music/favorite/delete"
            const params: any = new URLSearchParams()
            params.append('favorite_music_ids', this.selectedMusicIds)
            axios.post(url, params).then((response) => {
                console.log(response.data)
            })
            // reload
            this.$router.go({path: this.$router.currentRoute.path, force: true})
        }
    }
})
</script>
<style scoped>
    .modal_wrapper{
        z-index:1;
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:120%;
        background-color:rgba(0,0,0,0.75);
    }
    .favorite_music_wrapper{
        width:50%;
        margin:5em auto 0;
        border:2px solid #aaa;
        background:#fff;
        z-index:2;
        height: 600px;
        /* border-radius:20px; */
        overflow-y: scroll;
    }
    .close_button{
        display: flex;

    }
    .close_icon{
        font-size:24px;
        border-radius: 50%;
        background: grey;
        padding:5px 10px;
        color:white;
        position: absolute;
        right: 25%;
        cursor: pointer;
    }
    .favorite_list_field{
        padding: 30px;
    }
    .favorite_list_field h2{
        text-align: center;
    }
    .favorite_infos{
        display: flex;
        flex-wrap: wrap;
        margin-top:5em;
    }
    .favorite_info{
        border-radius: 30px;
        border: 2px solid black;
        padding: 5px 10px;
        margin: 10px;
    }
    .submit_field{
        text-align: center;
        margin-top: 50px;
    }
    .submit_field span{
        padding: 10px 20px;
        border-radius: 20px;
        background: blue;
        color: white;
        cursor: pointer;
    }
    .submit_field span:hover{
        opacity: 0.8;
    }
</style>
