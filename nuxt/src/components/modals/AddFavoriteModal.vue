<template>
    <div>
        <h2>グラフにお気に入り曲を追加</h2>
        <div class="favorite_infos">
            <div v-if="favoriteMusicInfos.length === 0">
                <p>お気に入り曲が登録されていません。</p>
            </div>
            <div class="favorite_info" v-for="favoriteMusicInfo in favoriteMusicInfos" :key="favoriteMusicInfo.music_id">
                <input type="radio" :id="favoriteMusicInfo.music_id" :value="favoriteMusicInfo.music_id" v-model="selectedMusicId">
                {{ favoriteMusicInfo.music_name }}
            </div>
        </div>
        <div class="submit_field" v-if="favoriteMusicInfos.length > 0">
            <span @click="addChart">追加</span>
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
        getFavoriteMusicInfo(){
            const user_id: string = this.$store.getters.user.uid
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/list`
            const params: any = new URLSearchParams()
            params.append('user_id', user_id)
            axios.post(url, params).then((response) => {
                this.favoriteMusicInfos= response.data.data
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
            this.$emit('closeModal');
        }
    }
})
</script>
