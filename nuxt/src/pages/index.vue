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
        v-if="target_artist_name == ''"
        @searchMusic='searchMusics'
      />
      <MusicField v-else 
        :music-infos="target_musics" 
        :artist-name="target_artist_name"
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
    mounted() {
        this.$store.commit("modal/closeModal");
    },
    methods: {
        searchMusics(value: string) {
            this.$store.commit("loading/loading_state", true);
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
                this.$store.commit("loading/loading_state", false);
            });
        },
    },
    components: { Modal }
})
</script>
<style>
  .container{
    background: black;
    min-height: 92vh;
    opacity: 0.9;
  }
</style>
