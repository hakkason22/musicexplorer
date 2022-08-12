<template>
    <div class="modal_wrapper">
        <div class="favorite_music_wrapper">
            <div class="close_button">
                <font-awesome-icon icon="fa-solid fa-xmark" class="close_icon" @click="closeModal" />
            </div>
            <div class="modal_field">
                <AddFavoriteModal
                    v-if="modalType==='add-favorite'"
                    @closeModal="closeModal"
                />
                <DeleteFavoriteModal
                    v-else-if="modalType==='delete-favorite'"
                />
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import DeleteFavoriteModal from './DeleteFavoriteModal.vue';
import AddFavoriteModal from './AddFavariteModal.vue';

export default Vue.extend({
    props:["modalType"],
    mounted(){
        console.log(this.modalType)
    },
    methods: {
        closeModal(){
            this.$store.commit('modal/closeModal');
        },
    },
    components:{
        DeleteFavoriteModal,
        AddFavoriteModal
    }
})
</script>
<style>
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
        border-radius:20px;
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
    .modal_field{
        padding: 30px;
    }
    .modal_field h2{
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
