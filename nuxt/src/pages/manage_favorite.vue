<template>
    <div>
        <Header />
        <DeleteFavoriteModal v-if="$store.state.show_delete_favorite_modal_flag" />
        <div class="container"> 
            <div class="delete_favorite_button_wrapper">
                <span @click="showDeleteFavoriteModal">お気に入り曲を管理</span>
            </div>
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
            error_msg: ""
        }
    },
    mounted(){
        this.getFavoriteMusicInfo()
    },
    methods: {
        getFavoriteMusicInfo(){
            const user_id = this.$store.getters.user.uid
            const url = `${process.env.BACKEND_ROOT}/music/favorite/list`
            const params = new URLSearchParams()
            params.append('user_id', user_id)
            axios.post(url, params).then((response) => {
                if(response.data.result == 0) {
                    this.error_msg = "通信中にエラーが発生しました。"
                }else{
                    this.favoriteMusicInfos= response.data.data
                    console.log(response.data.data)
                }  
            })
        },
        showDeleteFavoriteModal(){
            this.$store.commit('showDeleteFavoriteModal');
        },
    }
})
</script>
<style scoped>
    .container{
        background: black;
        min-height: 120vh;
        opacity: 0.9;
    }
    .delete_favorite_button_wrapper span{
        cursor: pointer;
        background:white;
        padding: 10px;
        margin: 10px;
    }
</style>
