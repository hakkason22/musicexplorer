<template>
    <div>
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
        getFavoriteMusicInfo(){
            const user_id: string = this.$store.getters.user.uid
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/list`
            const params: any = new URLSearchParams()
            params.append('user_id', user_id)
            axios.post(url, params).then((response) => {
                this.favoriteMusicInfos= response.data.data
                console.log(response.data)
            })
        },
        deleteFavorite(){
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/delete`
            const params: any = new URLSearchParams()
            params.append('favorite_music_ids', this.selectedMusicIds)
            axios.post(url, params).then((response) => {
                console.log(response.data)
            })
            // reload
            location.reload()
        }
    }
})
</script>
