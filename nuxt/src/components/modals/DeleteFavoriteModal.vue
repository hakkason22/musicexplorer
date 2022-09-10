<template>
    <div>
        <div v-if="favoriteMusicInfos.length === 0">
            <p>お気に入り曲が登録されていません。</p>
        </div>
        <div class="favorite_musics">
            <div class="favorite_music" v-for="favoriteMusicInfo in favoriteMusicInfos" :key="favoriteMusicInfo.music_id">
                <div class="favorite_music_menu">
                    <input type="checkbox" :id="favoriteMusicInfo.music_id" :value="favoriteMusicInfo.favorite_music_id" v-model="selectedMusicIds">
                    <a :href="'https://open.spotify.com/track/' + favoriteMusicInfo.music_id" target="_blank" class="listen_to_spotify">Spotifyで聴く</a>
                </div>
                <iframe
                    style="border-radius:12px"
                    :src="'https://open.spotify.com/embed/track/'+favoriteMusicInfo.music_id+'?utm_source=generator'"
                    width="100%"
                    height="80"
                    frameBorder="0"
                    allowfullscreen=""
                    allow="autoplay; clipboard-write; fullscreen; picture-in-picture">
                </iframe>
            </div>
        </div>
        <div class="submit_field" v-if="favoriteMusicInfos.length > 0 && selectedMusicIds.length > 0">
            <span @click="deleteFavorite">選択したお気に入り曲を削除</span>
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
        async getFavoriteMusicInfo(){
            const user_id: string = this.$store.getters.user.uid
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/list`
            const params: any = new URLSearchParams()
            params.append('user_id', user_id)
            const response = await axios.post(url, params)
            this.favoriteMusicInfos= response.data.data
            console.log(response.data)
        },
        async deleteFavorite(){
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/delete`
            const params: any = new URLSearchParams()
            params.append('favorite_music_ids', this.selectedMusicIds)
            const response = await axios.post(url, params)
            console.log(response.data)
            // reload
            location.reload()
        }
    }
})
</script>
<style scoped>
    .favorite_musics{
        padding: 0 5em;
        overflow-y: scroll;
        height: 60vh;
        align-content: baseline;
    }
    .favorite_music{
        padding: 5px 10px;
        margin: 10px;
    }
    .listen_to_spotify{
        text-decoration: none;
        border-radius: 50px;
        padding: 5px;
        color: white;
        background: black;
        font-size: 14px;
    }
    .favorite_music_menu{
        margin: 5px 0;
    }
</style>
