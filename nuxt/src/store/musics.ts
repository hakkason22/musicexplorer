import { Music } from "~/pages/index.vue";

const state = {
    musics: [] as Array<Music>,
    artist_name: ""
};

const mutations = {
    setMusics(state: any, musics: Array<Music>) {
        state.musics = musics;
    },
    setArtistName(state:any,artist_name:string){
        state.artist_name = artist_name
    }
}

const getters = {
    getMusics(state:any){
        return state.musics
    },
    getArtistName(state:any){
        return state.artist_name
    }
}

const musics = {
    state: state,
    mutations: mutations,
    getters: getters
};

export default musics;
