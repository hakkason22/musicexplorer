<template>
    <div class="music_field_wrapper">
        <MusicList  :music-infos="musicInfos" :artist-name="artistName" />
        <MusicGraphArea :music-infos="musicInfos" />
    </div>
</template>
<script lang="ts">
    import Vue from "vue";

    export default Vue.extend({
        props: ["musicInfos", "artistName"],
    })
</script>
<style scoped>
    .music_field_wrapper{
        margin: 30px;
    }
    .search_result_headding{
        font-size:20px;
    }
</style>
