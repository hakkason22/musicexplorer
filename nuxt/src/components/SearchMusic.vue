<template>
    <div class="search_music_wrapper">
        <input type="text" v-model="search_music_name" @keypress.enter="searchMusic" placeholder="マップ内検索">
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import { Music } from '../pages/index.vue'
export default Vue.extend({
    data() {
        return {
            search_music_name: '',
        }
    },
    methods: {
        searchMusic() {
            let is_matched: boolean = false
            this.$store.state.musics.musics.forEach((musicInfo: Music) => {
                if(musicInfo.music_name.indexOf(this.search_music_name) !== -1) {
                    this.$emit('displayDetail', musicInfo)
                    is_matched = true
                }
            })
            if(is_matched === false){
                this.search_music_name = "該当なし"
            }
        }
    }
})
</script>
<style scoped>
    .search_music_wrapper{
        position: fixed;
        top: 15%;
        left: 2.4%;
        margin: auto;
    }
    .search_music_wrapper input{
        font-size: 18px;
        padding: 3px;
        border-radius: 5px;
    }
</style>
