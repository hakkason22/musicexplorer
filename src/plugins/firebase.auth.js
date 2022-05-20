import { getAuth, onAuthStateChanged } from 'firebase/auth'

export default (context) => {
    const { store } = context

    return new Promise((resolve, reject) => {
        const auth = getAuth()
        onAuthStateChanged(auth, user => {
            store.commit('setUser', user)
            resolve()
        })
    })
}
