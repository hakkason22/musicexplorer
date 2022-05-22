import { getAuth, signInWithPopup, GoogleAuthProvider, signOut } from "firebase/auth";

export const strict = false

export const state = () => ({
    user: null,
    show_favorite_modal_flag: false,
    show_delete_favorite_modal_flag: false,
})

export const mutations = {
    setUser(state, payload) {
        state.user = payload
    },
    showFavoriteModal(state){
        state.show_favorite_modal_flag = true;
    },
    showDeleteFavoriteModal(state){
        state.show_delete_favorite_modal_flag = true;
    },
    closeFavoriteModal(state){
        state.show_favorite_modal_flag = false;
        state.show_delete_favorite_modal_flag = false;
    }
}

export const actions = {
    signInWithGoogle({ commit }){
        const auth = getAuth()
        return signInWithPopup(auth, new GoogleAuthProvider())
    },

    signOut() {
        const auth = getAuth()
        return signOut(auth)
    },
}

export const getters = {
    user(state){
        return state.user
    },
    isAuthenticated (state) {
        return !!state.user
    }
}
