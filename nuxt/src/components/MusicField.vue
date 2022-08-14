<template>
    <div class="music_field_wrapper">
        <MusicList  :music-infos="musicInfos" :artist-name="artistName" />
        <MusicGraphArea :music-infos="musicInfos" :artist-name="artistName" />
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
        padding: 30px 0;
    }
    .search_result_headding{
        font-size:20px;
    }
</style>
