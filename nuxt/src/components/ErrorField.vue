<template>
    <div class="error_container">
        <div class="error_message_field">
            <div>
                <h1>{{ errorMsg }}</h1>
                <p><a href="/">TOPへ戻る</a></p>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    props:["errorMsg"],
    data(){
        return {
            
        }
    }
    
})
</script>
<style scoped>
    .error_container{
        background: rgba(0, 0, 0, 0.8);
        height: 100vh;
    }
    .error_message_field {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
        width: 60%;
        height: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: black;
    }
    .error_message_field h1, .error_message_field p{
        color: white;
        text-align: center;
    }
    .error_message_field p a{
        color: white;
        text-decoration: none;
        padding: 5px 10px;
        border: 1px solid white;
    }
</style>
