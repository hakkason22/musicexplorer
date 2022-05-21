<template>
    <div>
        <Header />
        <div class="container"> 
            <MusicGraphArea :music-infos="favoriteMusicInfos" />
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
export default Vue.extend({
    data(){
        return {
            favoriteMusicInfos: [],
        }
    },
    mounted(){
        this.getFavoriteMusicInfo()
    },
    methods: {
        getFavoriteMusicInfo(){
            const user_id = this.$store.getters.user.uid
            const url = "http://52.192.42.106/music/favorite/list"
            const params = new URLSearchParams()
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
        //     ];
        }
    }
})
</script>
<style scoped>
    .container{
        background: black;
        min-height: 120vh;
        opacity: 0.9;
    }
</style>
