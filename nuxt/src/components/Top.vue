<template>
    <div class="top_wrapper">
        <div class="message_wrapper">
            <h1 class="top_message">Welcome to MusicExplorer, </h1>
            <p class="top_message">
                <input class="top_input_area" type="text" v-model="artist_name" placeholder="search your favorite artists." @keypress.enter="onSubmit">
            </p>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    data(){
        return {
            artist_name: ""
        }
    },
    methods: {
        onSubmit(){
            this.$emit('searchMusic', this.artist_name);
        }
    }
})
</script>
<style scoped>
    .top_wrapper{
        text-align: center;
        padding-top:200px;
    }

    .top_message{
        color:white;
        margin-bottom: 50px;
    }
    .top_input_area{
        width: 30%;
        height: 40px;
        font-size: 20px;
        border-radius: 30px;
        padding: 0px 20px;
    }
</style>
