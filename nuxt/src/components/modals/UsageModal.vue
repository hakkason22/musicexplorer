<template>
    <div id="usage_container">
        <div id="usage_cards">
            <div class="usage_card">

            </div>
            <!-- /.usage_item -->
            <div class="usage_card">
                
            </div>
            <!-- /.usage_item -->
            <div class="usage_card">
                
            </div>
            <!-- /.usage_item -->
            <div class="usage_card">
                
            </div>
            <!-- /.usage_item -->
        </div>
        <!-- /#usage_card -->
    </div>
    <!-- /#usage -->
</template>
<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
    data(){
        return {
            
        }
    },
    mounted(){
        
    },
    methods:{
        
    }
})
</script>

<style>
    #usage_container{
        color: white;
        height: 100%;
        width: 100%;
    }
    #usage_cards{
        display: flex;
        height: 100%;
        width: 100%;
        flex-wrap: wrap;
    }
    .usage_card{
        height: 46%;
        width: 46%;
        background-color: rgb(60, 50, 50);
        margin: 2%;
    }
</style>
