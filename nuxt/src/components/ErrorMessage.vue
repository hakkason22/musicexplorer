<template>
    <h1 class="error_message">error!!!</h1>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    mounted(){
        console.log("error_massage")
    }
})
</script>
<style scoped>
    .error_message{
        color: white;
    }
</style>
