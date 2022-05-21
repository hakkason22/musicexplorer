<template>
    <div class="modal_wrapper">
        <div class="favorite_music_wrapper">
            <div class="close_button">
                <font-awesome-icon icon="fa-solid fa-xmark" class="close_icon" @click="closeFavoriteModal" />
            </div>
            <div class="favorite_list_field">
                <h2>グラフにお気に入り曲を追加</h2>
                <div class="favorite_infos">
                    <div class="favorite_info" v-for="favoriteMusicInfo in favoriteMusicInfos" :key="favoriteMusicInfo.music_id">
                        <input type="radio" :id="favoriteMusicInfo.music_id" :value="favoriteMusicInfo.music_id" v-model="selectedMusicId">
                        {{ favoriteMusicInfo.music_name }}
                    </div>
                </div>
                <div class="submit_field">
                    <span @click="addChart">追加</span>
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

}

export type datatype = {
    favoriteMusicInfos: musicInfos[],
    selectedMusicId: string
}

export default Vue.extend({
    data(): datatype{
        return {
            favoriteMusicInfos: [],
            selectedMusicId: "",
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
            const url: string = "http://52.192.42.106/music/favorite/list"
            const params: any = new URLSearchParams()
            params.append('user_id', user_id)
            axios.post(url, params).then((response) => {
                this.favoriteMusicInfos= response.data
                console.log(response.data)
            })

        //     this.favoriteMusicInfos = [
        //   {
        //     music_name: 'ミラーチューン',
        //     valence: 0.895,
        //     energy: 0.933,
        //     music_id: "0R8JLNP107Hr7V7lL9oh13"
        //   },
        //   {
        //     music_name: 'あいつら全員同窓会',
        //     valence: 0.913,
        //     energy: 0.913,
        //     music_id: "2VIK6jaaKghS4QPHr6sAkv"
        //   },
        //   {
        //     music_name: "秒針を噛む",
        //     valence: 0.775,
        //     energy: 0.962,
        //     music_id: "4HgsPAX3MmMgIT60hJ4W4U"
        //   },
        //   {
        //     music_name: '正しくなれない',
        //     valence: 0.484,
        //     energy: 0.679,
        //     music_id: "2FHexlZenTsS3lsjUYHiDx"
        //   },
        //   {
        //     music_name: '勘冴えて悔しいわ',
        //     valence: 0.762,
        //     energy: 0.924,
        //     music_id: "7zbfS30vKiHU8oBs6Wi1Qp"
        //   },
        //   {
        //     music_name: '袖のキルト',
        //     valence: 0.658,
        //     energy: 0.813,
        //     music_id: "7iDC1sNnfChQhMmdBuZmBA"
        //   },
        //   {
        //     music_name: 'お勉強しといてよ',
        //     valence: 0.868,
        //     energy: 0.875,
        //     music_id: "3sgJTMHqDwxfsBIMqvkXKE"
        //   },
        //   {
        //     music_name: 'ばかじゃないのに',
        //     valence: 0.739,
        //     energy: 0.937,
        //     music_id: "2UkcZV07LP39NQg9tGBvnh"
        //   },
        //   {
        //     music_name: '猫リセット',
        //     valence: 0.935,
        //     energy: 0.902,
        //     music_id: "68TwxeHi1pyFDRIKHxSArM"
        //   },
        //   {
        //     music_name: '違う曲にしようよ',
        //     valence: 0.9,
        //     energy: 0.806,
        //     music_id: "7abFHUH53rYlZwmsjZCvND"
        //   },
        // ];
        },
        addChart(){
            const targetMusicInfo = this.favoriteMusicInfos.find(element => element.music_id === this.selectedMusicId)
            this.$nuxt.$emit('addFavoriteToChart', targetMusicInfo)
            this.closeFavoriteModal()
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
        min-height: 600px;
        border-radius:20px;
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
