<template>
    <div class="loading_container">
        <div class="loading_area">
            <Loading />
        </div>

    </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    
})
</script>
<style scoped>
    h1{
        color: white;
    }
    .loading_container{
        z-index:1;
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:100%;
        background: black;
        opacity: 0.6;
        display: flex;
        align-items: center;
    }
    .loading_icon, i{
        font-size: 100px;
        color: white;
    }
    .loading_area{
        width:50%;
        height: fit-content;
        margin:0 auto;
        z-index:2;
        opacity: 0.8;
    }
</style>
