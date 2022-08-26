<template>
    <div class="menu_wrapper">
        <div class="nav">
            <div class="main_menu_wrapper">
                <div class="artist_name_wrapper" >
                    {{ artistName }}
                </div>
                <div class="list_message">
                    <span>
                        <font-awesome-icon 
                            @click="showFavoriteModal" 
                            icon="fa-solid fa-circle-chevron-down" 
                        />
                    </span>
                    <span>
                        <font-awesome-icon
                            @click="resize"
                            icon="fa-solid fa-expand" 
                            class="resize_icon"
                        />
                    </span>
                </div>
            </div>
            <!-- /.main_menu -->
            <div class="sub_menu_wrapper">
                <div class = "sub_menu_item">
                    <a href="#" class="recommend_button" @click="toggleRecommendArtist">
                        おすすめアーティスト
                        <font-awesome-icon v-if="show_recommend" icon="fa-solid fa-angle-up" />
                         <font-awesome-icon v-else icon="fa-solid fa-angle-down" />
                    </a>
                </div>
            </div>
            <!-- /.sub_menu_wrapper -->
        </div>
        <!-- /.nav -->
        <div class="recommend_artist_wrapper" v-if="recommend_artists.length > 0 && show_recommend">
            <nuxt-link to="/" class="recommend_artist_item" v-for="artist in recommend_artists" :key="artist.id" @click.native="searchMusics(artist.name)">
                <div class="artist_content_wrap">
                    <img :src="artist.image.url" alt="">
                    <div>{{ artist.name }}</div>
                </div>
                <!-- /.artist_content_wrap -->
            </nuxt-link>
            <!-- /.recommend_artist_item -->
        </div>
    </div>
    
</template>
<script defer src="https://use.fontawesome.com/releases/v5.15.4/js/all.js"></script>
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
export default Vue.extend({
    props: ["musicInfos", "artistName"],
    data(){
        return{
            show_flag: 1,
            recommend_artists:[],
            show_recommend:false,
        };
    },
    methods: {
        toggle_list(){
            this.show_flag *= -1;
        },
        displayPlayer(music_id: string){
            let el: any = document.getElementById("player_wrapper");
            el.innerHTML =
                    '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/'
                    + music_id
                    + '?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>';

        },
        showFavoriteModal(){
            if(!this.$store.getters.isAuthenticated) {
                this.$store.commit("modal/showModal", "login-induction");
            }else{
                this.$store.commit('modal/showModal', 'add-favorite');
            }
        },
        resize() {
            this.$emit('resize')
        },
        searchMusics(artist_name:string){
            console.log(artist_name)
            this.$emit('searchMusics', artist_name);
            this.show_recommend = false
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
        },
        toggleRecommendArtist(){
            if(this.show_recommend){
                this.show_recommend = false
            }else{
                this.show_recommend = true
            }
        }
    },
    mounted: function(){
        this.getRecommendArtists()
    }

})
</script>
<style scoped>
    .menu_wrapper{
        display: flex;
        position: fixed;
        flex-direction: column;
        width: 95%;
        top: 10%;
        left: 0;
        right: 0;
        margin: auto;
    }
    .nav{
        width: 100%;
        height: 5%;
        text-align: center;
        display: flex;
    }
    .main_menu_wrapper{
        width: 30%;
        height: 100%;
        text-align: left;
    }
    .list_message, .artist_name_wrapper{
        font-size:22px;
        color:black;
        padding:0 10px;
        display: inline-block;
        border-radius: 5px;
        background: #fff;
    }
    .list_message span{
        cursor: pointer;
    }

    .music_list{
        display: flex;
        overflow-x: auto;
    }
    .music_info{
        background: black;
        color: white;
        cursor:pointer;
        flex: 0 0 auto;
        margin-top:5px;
    }
    .music_info:hover{
        opacity: 0.8;
        background: blue;
    }

    .sub_menu_wrapper{
        width: 70%;
        height: 100%;
        text-align: right;
    }

    .recommend_button{
        color: rgba(255, 255, 255);
        text-decoration: none;
        padding: 0.2rem;
        border: solid;
        border-color: rgb(252, 250, 250);
        border-radius: 5px;
        background-color: rgb(0, 0, 0, 0.8);
    }

    .recommend:hover{
        color: rgb(181, 181, 181);
    }

    .close_recommend:after {
        content: '';
        display: inline-block;
        width: 6px;
        height: 6px;
        margin: 0 0 0 15px;
        border-right: 1px solid #fff;
        border-bottom: 1px solid #fff;
        -webkit-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
        transform: rotate(45deg);
    }

    .open_recommend:after {
        content: '';
        display: inline-block;
        width: 6px;
        height: 6px;
        margin: 0 0 0 15px;
        border-right: 1px solid #fff;
        border-bottom: 1px solid #fff;
        -webkit-transform: rotate(225deg);
        -ms-transform: rotate(225deg);
        transform: rotate(225deg);
    }
    
    .recommend_artist_wrapper{
        display: flex;
        width: 100%;
        max-height: 90%;
        padding-top: 10px;
        padding-bottom: 12px;
        margin-bottom: 12px;
        overflow-x: scroll;
        text-align: center;
    }
    .recommend_artist_item{
        width: 12%;
        padding-top: 12%;
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

    .recommend_artist_wrapper::after{
        height: 50px;
        width: 50px;
        background-color: red;
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
        font-size: 1.2vw;
    }

    .artist_content_wrap img{
        width: 50%;
        height: 50%;
        margin-top: 20px;

        border-radius: 10px;
        background-color: black;
    }
    .artist_content_wrap div{
        padding: 0 5px;
    }
</style>
