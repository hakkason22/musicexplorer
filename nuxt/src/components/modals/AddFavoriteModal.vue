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
        async getFavoriteMusicInfo(){
            const user_id: string = this.$store.getters.user.uid
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/list`
            const params: any = new URLSearchParams()
            params.append('user_id', user_id)
            const response = await axios.post(url, params)
            this.favoriteMusicInfos= response.data.data
            console.log(response.data)
        },
        addChart(){
            const targetMusicInfo = this.favoriteMusicInfos.find(element => element.music_id === this.selectedMusicId)
            this.$nuxt.$emit('addFavoriteToChart', targetMusicInfo)
            this.$emit('closeModal');
        }
    }
})
</script>
