<template>
    <div>
        <Header />
        <Modal
            v-if="$store.state.modal.target_modal_type"
            :modal-type="$store.state.modal.target_modal_type"
        />
        <ErrorField
             v-if="error_msg!==''"
             :errorMsg="error_msg"
         />
        <div class="container" v-else> 
            <div class="delete_favorite_button_wrapper">
                <span @click="showDeleteFavoriteModal">お気に入り曲を管理</span>
            </div>
            <MusicGraphArea v-if="favoriteMusicInfos.length > 0"
                :music-infos="favoriteMusicInfos" 
            />
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
import Modal from '../components/modals/Modal.vue'
export default Vue.extend({
    data() {
        return {
            favoriteMusicInfos: [],
            error_msg: ""
        };
    },
    created() {
        this.getFavoriteMusicInfo();
    },
    methods: {
        async getFavoriteMusicInfo() {
            const user_id = this.$store.getters.user.uid;
            const url = `${process.env.BACKEND_ROOT}/music/favorite/list`;
            const params = new URLSearchParams();
            params.append("user_id", user_id);
            const response = await axios.post(url, params)
            
            if (response.data.result == 0) {
                this.error_msg = "通信中にエラーが発生しました。";
            }
            else {
                this.favoriteMusicInfos = response.data.data;
                console.log(response.data.data);
            }
        },
        showDeleteFavoriteModal() {
            this.$store.commit("modal/showModal", "delete-favorite");
        },
    },
    components: { Modal }
})
</script>
<style scoped>
    .container{
        background: black;
        height: 92vh;
        opacity: 0.9;
    }
    .delete_favorite_button_wrapper { 
        position: fixed;
        top: 85px;
        left: 50px;
    }
    .delete_favorite_button_wrapper span{
        cursor: pointer;
        background:white;
        padding: 10px;
        margin: 10px 0;
        border-radius: 50px;
        font-weight: bold;
    }
</style>
