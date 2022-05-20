<template>
  <Main>
    <Header @searchMusic='searchMusics' />
    <Top v-if="target_artist_name == ''"/>
    <ErrorMessage v-else-if="error_flag" />
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
      target_musics: [{}],
      error_flag: false,
    };
  },
  methods: {
    searchMusics(value: string){
      //this.error_flag = false;
      this.target_artist_name = value;

      const url = "http://52.192.42.106/music/list";
      const params = new URLSearchParams();
      params.append('artist_name', this.target_artist_name);
      
          axios.post(url, params).then((response) => {
            
              console.log(response.data);
              this.target_musics = response.data;
              if('message' in this.target_musics){
                this.error_flag = true;
              }
                
            
          });
      
    },
  },
})
</script>
