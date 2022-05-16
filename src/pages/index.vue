<template>
  <Main>
    <Header @searchMusic='searchMusics' />
    <Top v-if="target_artist_name == ''"/>
    <MusicField v-else 
      :music-infos="target_musics" 
      :artist-name="target_artist_name"
     />
  </Main>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  data(){
    return {
      target_artist_name: "",
      target_musics: null
    };
  },
  methods: {
    searchMusics(value){
      this.target_artist_name = value;

      // test用
      this.target_musics = [
        {
          music_name: 'lemon',
          valence: 2,
          arousal: 5,
          music_url: "https//...."
        },
        {
          music_name: 'LOSER',
          valence: 4,
          arousal: 1,
          music_url: "https//...."
        },
      ];
    }
  },
})
</script>
