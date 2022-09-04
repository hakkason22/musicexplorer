<template>
  <div>
    <Modal
      v-if="$store.state.modal.target_modal_type!==''"
      :modal-type="$store.state.modal.target_modal_type"
    />
    <Header @searchMusic='searchMusics' />
    <ErrorField
      v-if="error_msg!==''"
      :errorMsg="error_msg"
    />
    <div class="container" v-else>
      <Top 
        v-if="!$route.query.target_artist"
        @searchMusics='searchMusics'
      />
      <MusicField v-else 
        :music-infos="$store.getters['musics/getMusics']" 
        :artist-name="$store.getters['musics/getArtistName']"
        @searchMusics='searchMusics'
      />
    </div>
    <LoadingField v-if="$store.state.loading.loading_state" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios';
import Modal from '../components/modals/Modal.vue';

export interface Music {
  artist_name: string;
  music_id: string;
  music_name: string;
  energy: number;
  valence: number;
  display_music_name: string;
  graph_color: string;
  is_favorite: boolean;
}

export default Vue.extend({
    data() {
        return {
            target_artist_name: "",
            target_musics: [] as Array<Music>,
            error_msg: "",
            is_loading: false,
        };
    },
    fetch(){
      if (this.$route.query.target_artist && !this.$store.getters['musics/getArtistName']){
        this.searchMusics(this.$route.query.target_artist as string)
      }
    },
    mounted() {
        this.$store.commit("modal/closeModal");
    },  
    methods: {
        async searchMusics(value: string) {
            this.$store.commit("loading/loading_state", true);
            const url = `${process.env.BACKEND_ROOT}/music/list`;
            const params = new URLSearchParams();
            params.append("artist_name", value);
            const response = await axios.post(url, params)
            console.log(response.data);
            
            if ("message" in response.data) {
                console.log("error");
                this.error_msg = "アーティストが見つかりませんでした。";
            }
            else {
                this.error_msg = "";
                if(this.target_artist_name !== response.data[0]["artist_name"]) {
                  this.$store.commit("musics/setMusics",response.data)
                  this.target_artist_name = response.data[0]["artist_name"]
                  this.$store.commit("musics/setArtistName",response.data[0]["artist_name"])
                }
            }
            this.$store.commit("recommend/setShowRecommend", false)
            this.$store.commit("loading/loading_state", false);
            this.$router.push({ path: '/',query:{target_artist : this.target_artist_name} })
        },
    },
    components: { Modal }
})
</script>
<style>
  .container{
    background: radial-gradient(midnightblue, #010007);
    height: 92vh;
    opacity: 0.9;
  }
</style>
