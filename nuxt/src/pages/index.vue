<template>
  <div>
    <FavariteModal v-if="$store.state.show_favorite_modal_flag" />
    <Header @searchMusic='searchMusics' />
    <div class="container">
      <Top v-if="target_artist_name == ''"/>
      <ErrorMessage v-else-if="error_flag" />
      <MusicField v-else 
        :music-infos="target_musics" 
        :artist-name="target_artist_name"
      />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios';

export default Vue.extend({
  data(){
    return {
      target_artist_name: "",
      target_musics: [],
      error_flag: false,
    };
  },
  mounted(){
    this.$store.commit('closeFavoriteModal');
  },
  methods: {
    searchMusics(value: string){
      //this.error_flag = false;

      const url = "http://52.192.42.106/music/list";
      const params = new URLSearchParams();
      params.append('artist_name', value);
      
      axios.post(url, params).then((response) => {
          console.log(response.data);
          this.target_musics = response.data;
          if('message' in this.target_musics){
            console.log("error")
            this.error_flag = true;
            console.log(this.error_flag)
          }else{
            this.target_artist_name = this.target_musics[0]['artist_name'];
          }
      });
      
    },
  },
})
</script>
<style>
  .container{
    background: black;
    min-height: 120vh;
    opacity: 0.9;
  }
</style>
