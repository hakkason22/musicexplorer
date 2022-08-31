<template>
    <div id="usage_container">
        <div id="usage_cards">
            <div id='usage_1' class="usage_card" v-show="$store.getters['usage/show_usage_page'](1)">
                <h1>1</h1>
            </div>
            <!-- /.usage_item -->
            <div id='usage_2' class="usage_card" v-show="$store.getters['usage/show_usage_page'](2)">
                <h1>2</h1>
            </div>
            <!-- /.usage_item -->
            <div id='usage_3' class="usage_card" v-show="$store.getters['usage/show_usage_page'](3)">
                <h1>3</h1>
            </div>
            <!-- /.usage_item -->
            <div id='usage_4' class="usage_card" v-show="$store.getters['usage/show_usage_page'](4)">
                <h1>4</h1>
            </div>
            <!-- /.usage_item -->
        </div>
        <!-- /#usage_card -->
        <div id="usage_pagination">
            <div id="back_page" class="usage_pagination_item" @click="back_usage_page"></div>
            <!-- /.usage_pagination_item -->
            <div id="next_page" class="usage_pagination_item" @click="next_usage_page"></div>
            <!-- /.usage_pagination_item -->
        </div>
        <!-- /#usage_paging -->
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
        next_usage_page(){
            this.$store.commit("usage/next_usage_page")
            console.log(this.$store.state.usage.usage_page)
        },
        back_usage_page(){
            this.$store.commit("usage/back_usage_page")
            console.log(this.$store.state.usage.usage_page)
        }
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
        height: 90%;
        width: 100%;
        flex-wrap: wrap;
    }
    .usage_card{
        height: 100%;
        width: 100%;
        background-color: rgb(60, 50, 50);
    }

    #usage_pagination{
        display: flex;
        height: 10%;
        width: 100%;
        align-items: center;
        justify-content: center;
    }
    .usage_pagination_item{
        height: 100%;
        width: 40%;
        background-color: red;
        margin: 5%;
    }
</style>
