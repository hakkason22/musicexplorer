const state = {
    target_music_id: "" as string,
    target_music_name: "" as string,
    target_display_music_name: "" as string,
    target_valence: -1 as number,
    target_energy: -1 as number,
    target_is_favorite: false as boolean,
};

const mutations = {
    setMusic(state: any, music: any){
        state.target_music_id = music.music_id;
        state.target_music_name = music.music_name;
        state.target_display_music_name = music.display_music_name;
        state.target_valence = music.valence;
        state.target_energy = music.energy;
        state.target_is_favorite = music.is_favorite;
    },
    setPlayerFavorite(state: any, is_favorite: boolean) {
        state.target_is_favorite = is_favorite
    }
};

const player = {
    state: state,
    mutations: mutations,
};

export default player;
