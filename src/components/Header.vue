<template>
<div class="header_container">
    <div class="header_logo_wrapper">
        <h2>MusicExplorer</h2>
    </div>
    <div class="menu_wrapper">
        <input type="text" v-model="artist_name" placeholder="artist name" @keypress.enter="onSubmit">
    </div>
    
</div>
</template>
<style>
    body{
        margin:0;
        padding:0;
    }
    .header_container{
        display: flex;
        justify-content: space-between;
        background: blue;
        padding:0 40px;
    }
    .header_logo_wrapper{
        color: white;
    }
    .menu_wrapper{
        display: flex;
        align-items: center;
    }
    .menu_wrapper input{
        font-size:20px;
    }
    
</style>

<script lang="ts">
    import Vue from "vue";

    export default Vue.extend({
        data(){
            return {
                artist_name: ""
            };
        },
        methods: {
            created(){
                console.log("test");
            },
            onSubmit(){
                this.$emit('artist_name', this.artist_name);
            }
        }
    })
</script>
