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
import axios from 'axios';

export default Vue.extend({
  data(){
    return {
      target_artist_name: "",
      target_musics: [{}]
    };
  },
  methods: {
    searchMusics(value: string){
      this.target_artist_name = value;

      // const url = "/music/list";
      // const params = new URLSearchParams();
      // params.append('artist_name', this.target_artist_name);
      // axios.post(url, params).then((response) => {
      //   this.target_musics = JSON.parse(response.data);
      // });

      // test用
      if(this.target_artist_name !== "test"){
          this.target_musics = [
          {
            music_name: 'lemon',
            valence: 0.2,
            arousal: 0.5,
            music_url: "https//...1."
          },
          {
            music_name: 'LOSER',
            valence: 0.4,
            arousal: 0.1,
            music_url: "https//....2"
          },
          {
            music_name: this.target_artist_name,
            valence: 0.9,
            arousal: 0.1,
            music_url: "https//....3"
          },
          {
            music_name: '曲４',
            valence: 0,
            arousal: 0,
            music_url: "https//....4"
          },
          {
            music_name: '曲５',
            valence: 1,
            arousal: 1,
            music_url: "https//....5"
          },
          {
            music_name: '曲６',
            valence: 1,
            arousal: 0,
            music_url: "https//....6"
          },
          {
            music_name: '曲７',
            valence: 0,
            arousal: 1,
            music_url: "https//....7"
          },
        ];
      }else{
        this.target_musics = [
          {
            music_name: 'lemon',
            valence: 0.6,
            arousal: 0.2,
            music_url: "https//...1."
          },
          {
            music_name: 'LOSER',
            valence: 0.7,
            arousal: 0.4,
            music_url: "https//....2"
          },]
      }
      
    }
  },
})
</script>
