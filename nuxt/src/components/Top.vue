<template>
    <div class="top_wrapper">
        <div class="message_wrapper">
            <h1 class="top_message">Welcome to MusicExplorer, </h1>
            <p class="top_message">
                <input class="top_input_area" type="text" v-model="artist_name" placeholder="search your favorite artists." @keypress.enter="onSubmit">
            </p>
        </div>

        <div class="recommend_artist_wrapper" v-if="recommend_artists.length > 0">
            <nuxt-link to="/" class="recommend_artist_item" v-for="artist in recommend_artists" :key="artist.id" @click.native="onSubmitFromRecommend(artist.name)">
                <div class="artist_content_wrap">
                    <img :src="artist.image.url" alt="">
                    <h3>{{ artist.name }}</h3>
                </div>
                <!-- /.artist_content_wrap -->
            </nuxt-link>
            <!-- /.recommend_artist_item -->
        </div>
        <div v-else style="height: 50%">
            <!-- loading recommend music -->
        </div>
        <!-- /.recommend_artist_wrapper -->

    </div>
</template>
<script lang="ts">
import axios from 'axios';
import Vue from 'vue'
export default Vue.extend({
    data(){
        return {
            artist_name: "",
            recommend_artists:[]
        }
    },
    methods: {
        onSubmit(){
            this.$emit('searchMusic', this.artist_name);
        },
        onSubmitFromRecommend(artist_name:string){
            console.log(artist_name)
            this.artist_name = artist_name
            this.$emit('searchMusic', this.artist_name);
        },
        async getRecommendArtists(){
            const postParams = new URLSearchParams()
            const url = `${process.env.BACKEND_ROOT}/artist/recommend`
            const user_id = this.$store.getters.isAuthenticated ? this.$store.getters.user.uid:""
            postParams.set('user_id', user_id)
            const res = await axios.post(url,postParams).catch((error)=>{
                throw new Error(error)
            })

            this.recommend_artists = res.data
        }
    },
    mounted: function(){
        this.getRecommendArtists()
    }
})
</script>
<style scoped>
    .top_wrapper{
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: center;
        height: 100%;
        width: 100%;
    }

    .top_message{
        color:white;
        margin-bottom: 50px;
    }
    .top_input_area{
        width: 30%;
        height: 40px;
        font-size: 20px;
        border-radius: 30px;
        padding: 0px 20px;
    }

    .recommend_artist_wrapper{
        display: flex;
        width: 90%;
        max-height: 90%;
        margin: 30px auto;
        padding-bottom: 12px;
        overflow-x: scroll;
    }
    .recommend_artist_item{
        width: 22%;
        padding-top: 22%;
        position: relative;
        margin-right: 15px;

        background-color: rgb(34, 29, 29);
        flex-shrink: 0;
        max-height: 90%;
        color: white;
        list-style: none;
        border-radius: 10px;
        box-shadow: 2px 2px 1px 1px black;
    }

    .recommend_artist_wrapper a:last-child{
        margin-right: 0;
    }

    .recommend_artist_wrapper::-webkit-scrollbar {
    height: 14px; /* スクロールバーの高さ */
    }
    
    .recommend_artist_wrapper::-webkit-scrollbar-thumb {
    background: rgb(160, 77, 228); /* ツマミの色 */
    border-radius: 7px; /* ツマミ両端の丸み */
    }
    
    .recommend_artist_wrapper::-webkit-scrollbar-track {
    background: rgba(160, 77, 228, 0.388); /* トラックの色 */
    border-radius: 7px; /* トラック両端の丸み */
    }

    .artist_content_wrap{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
    }

    .artist_content_wrap img{
        width: 50%;
        height: 50%;
        margin-top: 20px;

        border-radius: 10px;
        background-color: black;
    }
</style>
