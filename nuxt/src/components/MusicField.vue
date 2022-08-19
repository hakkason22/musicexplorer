<template>
    <div class="music_field_wrapper">
        <MusicList  
            :music-infos="musicInfos" 
            :artist-name="artistName" 
            @resize="resizeChart"
        />
        <MusicGraphArea 
            :music-infos="musicInfos" 
            :artist-name="artistName"
            ref="graph"
        />
    </div>
</template>
<script lang="ts">
import Vue from "vue";

    export default Vue.extend({
        props: ["musicInfos", "artistName"],
        methods: {
            resizeChart(){
                const graph = this.$refs.graph as any
                graph.preProcess()
            }
        }
    })
</script>
<style scoped>
    .search_result_headding{
        font-size:20px;
    }
</style>
