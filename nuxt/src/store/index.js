import { getAuth, signInWithPopup, GoogleAuthProvider, signOut } from "firebase/auth";

export const strict = false

export const state = () => ({
    user: null,
})

export const mutations = {
    setUser(state, payload) {
        state.user = payload
    },
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
