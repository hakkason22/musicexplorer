<template>
    <div class="player_wrapper">
        <div class="player_area">
            <iframe
                style="border-radius:12px"
                :src="'https://open.spotify.com/embed/track/'+$store.state.player.target_music_id+'?utm_source=generator'"
                width="100%"
                height="80"
                frameBorder="0"
                allowfullscreen=""
                allow="autoplay; clipboard-write; fullscreen; picture-in-picture">
            </iframe>
        </div>
        <div class="favorite_area">
            <span 
                v-if="$store.state.player.target_is_favorite"
                class="favorite_icon faved"
                @click="deleteFavorite"
            >
                    ★
            </span>
            <span 
                v-else
                @click="registerFavorite"
                class="favorite_icon not_faved"
            >
                    ☆
            </span>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
export default Vue.extend({
    methods: {
        async registerFavorite() {
            if (!this.$store.getters.isAuthenticated) {
                this.$store.commit("modal/showModal", "login-induction");
            }
            else {
                const url = `${process.env.BACKEND_ROOT}/music/favorite/register`;
                const params = new URLSearchParams();
                params.append("music_name", this.$store.state.player.target_music_name);
                params.append("valence", String(this.$store.state.player.target_valence));
                params.append("energy", String(this.$store.state.player.target_energy));
                params.append("music_id", this.$store.state.player.target_music_id);
                params.append("user_id", this.$store.getters.user.uid);
                const response = await axios.post(url, params);
                console.log(response.data);
                this.$store.commit("player/setPlayerFavorite", true);
                console.log(this.$store.state.player.is_favorite);
                this.$emit('setFavoriteMusicInfo');
            }
        },
        
    }
})
</script>
<style scoped>
    .player_wrapper{
        position: fixed;
        bottom: 3%;
        left: 0;
        right: 0;
        margin: auto;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .player_area{
        width: 40%;
    }
    .favorite_area{
        padding-left: 10px;
    }
    .favorite_icon{
        font-weight: bold;
        border-radius: 50%;
        padding: 10px;
        font-size: 18px;
    }
    .faved{
        color: black;
        background: lightgray;
        cursor: default;
    }
    .not_faved{
        background: white;
        cursor: pointer;
    }
</style>
