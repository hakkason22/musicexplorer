<template>
    <div class="modal_wrapper">
        <div :class="modalClass">
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
                <LoginInductionModal
                    v-else-if="modalType==='login-induction'"
                />
                <UsageModal
                    v-else-if="modalType==='usage'"
                />
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import DeleteFavoriteModal from './DeleteFavoriteModal.vue';
import AddFavoriteModal from './AddFavoriteModal.vue';
import LoginInductionModal from './LoginInductionModal.vue';
import UsageModal from './UsageModal.vue';

export default Vue.extend({
    props:["modalType"],
    data() {
        return {
            modalClass: "modal_message_wrapper_transparence"
        }
    },
    methods: {
        closeModal(){
            this.$store.commit('modal/closeModal');
        },
    },
    components:{
        DeleteFavoriteModal,
        AddFavoriteModal,
        LoginInductionModal,
        UsageModal
    },
    mounted() {
        console.log(this.modalType)
        if(this.modalType === 'add-favorite' || this.modalType === 'delete-favorite') {
            this.modalClass = "modal_message_wrapper"
        }
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
    .modal_message_wrapper{
        width:50%;
        margin:5em auto 0;
        border:2px solid #aaa;
        background:#fff;
        z-index:2;
        height: 60%;
        border-radius:20px;
    }
    .modal_message_wrapper_transparence{
        width:50%;
        margin:5em auto 0;
        z-index:2;
        height: 60%;
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
        right: 23%;
        top: 5%;
        cursor: pointer;
    }
    .modal_field{
        padding: 30px;
        position: relative;
        height: 85%;
    }
    .modal_field h2{
        text-align: center;
    }
    .favorite_infos{
        display: flex;
        flex-wrap: wrap;
        margin-top:3em;
        padding: 0 5em;
        overflow-y: scroll;
        height: 43vh;
        align-content: baseline;
    }
    .favorite_info{
        border-radius: 30px;
        border: 2px solid black;
        padding: 5px 10px;
        margin: 10px;
        height: 1.5em;
    }
    .submit_field{
        text-align: center;
        margin-top: 50px;
        position: absolute;
        bottom: 0;
        right: 0;
        left: 0;
    }
    .submit_field span{
        padding: 10px 20px;
        border-radius: 20px;
        background: black;
        color: white;
        cursor: pointer;
    }
    .submit_field span:hover{
        opacity: 0.8;
    }
</style>
