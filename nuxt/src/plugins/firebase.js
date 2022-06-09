import { initializeApp } from 'firebase/app'
import { getAnalytics } from 'firebase/analytics'

const config = {
    apiKey: "AIzaSyDe1PpoceboJ2VIxfk0pvKoeukTOcDw47k",
    authDomain: "musicexplorer-cae13.firebaseapp.com",
    projectId: "musicexplorer-cae13",
    storageBucket: "musicexplorer-cae13.appspot.com",
    messagingSenderId: "213690870691",
    appId: "1:213690870691:web:addad82d8de84821948816",
    measurementId: "G-XFPY4FYQ3M"
}

const firebase = initializeApp(config)
const analytics = getAnalytics(firebase)

// export const auth = firebase.auth
export default firebase
