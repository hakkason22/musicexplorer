<template>
  <div>
    <FavariteModal v-if="$store.state.show_favorite_modal_flag" />
    <Header @searchMusic='searchMusics' />
    <ErrorField
      v-if="error_msg!==''"
      :errorMsg="error_msg"
    />
    <div class="container" v-else>
      <Top v-if="target_artist_name == ''"/>
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

export interface Music {
  artist_name: string;
  color: string;
  label_color: string;
  music_id: string;
  music_name: string;
  energy: number;
  valence: number;
}

export default Vue.extend({
    data() {
        return {
            target_artist_name: "",
            target_musics: [] as Array<Music>,
            error_msg: "",
        };
    },
    mounted() {
        this.$store.commit("closeFavoriteModal");
    },
    methods: {
        searchMusics(value: string) {
            //this.error_flag = false;
            const url = `${process.env.BACKEND_ROOT}/music/list`;
            const params = new URLSearchParams();
            params.append("artist_name", value);
            axios.post(url, params).then((response) => {
                console.log(response.data);
                this.target_musics = response.data;
                if ("message" in this.target_musics) {
                    console.log("error");
                    this.error_msg = "アーティストが見つかりませんでした。";
                }
                else {
                    this.error_msg = "";
                    this.target_artist_name = this.target_musics[0]["artist_name"];
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
