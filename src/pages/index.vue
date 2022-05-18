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
            music_name: 'ミラーチューン',
            valence: 0.895,
            arousal: 0.933,
            music_url: "0R8JLNP107Hr7V7lL9oh13"
          },
          {
            music_name: 'あいつら全員同窓会',
            valence: 0.913,
            arousal: 0.913,
            music_url: "2VIK6jaaKghS4QPHr6sAkv"
          },
          {
            music_name: "秒針を噛む",
            valence: 0.775,
            arousal: 0.962,
            music_url: "4HgsPAX3MmMgIT60hJ4W4U"
          },
          {
            music_name: '正しくなれない',
            valence: 0.484,
            arousal: 0.679,
            music_url: "2FHexlZenTsS3lsjUYHiDx"
          },
          {
            music_name: '勘冴えて悔しいわ',
            valence: 0.762,
            arousal: 0.924,
            music_url: "7zbfS30vKiHU8oBs6Wi1Qp"
          },
          {
            music_name: '袖のキルト',
            valence: 0.658,
            arousal: 0.813,
            music_url: "7iDC1sNnfChQhMmdBuZmBA"
          },
          {
            music_name: 'お勉強しといてよ',
            valence: 0.868,
            arousal: 0.875,
            music_url: "3sgJTMHqDwxfsBIMqvkXKE"
          },
          {
            music_name: 'ばかじゃないのに',
            valence: 0.739,
            arousal: 0.937,
            music_url: "2UkcZV07LP39NQg9tGBvnh"
          },
          {
            music_name: '猫リセット',
            valence: 0.935,
            arousal: 0.902,
            music_url: "68TwxeHi1pyFDRIKHxSArM"
          },
          {
            music_name: '違う曲にしようよ',
            valence: 0.9,
            arousal: 0.806,
            music_url: "7abFHUH53rYlZwmsjZCvND"
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
